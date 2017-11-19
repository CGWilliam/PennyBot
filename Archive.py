# _*_coding:utf-8_*_
import praw
import sqlite3
import obot
import time
r = obot.login()


subreddit = r.subreddit('rwby')
subdone = []


def load_previous_submissions():
    with open('Submissions.txt', 'r') as f:
        subdone = [line.strip() for line in f]
    return subdone

subdone = load_previous_submissions()

while True:
    for submission in subreddit.submissions(start=None, end=None):
        if submission.id in subdone:
            continue
        print(str(submission.title).encode('utf-8'))
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created_utc)))
        subdone.append(submission.id)
        file = open("Submissions.txt", "a")
        file.write(str(submission.id) + "\n")
        file.close()

        db = sqlite3.connect("Sdatabase.db")
        db.text_factory = str
        cursor = db.cursor()
        cursor.execute('INSERT INTO Sdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        (str(submission.title), str(submission.id),  str(submission.permalink), str(submission.shortlink), str(submission.author), str(submission.link_flair_css_class), str(submission.author_flair_css_class), str(submission.author_flair_text), submission.score, submission.view_count, int(submission.created_utc)))
        db.commit()


        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            db = sqlite3.connect("Cdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Cdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            (str(submission.title), str(submission.id),  str(submission.permalink), str(submission.shortlink), str(submission.author), str(comment.author), str(comment.id), int(comment.created_utc), str(comment.body), int(comment.score), str(comment.author_flair_css_class), int(comment.created_utc)))
            db.commit()
        time.sleep(5)