# _*_coding:utf-8_*_
import os

__author__ = 'C.G.William / Weerdo5255'

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'

from pytz import timezone
from datetime import datetime
import Commands
import Tagger
import praw
import obot
import time
import sqlite3
import sys
import random

from django.utils.encoding import smart_str

shutdown = False


# Load the submission ID's from posts that have already been processed.
def load_previous_submissions():
    with open('Submissions.txt', 'r') as f:
        subdone = [line.strip() for line in f]
    return subdone

# Load AI phrases
def load_ai_phrase():
    with open('thoughts.txt', 'r') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase

# Search all of the submissions searching for any mention of keyword
def post_search(subreddit, subdone):
    for submission in subreddit.get_new(limit=20):
        if submission.id in subdone:
            continue

        subdone.append(submission.id)
        file = open("Submissions.txt", "a")
        file.write(str(submission.id) + "\n")
        file.close()

        if "Penny" in str(submission.title):
            submission.add_comment(
                "Who is that good looking robot? \n Pennybot stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)")
            Tagger.internaltag('penny', str(comment.submission.url), str(comment.submission.title),
                               int(comment.submission.created_utc))
            print("I found a Penny! in post: " + submission.id)

# Load all comments that have been processed
def already_processed_comments():
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # db_path = os.path.join(BASE_DIR, "Processed.db")
    db = sqlite3.connect('Processed.db')
    # with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    already_done = set()
    cursor.execute("SELECT * FROM Processed")
    results = cursor.fetchall()
    for row in results:
        Done_db = row[0]
        already_done.add(str(Done_db).replace(" ' ", ""))
    db.close()

    return already_done

# Check the inbox for messages
def get_messages():
    messages = r.get_unread()

    for message in messages:
        text = str(message.body)
        title = str(message.subject)
        message.mark_as_read()

        if "report" in text or "Report" in text or "report" in title or "Report" in title:
            print("Sending a report to: " + str(message.author))
            sendstring = str(Tagger.tagcollect())
            r.send_message(message.author, "A Pennybot Report!", sendstring)

def get_my_cake_day(username):
    try:
        redditor = r.get_redditor(username)
        return time.strftime("%m%d", time.gmtime(redditor.created_utc))
    except praw.errors.NotFound:
        print("No Cake Day")

