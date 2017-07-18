
import obot
import sqlite3
import time
from datetime import datetime


def load_previous_submissions():
    db = sqlite3.connect('Rdatabase.db')
    cursor = db.cursor()
    subs = set()
    cursor.execute("SELECT Submissionid FROM Rdatabase")
    results = cursor.fetchall()
    for row in results:
        subs.add(str(row[0]))
    return subs


def sub_stream(subreddit, subdone):
    #print(subdone)
    for submission in subreddit.stream.submissions():
        if not str(submission.id) in subdone:
            print(submission.id)
            db = sqlite3.connect("Rdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Rdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            (str(submission.title), str(submission.id), str(submission.shortlink), None,
                            None, None, None, None, None))
            db.commit()
            subdone.add(submission.id)
            print(str(submission.title).encode("utf-8"))
            title = str(submission.title).lower()
            if "penny" in title:
                submission.reply("Who is that good looking robot? \n Pennybot stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)")
                print("I found a Penny! in post: " + submission.id + " At: " + str(datetime.now()))


while True:
    try:
        mods = []
        r = obot.login()
        subreddit = r.subreddit('rwby')
        for moderator in subreddit.moderator():
            mods.append(str(moderator))
        #print("The " + str(subreddit) + " Moderators: " + str(mods))
        sub_stream(subreddit, load_previous_submissions())
    except Exception as e:
        print(e)
        print("Waiting 20 seconds to restart")
        time.sleep(20)
        pass





