import datetime
import os
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

Debug = False
Stream = False
S3Resources = True
S3Logging = True
S3Bucket = private_credentials.amazon_bucket()
S3Region = private_credentials.amazon_region()
celebrate_cake_day = True

log_level = logging.INFO
log_name = 'weerdbot.log'
log_size = 2048
maintainer = 'weerdo5255'
botname = ['pennybotv2']
subreddit_list = ['rwby', 'fnki', 'club_penny', 'anime', 'genlock', 'roosterteeth', 'cgwilliam', 'hfy', 'c1764',
                  'airefuge', 'test']
subreddit_advanced_scan = ['rwby', 'fnki', 'club_penny']
comment_triggers = ['pb,', 'pennybot', 'pennybotv2', 'pennybot,', 'pennybotv2,']
submission_triggers = ['penny']
json_memory_length = 3600
cake_day_message = "PennybotV2 Wishes you a Happy Cake Day!"
banner_message = "--- \n \n ^^^^Bot ^^^^Created ^^^^by ^^^^/u/Weerdo5255 ^^^^See ^^^^Source ^^^^[Here.](" \
                 "https://github.com/CGWilliam/PennyBot) "
creator_message = "\n \n ^^^^Creator, ^^^^when ^^^^do ^^^^I ^^^^get ^^^^my ^^^^next ^^^^update?"

ignore_posts = []

r = None
s3 = None
loaded_comments = None

formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(log_name)
if not S3Logging:
    handler = logging.FileHandler(log_name, mode='a')
    filehandler = RotatingFileHandler(log_name, maxBytes=log_size, backupCount=1)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(filehandler)
screen_handler = logging.StreamHandler(stream=sys.stdout)
screen_handler.setFormatter(formatter)
logger.setLevel(log_level)
logger.addHandler(screen_handler)
log = logger

log.info('Logging service started')
log.info('Watching these Subreddits: %s', ' '.join(subreddit_list))
log.info('Watching these Subreddits for exact commands: %s', ' '.join(subreddit_advanced_scan))


def lambdar(r):
    if r is None:
        r = private_credentials.reddit_login()
        return r
    else:
        return r


def lamdas3(s3):
    if s3 is None:
        s3 = private_credentials.amazon_login()
        return s3
    else:
        return s3


def upload_comments_to_s3(upload_comments):
    if S3Resources:
        with open('/tmp/processed_reddit_comments.json', 'w') as json_dump:
            json.dump(upload_comments, json_dump)
        lamdas3(s3).Bucket(S3Bucket).upload_file('/tmp/processed_reddit_comments.json',
                                                 'processed_reddit_comments.json')
    else:
        with open('data_sources/processed_reddit_comments.json', 'w') as json_dump:
            json.dump(upload_comments, json_dump)


def comment_process(comment, complete_dict):
    reply = False
    comment_response = []
    log.debug('Processing comment: %s', str(comment.id))
    # Break the comment body down into lines and remove case.
    comment_lines = (str(comment.body).lower()).splitlines(True)
    for current_comment in comment_lines:
        log.debug('current comment line: %s', current_comment)
        # Look for any bot phrases in the current comment line.
        for trigger in sorted(complete_dict.keys(), key=len):
            if trigger in current_comment:
                log.debug('Found Trigger in Comment: %s phrase is: %s', str(comment.id), current_comment)
                temp_dict = complete_dict.get(trigger)
                reply_string = temp_dict.get(str(randint(0, len(temp_dict) - 1)))
                if reply_string.startswith("!!"):
                    log.info('Found a complex command Routing to Complex Commands.')
                    comment_response.append(
                        external_commands.complex_commands(r, S3Bucket, reply_string, comment, current_comment, log,
                                                           maintainer, complete_dict))
                else:
                    comment_response.append(reply_string)
                reply = True

        if str(comment.subreddit) in subreddit_advanced_scan:
            pyrrha_response = external_commands.pyrrhascan(comment, S3Bucket)
            if pyrrha_response is not None:
                comment_response.append(pyrrha_response)
                reply = True

        for trigger in comment_triggers:
            if trigger in current_comment and reply is False and str(comment.subreddit) in subreddit_advanced_scan:
                if S3Resources:
                    lamdas3(s3).Bucket(S3Bucket).download_file('default_commands.json', '/tmp/default_commands.json')
                    with open('/tmp/default_commands.json') as read:
                        json_default_commands = json.load(read)
                else:
                    with open('data_sources/default_commands.json') as read:
                        json_default_commands = json.load(read)
                comment_response.append(json_default_commands.get(str(randint(0, len(json_default_commands) - 1))))
                reply = True

    if reply:
        log.debug('Responding to a comment: %s', str(comment.id))
        comment_reply_string = " \n \n".join(comment_response)
        if celebrate_cake_day:
            redditor = lambdar(r).redditor(str(comment.author))
            signuptime = time.strftime("%m%d", time.gmtime(redditor.created_utc))
            now_utc = datetime.datetime.now(timezone('UTC'))
            now_pacific = now_utc.astimezone(timezone('US/Pacific'))
            today = now_pacific.strftime("%m%d")
            if today == signuptime:
                comment_reply_string = " \n \n".join([comment_reply_string, cake_day_message])
        if str(comment.subreddit) in subreddit_advanced_scan:
            comment_reply_string = "\n \n ".join([comment_reply_string, banner_message])
        if maintainer in str(comment.author).lower():
            comment_reply_string = "\n \n ".join([comment_reply_string, creator_message])
        log.info('Replying to comment: %s with: %s', str(comment.id), comment_reply_string)
        comment.reply(comment_reply_string)


