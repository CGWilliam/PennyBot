import datetime
import sys
import threading
import time
import json
from logging.handlers import RotatingFileHandler

import external_commands
from random import randint
from pytz import timezone
import private_credentials
import logging

Debug = True
Stream = False
S3Resources = True
celebrate_cake_day = True

log_level = logging.INFO
log_name = 'weerdbot.log'
log_size = 2048
maintainer = ['weerdo5255']
botname = ['weerdbot']
subreddit_list = ['test']
subreddit_advanced_scan = ['rwby', 'fnki', 'test']
comment_triggers = ['pb,', 'pb','wb,']
submission_triggers = ['penny']
json_memory_length = 86400
cake_day_message = "Happy Cake Day!"

Title_Flags = []
Comment_Flags = []
ignore_posts = []

r = private_credentials.reddit_login()
s3 = private_credentials.amazon_login()


def setup_logger():
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_name, mode='a')
    filehandler = RotatingFileHandler(log_name, maxBytes=log_size, backupCount=1)
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    logger.addHandler(filehandler)
    logger.addHandler(screen_handler)
    return logger


def find_user_cake_day(username):
    redditor = r.redditor(username)
    signuptime = time.strftime("%m%d", time.gmtime(redditor.created_utc))
    now_utc = datetime.datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    today = now_pacific.strftime("%m%d")
    if today == signuptime:
        return True
    else:
        return False


def comment_process(comment, complete_dict):
    reply = False
    comment_response = []
    log.debug('Processing comment: %s', str(comment.id))
    # Break the comment body down into lines and remove case.
    comment_lines = (str(comment.body).lower()).splitlines(True)
    for current_comment in comment_lines:
        log.debug('current comment line: %s', current_comment)
        # Look for any bot phrases in the current comment line.
        for trigger in complete_dict.keys():
            if trigger in current_comment:
                log.debug('Found Trigger in Comment: %s phrase is: %s', str(comment.id), current_comment)
                reply = True
                temp_dict = complete_dict.get(trigger)
                reply_string = temp_dict.get(str(randint(0, len(temp_dict)-1)))
                if reply_string.startswith("!!"):
                    log.info('Found a complex command Routing to Complex Commands.')
                    comment_response.append(external_commands.complex_commands(r, reply_string, comment, log, maintainer, complete_dict))
                else:
                    comment_response.append(reply_string)
        if str(comment.subreddit) in subreddit_advanced_scan:
            reply = True
            comment_response.append(external_commands.pyrrhascan(comment))

        for trigger in comment_triggers:
            if trigger in current_comment and reply is False:
                with open('data_sources/default_commands.json') as read:
                    json_default_commands = json.load(read)
                comment_response.append(json_default_commands.get(str(randint(0, len(json_default_commands) - 1))))

    if reply:
        log.debug('Responding to a comment: %s', str(comment.id))
        comment_reply_string = " \n \n".join(comment_response)
        if celebrate_cake_day:
            cake = find_user_cake_day(str(comment.author))
            if cake:
                comment_reply_string = " \n \n".join([comment_reply_string, cake_day_message])
        log.info('Replying to comment: %s with: %s', str(comment.id), comment_reply_string)
        comment.reply(comment_reply_string)