# Determine what the comment is and the needed response
def find_penny_comment(flat_comments, processing, mods):
    global shutdown
    # Don't care about where the comments are so flatten the comment tree
    for comment in flat_comments:
        # Divide the body of all of the comments so we can scan each line correctly

        if comment.id not in processing:
            continue
        replied = False
        response = []

        commentauthor = str(comment.author)
        wholecomment = comment.body
        list = wholecomment.splitlines(True)
        reply = ''

        for current in list:
            # Looking at each line of a body comment turn it lower case and cut out v2
            current = current.lower()
            current = current.replace("v2", "")

            # Scan for mention of pennybot and respond
            if "pennybot," in current:
                print("Found a Penny comment at: " + time.asctime(time.localtime(time.time())))
                lookingfor = "pennybot,"

                # Remove pennybot from the string start scanning for response
                indexcount = current.index(lookingfor) + 9
                current = current.lstrip(current[:indexcount])
                current = current.strip()
                replied = True

                if current.startswith("tag report"):
                    sendstring = str(Tagger.tagcollect())
                    r.send_message(commentauthor, "A Pennybot Report!", sendstring)
                    reply = "I've sent you the report!"

                # Add to the suggestion text file
                elif current.startswith("suggestion"):
                    reply = "Thank you for the command suggestions! \n Creator! /u/Weerdo5255 ! Someone has made an excellent suggestion for a command! \n (PennyBotV2 has saved this suggestion, even if the creator does not respond!)"
                    filesug = open("Suggestions.txt", "a")
                    filesug.write(str(wholecomment) + "FROM:" + str(commentauthor) + "\n")
                    filesug.close()

                elif current.startswith("tag"):
                    reply = Tagger.replytag(current, str(comment.submission.url), str(comment.submission.title),
                                            int(comment.submission.created_utc))

                # Access the AI Function
                elif current.startswith("thoughts"):
                    thoughtstring = " "
                    randomnum = (random.randint(0, 3))
                    try:
                        x = 0
                        phrases = load_ai_phrase()
                        while (x <= randomnum):
                            thoughtstring = thoughtstring + random.choice(phrases) + "\n"
                            x += 1
                    except:
                        thoughtstring = ("I don't have any thoughts at the moment.")

                    reply = thoughtstring

                elif current.startswith("shutdown"):
                    print(commentauthor)
                    if commentauthor in mods or commentauthor == "Weerdo5255":
                        reply = "Emergency Shutdown Initiated! Bye!"
                        shutdown = True
                    else:
                        reply = "You are not Pyrrha!"

                elif current.startswith("statistics"):
                    db = sqlite3.connect("Processed.db")
                    db.text_factory = str
                    cursor = db.cursor()
                    cursor.execute('SELECT COUNT(Response), Response FROM Processed WHERE Response is not null GROUP BY Response ORDER BY COUNT(Response) DESC')
                    rows = cursor.fetchall()
                    rows_result = [row for row in rows]
                    rows_result = rows_result[1:6]
                    print(rows_result)
                    stringout = ""
                    #reply = '\n \n '.join(str(p.replace("(")) for p in rows_result)
                    for i in rows_result:
                        string = str(i)
                        string = string.replace('(', "", 1)
                        string = string.replace('"', "", 1)
                        string = string.replace("'", "", 1)
                        string = string.replace(',', "|", 1)

                        string = string[:-2]
                        stringout += (string + "\n")
                    reply = "Count | Response \n :--|:-- \n" + stringout
                    db.close()

                elif current.startswith("ignore") or current.startswith("mute"):
                    submission = comment.submission.id
                    print(submission)
                    postauthor = comment.submission.author
                    print(commentauthor)
                    print(postauthor)
                    if commentauthor in mods or commentauthor == "Weerdo5255":
                        reply = "Sorry! I'll be quite!"
                        file = open("ignore.txt", "a")
                        file.write(str(submission.id) + "\n")
                        file.close()
                    elif str(commentauthor) == str(postauthor):
                        reply = "Sorry! I'll be quite!"
                        file = open("ignore.txt", "a")
                        file.write(str(submission) + "\n")
                        file.close()
                    else:
                        reply = "You do not have sufficient privileges for that action."

                elif current.startswith("pennycheck"):
                    lookingfor = "pennycheck"
                    indexcount = current.index(lookingfor) + 10
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    reply = "[Here are the Images I could Find!](http://iqdb.org/?url=" + current + ")"

                elif current.startswith("pennykarma"):
                    reply = "Here is the [Karma Decay](http://karmadecay.com/" + str(
                    comment.submission.url) + ")"
                else:
                    reply = Commands.penny_commands(current, str(comment.submission.url), str(comment.submission.title),
                                                    int(comment.submission.created_utc))

                response.append(reply)

        if replied:
            print(comment.submission.permalink)
            print(response)
            cake = get_my_cake_day(commentauthor)
            print(cake)
            now_utc = datetime.now(timezone('UTC'))
            now_pacific = now_utc.astimezone(timezone('US/Pacific'))
            nowp = now_pacific.strftime("%m%d")
            print(nowp)
            if nowp == cake:
                string = ""
                for x in response:
                    string += x + " \n \n"
                comment.reply(string + "\n \n Pennybot wishes you a Happy Cake Day as well!")
            else:
                string = ""
                for x in response:
                    string += x + " \n \n"
                comment.reply(string)

        db = sqlite3.connect("Processed.db")
        db.text_factory = str
        cursor = db.cursor()
        cursor.execute('INSERT INTO Processed VALUES (?, ?, ?, ?, ?, ?)',
                       (str(comment.id), int(comment.created_utc), str(comment.body), str(comment.author), str(replied),
                        str(reply)))
        cursor.execute("DELETE FROM Processed WHERE time <= strftime('%s') - 86400 * 2;")
        db.commit()
    return comment.id


while True:
    if shutdown == True:
        sys.exit()

    try:
        # Reddit login

        r = obot.login()
        subreddit = r.get_subreddit('rwby')

        # Retrive mods of the subreddit for use in shutdown

        mods = r.get_moderators(subreddit)

        subdone = load_previous_submissions()

        post_search(subreddit, subdone)

        subreddit_comments = subreddit.get_comments()
        flat_comments = praw.helpers.flatten_tree(subreddit_comments)

        already_done = already_processed_comments()

        processing = set()

        for comment in flat_comments:
            processing.add(comment.id)
        processing = processing - already_done

        commentid = find_penny_comment(flat_comments, processing, mods)

        get_messages()

        already_done.add(commentid)

        file = open("Logs.txt", "a")
        file.write("I ran successfully at: " + smart_str(time.asctime(time.localtime(time.time())) + "\n"))
        file.close()
        print("I ran successfully at: " + time.asctime(time.localtime(time.time())))

    except Exception as e:
        file = open("Logs.txt", "a")
        file.write(
            "!! I didn't Run at !!: " + smart_str(time.asctime(time.localtime(time.time())) + smart_str(e) + "\n"))
        file.close()
        print("!! I didn't Run at: " + smart_str(time.asctime(time.localtime(time.time())) + smart_str(e) + "\n"))

    time.sleep(70)
