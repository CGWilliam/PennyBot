

__author__ = 'C.G.William / Weerdo5255' \

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'

import Commands
import praw
import obot
import time
import sqlite3
import sys

shutdown = False

# Load the submission ID's from posts that have already been processed.
def load_previous_submissions():
    with open('Submissions.txt', 'r') as f:
        subdone = [line.strip() for line in f]
    return subdone

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
            submission.add_comment("Who is that good looking robot? \n Pennybot stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)")
            print("I found a Penny! in post: " + submission.id)

# Load all comments that have been processed
def already_processed_comments():
    db = sqlite3.connect("Processed.db")
    cursor = db.cursor()
    already_done = set()
    cursor.execute("SELECT * FROM Processed Post")
    results = cursor.fetchall()
    for row in results:
        Done_db = row[0]
        already_done.add(str(Done_db).replace(" ' ", ""))
    db.close()

    return already_done

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

        commentauthor = comment.author
        wholecomment = comment.body
        list = wholecomment.splitlines(True)
        reply = ''

        for current in list:
            # Looking at each line of a body comment turn it lower case and cut out v2
            current = current.lower()
            current = current.replace("v2", "")

            # Scan for mention of pennybot and respond
            if "pennybot," not in current:
                continue

            print("Found a Penny comment at: " + time.asctime(time.localtime(time.time())))
            lookingfor = "pennybot,"

            # Remove pennybot from the string start scanning for response
            indexcount = current.index(lookingfor) + 9
            current = current.lstrip(current[:indexcount])
            current = current.strip()
            replied = True


            if current.startswith("suggestion"):
                reply ="Thank you for the command suggestions! \n Creator! /u/Weerdo5255 ! Someone has made an excellent suggestion for a command! \n (PennyBotV2 has saved this suggestion, even if the creator does not respond!)"
                file = open("Suggestions.txt", "a")
                file.write(str(wholecomment) + "FROM:" + str(commentauthor) + "\n")
                file.close()

            #Emergency shutdown
            elif current.startswith("shutdown"):
                print(commentauthor)
                if commentauthor in mods or commentauthor == "Weerdo5255":
                    reply = "Emergency Shutdown Initiated! Bye!"
                    shutdown = True
                else:
                    reply = "You are not Pyrrha!"

            else:
                reply = Commands.penny_commands(current)


            response.append(reply)

        if replied:
            print(comment.submission.permalink)
            print(response)

            string = ""
            for x in response:
                string += x + " \n \n"
            comment.reply(string)

        db = sqlite3.connect("Processed.db")
        cursor = db.cursor()
        cursor.execute('INSERT INTO Processed VALUES (?, ?, ?, ?, ?, ?)',
                    (str(comment.id), int(comment.created_utc), str(comment.body), str(comment.author), str(replied), str(reply)))
        cursor.execute("DELETE FROM Processed WHERE time <= strftime('%s') - 86400 * 2;")
        db.commit()

    return comment.id


while True:
    if shutdown:
        sys.exit()

    try:
        # Reddit login

        r = obot.login()
        subreddit = r.get_subreddit('test')

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

        already_done.add(commentid)

        file = open("Logs.txt", "a")
        file.write("I ran successfully at: " + str(time.asctime( time.localtime(time.time())) + "\n"))
        file.close()
        print("I ran successfully at: " + time.asctime( time.localtime(time.time())))

    except Exception as e:
        file = open("Logs.txt", "a")
        file.write("!! I didn't Run at !!: " + str(time.asctime(time.localtime(time.time())) + "\n" + str(e) + "\n"))
        file.close()
        print("!! I didn't Run at: " + time.asctime(time.localtime(time.time())+ "\n" + str(e)))

    time.sleep(70)