def subreddit_comment_ingest(subreddit, Stream, ignore_posts=[]):
    with open('data_sources/common_commands.json') as read:
        json_commands = json.load(read)
    complete_dict = {}
    for trigger in comment_triggers:
        for key in json_commands.keys():
            complete_dict.update({str(trigger + " " + key): json_commands.get(key)})
    global processed_reddit_comments

    try:
        with open('data_sources/processed_reddit_comments.json') as read:
            processed_reddit_comments = json.load(read)
    except Exception as e:
        log.warning("Error loading Already Processed Comments")
        log.warning(e)

    processed_comments = list(processed_reddit_comments.keys())

    if Stream:
        for comment in subreddit.stream.comments():
            if str(comment.id) not in processed_comments:
                if comment.author in botname:
                    log.debug('Comment is Bots, ignoring.')
                    continue
                elif comment.submission.id in ignore_posts:
                    log.debug('Comment is in post ignore list, ignoring.')
                    continue
                else:
                    log.debug("Processing Comment: " + str(comment.id) + "|||" + str(comment.body))
                    comment_process(comment, complete_dict)
                    processed_reddit_comments = {key: val for key, val in processed_reddit_comments.items() if not (time.time() - val) > json_memory_length}
                    processed_reddit_comments[str(comment.id)] = int(time.time())
                    with open('data_sources/processed_reddit_comments.json', 'w') as json_dump:
                        json.dump(processed_reddit_comments, json_dump)
    else:
        for comment in subreddit.comments():
            if str(comment.id) not in processed_comments:
                if comment.author in botname:
                    log.debug('Comment is Bots, ignoring.')
                    continue
                elif comment.submission.id in ignore_posts:
                    log.debug('Comment is in post ignore list, ignoring.')
                    continue
                else:
                    log.debug("Processing Comment: " + str(comment.id) + "|||" + str(comment.body))
                    comment_process(comment, complete_dict)
                    processed_reddit_comments = {key: val for key, val in processed_reddit_comments.items() if not (time.time() - val) > json_memory_length}
                    processed_reddit_comments[str(comment.id)] = int(time.time())
                    with open('data_sources/processed_reddit_comments.json', 'w') as json_dump:
                        json.dump(processed_reddit_comments, json_dump)


def subreddit_submissions_ingest(subreddits, Stream):
    global processed_reddit_submissions
    try:
        with open('data_sources/processed_reddit_submissions.json') as read:
            processed_reddit_submissions = json.load(read)
    except Exception as e:
        log.warning("Error loading Already Processed Submissions")
        log.warning(e)

    processed_submissions = list(processed_reddit_submissions.keys())

    if Stream:
        for submission in subreddits.stream.submissions():
            if str(submission.id) not in processed_submissions:
                if str(submission.title).lower() in submission_triggers:
                    processed_reddit_submissions = {key: val for key, val in processed_reddit_submissions.items() if
                                                    not (time.time() - val) > json_memory_length}
                    processed_reddit_submissions[str(submission.id)] = int(time.time())
                    with open('data_sources/processed_reddit_submissions.json', 'w') as json_dump:
                        json.dump(processed_reddit_submissions, json_dump)
                    with open('data_sources/default_reddit_posts.json') as read:
                        default_reddit_posts = json.load(read)
                    submission.reply(default_reddit_posts.get(str(randint(0, len(default_reddit_posts) - 1))))
    else:
        for submission in subreddits.new(limit=10):
            if str(submission.id) not in processed_submissions:
                if str(submission.title).lower() in submission_triggers:
                    processed_reddit_submissions = {key: val for key, val in processed_reddit_submissions.items() if
                                                    not (time.time() - val) > json_memory_length}
                    processed_reddit_submissions[str(submission.id)] = int(time.time())
                    with open('data_sources/processed_reddit_submissions.json', 'w') as json_dump:
                        json.dump(processed_reddit_submissions, json_dump)
                    with open('data_sources/default_reddit_posts.json') as read:
                        default_reddit_posts = json.load(read)
                    submission.reply(default_reddit_posts.get(str(randint(0, len(default_reddit_posts) - 1))))



def main():
    log.info('Logging service started')
    log.info('Loading data')
    subreddits = r.subreddit('+'.join(subreddit_list))
    log.info('Watching these Subreddits: %s', subreddits)

    if Stream:
        log.info('Utilizing Subreddit Streams')
        comment_thread = threading.Thread(target=subreddit_comment_ingest, args=(subreddits, ignore_posts))
        submission_thread = threading.Thread(target=subreddit_submissions_ingest, args=(subreddits,))
        log.info('Starting Threads.')
        comment_thread.start()
        time.sleep(5)
        submission_thread.start()
    else:
        log.info('Utilizing Subreddit Iteration')
        subreddit_submissions_ingest(subreddits, Stream)
        subreddit_comment_ingest(subreddits, Stream, ignore_posts)


log = setup_logger()
main()