def subreddit_comment_process(comment):
    if S3Resources:
        lamdas3(s3).Bucket(S3Bucket).download_file('ignore.txt', '/tmp/ignore.txt')
        with open('/tmp/ignore.txt', 'r', encoding='utf8') as f:
            ignore_these_posts = [line.strip() for line in f]
    else:
        with open('data_sources/ignore.txt', 'r', encoding='utf8') as f:
            ignore_these_posts = [line.strip() for line in f]

    if S3Resources:
        lamdas3(s3).Bucket(S3Bucket).download_file('processed_reddit_comments.json',
                                                   '/tmp/processed_reddit_comments.json')
        with open('/tmp/processed_reddit_comments.json') as read:
            processed_reddit_comments = json.load(read)
    else:
        with open('data_sources/processed_reddit_comments.json') as read:
            processed_reddit_comments = json.load(read)
    processed_comments = list(processed_reddit_comments.keys())
    if str(comment.id) not in processed_comments:
        if comment.author in botname:
            log.debug('Comment is Bots, ignoring.')
        elif comment.submission.id in ignore_these_posts:
            log.debug('Comment is in post ignore list, ignoring.')
        else:
            if S3Resources:
                lamdas3(s3).Bucket(S3Bucket).download_file('common_commands.json', '/tmp/common_commands.json')
                with open('/tmp/common_commands.json') as read:
                    json_commands = json.load(read)
            else:
                with open('data_sources/common_commands.json') as read:
                    json_commands = json.load(read)
            complete_dict = {}
            for trigger in comment_triggers:
                for key in json_commands.keys():
                    complete_dict.update({str(trigger + " " + key): json_commands.get(key)})
            log.debug("Processing Comment: " + str(comment.id) + " ||| " + str(comment.body))
            comment_process(comment, complete_dict)
            processed_reddit_comments = {key: val for key, val in processed_reddit_comments.items() if
                                         not (time.time() - val) > json_memory_length}
            processed_reddit_comments[str(comment.id)] = int(time.time())
            strtime = time.strftime("%H%M%S", time.localtime())
            if strtime.endswith("00") and Stream:
                upload_comments_to_s3(processed_reddit_comments)
    return processed_reddit_comments


def subreddit_submission_process(submission):
    if str(submission.subreddit) in subreddit_advanced_scan:
        if S3Resources:
            lamdas3(s3).Bucket(S3Bucket).download_file('processed_reddit_submissions.json',
                                                       '/tmp/processed_reddit_submissions.json')
            with open('/tmp/processed_reddit_submissions.json') as read:
                processed_reddit_submissions = json.load(read)
        else:
            with open('data_sources/processed_reddit_submissions.json') as read:
                processed_reddit_submissions = json.load(read)
        processed_submissions = list(processed_reddit_submissions.keys())
        if str(submission.id) not in processed_submissions:
            if str(submission.title).lower() in submission_triggers:
                if S3Resources:
                    lamdas3(s3).Bucket(S3Bucket).download_file('default_reddit_posts.json',
                                                               '/tmp/default_reddit_posts.json')
                    with open('/tmp/default_reddit_posts.json') as read:
                        default_reddit_posts = json.load(read)
                else:
                    with open('data_sources/default_reddit_posts.json') as read:
                        default_reddit_posts = json.load(read)
                submission.reply(default_reddit_posts.get(str(randint(0, len(default_reddit_posts) - 1))))

        processed_reddit_submissions = {key: val for key, val in
                                        processed_reddit_submissions.items() if
                                        not (time.time() - val) > json_memory_length}
        processed_reddit_submissions[str(submission.id)] = int(time.time())
        if S3Resources:
            with open('/tmp/processed_reddit_submissions.json', 'w') as json_dump:
                json.dump(processed_reddit_submissions, json_dump)
            lamdas3(s3).Bucket(S3Bucket).upload_file('/tmp/processed_reddit_submissions.json',
                                                     'processed_reddit_submissions.json')
        else:
            with open('data_sources/processed_reddit_submissions.json', 'w') as json_dump:
                json.dump(processed_reddit_submissions, json_dump)


def subreddit_comment_ingest(subreddit, stream_ingest):
    if stream_ingest:
        for comment in subreddit.stream.comments():
            subreddit_comment_process(comment)

    else:
        for comment in subreddit.comments():
            processed_comments = subreddit_comment_process(comment)
            upload_comments_to_s3(processed_comments)


def subreddit_submissions_ingest(subreddits, stream_ingest):
    if stream_ingest:
        for submission in subreddits.stream.submissions():
            subreddit_submission_process(submission)
    else:
        for submission in subreddits.new():
            subreddit_submission_process(submission)


def main():
    subreddits = lambdar(r).subreddit('+'.join(subreddit_list))
    advanced_subreddits = lambdar(r).subreddit('+'.join(subreddit_advanced_scan))

    if not os.path.isdir('/tmp'):
        os.mkdir('/tmp')

    if Stream:
        log.info('Utilizing Subreddit Streams')
        comment_thread = threading.Thread(target=subreddit_comment_ingest,
                                          args=(subreddits, advanced_subreddits, Stream))
        submission_thread = threading.Thread(target=subreddit_submissions_ingest,
                                             args=(subreddits, advanced_subreddits, Stream))
        log.info('Starting Threads.')
        comment_thread.start()
        time.sleep(1)
        submission_thread.start()
    else:
        log.debug('Utilizing Subreddit Iteration')
        subreddit_comment_ingest(subreddits, Stream)
        subreddit_submissions_ingest(subreddits, Stream)


main()
