import csv
import obot
import commands
import sqlite3
import time
import random
import praw
import sys
import re
from random import randint
import random
from datetime import datetime
from pytz import timezone

shutdown = False


def load_previous_comments():
    db = sqlite3.connect('Rdatabase.db')
    cursor = db.cursor()
    coms = set()
    cursor.execute("SELECT commentid FROM Rdatabase where Time >= (SELECT max(time) from Rdatabase) - 172800")
    results = cursor.fetchall()
    for row in results:
        coms.add(row[0])
    return coms


def load_ai_phrase():
    with open('thoughts.txt', 'r') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase


def load_random_phrase():
    with open('Commands.txt', 'r', encoding='utf8') as f:
        randomcmd = [line.strip() for line in f]
    return randomcmd


def load_ignore():
    with open('ignore.txt', 'r', encoding='utf8') as f:
        ignorelist = [line.strip() for line in f]
    return ignorelist


def get_my_cake_day(username):
    try:
        redditor = r.redditor(username)
        return time.strftime("%m%d", time.gmtime(redditor.created_utc))
    except praw.errors.NotFound:
        print("No Cake Day")


def ship_search(name1, name2):
    response = "I have no data on " + name1 + " X " + name2 + ". [You could fill in the shipsheet?](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"
    with open('Main.csv', 'r') as f:
        reader = csv.reader(f)
        columnlist = next(reader)
        if name2 in columnlist:
            x = columnlist.index(name2)
        try:
            for row in reader:
                if str(row[0]) == name1:
                    if str(row[x]).isspace():
                        response1 = "BLANK DATA. [You could fill in the shipsheet?](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"
                    else:
                        response1 = (row[x])
                        print(row[x])
                    response = name1 + " X " + name2 + " is called: " + response1
        except:
            pass
    return response


def ot3_search(name1, name2, name3):
    try:
        with open('OT3.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            fulllist = (list(reader))
            for sublist in fulllist:
                if name1 in sublist:
                    if name2 in sublist:
                        if name3 in sublist:
                            othervalue = str(sublist).encode('utf-8').strip()
            othervalue = str(othervalue.decode('utf-8'))
            commaindex = othervalue.index(',') - 1
            othervalue = othervalue[2:commaindex]
            response = othervalue
            response = name1 + " X " + name2 + " X " + name3 + " is called: " + response
    except:
        response = "I have no data on " + name1 + " X " + name2 + " X " + name3 + ". [You could fill in the shipsheet?](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"
    return response


def proccess_comments(current, comment, choice):
    # Add to the suggestion text file
    if current.startswith("suggestion"):
        reply = "[You can make Suggestions here!](https://goo.gl/forms/NKGPxdJzxh87dsjv2) \n \n Pennybot has saved this comment as well! \n \n ^^^^^^^^/u/weerdo5255 "
        filesug = open("Suggestions.txt", "a")
        filesug.write(str(comment.body) + "FROM:" + str(comment.author) + "\n")
        filesug.close()

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

    elif current.startswith("shutdown") or current.startswith("shut down"):
        print(comment.author)
        if comment.author in mods or comment.author == "Weerdo5255":
            print("Emergency Shutdown Initiated! At: " + time.asctime(time.localtime(
                time.time())))
            sys.exit()
        else:
            reply = "You are not Pyrrha!"

    elif current.startswith("statistics"):
        db = sqlite3.connect("Rdatabase.db")
        db.text_factory = str
        cursor = db.cursor()
        cursor.execute(
            "SELECT COUNT(Body), Body FROM Rdatabase WHERE Body is not null AND Author = 'PennyBotV2' GROUP BY Body ORDER BY COUNT(Body) DESC")
        rows = cursor.fetchall()
        rows_result = [row for row in rows]
        rows_result = rows_result[1:6]
        print(rows_result)
        stringout = ""
        # reply = '\n \n '.join(str(p.replace("(")) for p in rows_result)
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

    elif current.startswith("meat person list"):
        db = sqlite3.connect("Cdatabase.db")
        db.text_factory = str
        cursor = db.cursor()
        cursor.execute(
            "SELECT Distinct Comment_Author, count(Body) FROM Cdatabase WHERE Body LIKE '%pennybot,%' OR Body LIKE '%Pennybot,%' OR Body LIKE '%PennyBot,%' OR Body LIKE '%PB,%' OR Body LIKE '%pb,%' OR Body LIKE '%pennybotv2,%' GROUP BY Comment_Author ORDER BY count(Body) DESC;")
        rows = cursor.fetchall()
        db.close()
        rows_result = [row for row in rows]
        rows_result = rows_result[3:10]
        print(rows_result)
        stringout = ""
        # reply = '\n \n '.join(str(p.replace("(")) for p in rows_result)
        for i in rows_result:
            string = str(i)
            string = string.replace('(', "", 1)
            string = string.replace('"', "", 1)
            string = string.replace("'", "", 1)
            string = string.replace("'", "", 1)
            string = string.replace(',', "|", 1)

            string = string[:-1]
            stringout += (string + "\n")
        reply = "Meat Person | Rank \n :--|:-- \n" + stringout


    elif current.startswith("ignore") or current.startswith("mute"):
        submission = comment.submission.id
        print(submission)
        postauthor = comment.submission.author
        print(postauthor)
        if str(comment.author) in mods or str(comment.author) == "Weerdo5255":
            reply = "Sorry! I'll be quite!"
            file = open("ignore.txt", "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
        elif str(comment.author) == str(postauthor):
            reply = "Sorry! I'll be quite!"
            file = open("ignore.txt", "a")
            file.write(str(comment.submission.id) + "\n")
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

    elif current.startswith("random"):
        phrases = load_random_phrase()
        current = str(random.choice(phrases))
        current = current.lower()
        print(current)
        reply = commands.penny_commands(current)
        reply = "My " + current + " Command:     " + reply

    elif current.startswith("<"):
        try:
            index1 = current.index(' ')
            index2 = current.index(' ', index1 + 1)
            index3 = current.index(' ', index2 + 1)
            index4 = current.index('>')
            name1 = current[1:index1]
            name2 = current[index2 + 1:index3]
            name3 = current[index3 + 3:index4]
            reply = ot3_search(name1.title(), name2.title(), name3.title())
        except:
            index1 = current.index(' ')
            index2 = current.index(' ', index1 + 1)
            index4 = current.index('>')
            name1 = current[1:index1]
            name2 = current[index2 + 1:index4]
            reply = ship_search(name1.title(), name2.title())

    else:
        reply = commands.penny_commands(current, choice)

    return reply


def find_mispelling(comment):
    reply = ""
    if "phyrra" in comment:
        reply = "[Phyrra](http://streamable.com/c0fel)? Do you mean Pyrrha?"
    elif "pyrah" in comment:
        reply = "[Pyrah](https://streamable.com/rpnvt)? Do you mean Pyrrha?"
    elif "phyrrah" in comment:
        reply = "[Phyrrah](http://streamable.com/jsf47)? Do you mean Pyrrha?"
    elif "phyrrha" in comment:
        reply = "[Phyrrha](https://streamable.com/60hdz)? Do you mean Pyrrha?"
    elif "phryrra" in comment:
        reply = "[Phryrra](http://streamable.com/jc9af)? Do you mean Pyrrha?"
    elif "pyhrra" in comment:
        reply = "[Pyhrra](http://streamable.com/11tag)? Do you mean Pyrrha?"
    elif "pyrrah" in comment:
        reply = "[Pyrrah](http://streamable.com/ks8mf)? Do you mean Pyrrha?"
    elif "phrrya" in comment:
        reply = "[Phrrya](http://streamable.com/t4hg5)? Do you mean Pyrrha?"
    elif "pyrhha" in comment:
        reply = "[Pyrhha](http://streamable.com/ovdli)? Do you mean Pyrrha?"
    elif "pirrah" in comment:
        reply = "[Pirrah](http://streamable.com/nm2lz)? Do you mean Pyrrha?"
    elif "piera" in comment:
        reply = "[Piera](http://streamable.com/8aken)? Do you mean Pyrrha?"
    elif "pyra" in comment:
        reply = "[Pyra](http://streamable.com/ys90o)? Do you mean Pyrrha?"
    elif "pyhra" in comment:
        reply = "[Pyhra](http://streamable.com/q4vm1)? Do you mean Pyrrha?"
    elif "pierra" in comment:
        reply = "[Pierra](http://streamable.com/h8qxx)? Do you mean Pyrrha?"
    elif "pierah" in comment:
        reply = "[Pierah](http://streamable.com/gkd5o)? Do you mean Pyrrha?"
    elif "priah" in comment:
        reply = "[Priah](http://streamable.com/qcp0p)? Do you mean Pyrrha?"
    elif "phyrria" in comment:
        reply = "[Phyrria](http://streamable.com/8hqps)? Do you mean Pyrrha?"
    elif "pyrra" in comment:
        reply = "[Pyrra](http://streamable.com/d4nnu)? Do you mean Pyrrha?"
    elif "pyrhaa" in comment:
        reply = "[Pyrhaa](http://streamable.com/iiz8c)? Do you mean Pyrrha?"
    elif "pyyra" in comment:
        reply = "[Pyyra](http://streamable.com/ww1gk)? Do you mean Pyrrha?"
    elif "pyrrea" in comment:
        reply = "[Pyrrea](http://streamable.com/cyehb)? Do you mean Pyrrha?"
    elif "pureha" in comment:
        reply = "[Pureha](http://streamable.com/inysv)? Do you mean Pyrrha?"
    elif "pharah" in comment:
        reply = "[Pharah](http://streamable.com/i0ttw)? Do you mean Pyrrha?"
    elif "pharaoh" in comment:
        reply = "[Pharaoh](http://streamable.com/v12ah)? Do you mean Pyrrha?"
    elif "pyhhra" in comment:
        reply = "[Pyhhra](http://streamable.com/clfwa)? Do you mean Pyrrha?"
    elif "pyrhha" in comment:
        reply = "[Pyrhha](http://streamable.com/rmn9d)? Do you mean Pyrrha?"
    elif "pyhraa" in comment:
        reply = "[Pyhraa](http://streamable.com/we8bd)? Do you mean Pyrrha?"
    elif "pyyrah" in comment:
        reply = "[Pyyrah](http://streamable.com/lsjn2)? Do you mean Pyrrha?"
    elif "phyyra" in comment:
        reply = "[Phyyra](http://streamable.com/x8i9j)? Do you mean Pyrrha?"
    elif "pryyha" in comment:
        reply = "[Pryyha](http://streamable.com/5wbug)? Do you mean Pyrrha?"
    elif "pyyrha" in comment:
        reply = "[Pyyrha](http://streamable.com/34og7)? Do you mean Pyrrha?"
    elif "phyra" in comment:
        reply = "[Phyra](https://streamable.com/3nbyt)? Do you mean Pyrrha?"
    elif "prryha" in comment:
        reply = "[Prryha](http://streamable.com/0sj7t)? Do you mean Pyrrha?"
    elif "pyraah" in comment:
        reply = "[Pyraah](http://streamable.com/srreq)? Do you mean Pyrrha?"
    elif "pearhat" in comment:
        reply = "[Pearhat](http://streamable.com/i8z81)? Do you mean Pyrrha?"
    elif "pyyrahe" in comment:
        reply = "[Pyyrahe](http://streamable.com/upyvf)? Do you mean Pyrrha?"
    elif "purra" in comment:
        reply = "[Purra](http://streamable.com/pwx3t)? Do you mean Pyrrha?"
    elif "prhhya" in comment:
        reply = "[Prhhya](http://streamable.com/8c471)? Do you mean Pyrrha?"
    elif "pyrrahe" in comment:
        reply = "[Pyrrahe](http://streamable.com/woxdj)? Do you mean Pyrrha?"
    return reply


def find_penny(comment):
    replied = False
    ignoreposts = load_ignore()
    author = str(comment.author)
    if comment.submission.id not in ignoreposts:
        response = []
        commentlist = str(comment.body).splitlines(True)
        if "PennyBotV2" in author:
            print("My Own Comment, ignoring.")
        else:
            for current in commentlist:
                # Looking at each line of a body comment turn it lower case and cut out v2
                current = current.lower()
                current = current.replace("v2", "")
                # Scan for mention of pennybot and respond
                if "pennybot," in current:
                    lookingfor = "pennybot,"
                    # Remove pennybot from the string start scanning for response
                    indexcount = current.index(lookingfor) + 9
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    try:
                        choice = int(re.search(r'\d+', current).group())
                        print(choice)
                    except:
                        choice = (randint(0, 9))
                    replied = True
                    txtreply = proccess_comments(current, comment, choice)
                    response.append(txtreply)
                elif "pb," in current:
                    lookingfor = "pb,"
                    # Remove pennybot from the string start scanning for response
                    indexcount = current.index(lookingfor) + 3
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    try:
                        choice = int(re.search(r'\d+', current).group())
                        print(choice)
                    except:
                        choice = (randint(0, 9))
                    replied = True
                    txtreply = proccess_comments(current, comment, choice)
                    response.append(txtreply)
                else:
                    txtreply = find_mispelling(current)
                    if txtreply is not "":
                        replied = True
                        response.append(txtreply)

    if replied:
        cake = get_my_cake_day(str(comment.author))
        now_utc = datetime.now(timezone('UTC'))
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        nowp = now_pacific.strftime("%m%d")
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
        print(
            "Found a Penny comment at: " + time.asctime(time.localtime(
                time.time())) + "\nIn thread: " + comment.submission.shortlink + " \nI responded with:" + "\n" + string)


def com_stream(subreddit, comdone):
    for comment in subreddit.stream.comments():
        if not str(comment.id) in comdone:
            db = sqlite3.connect("Rdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Rdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (
                               str(comment.submission.title), str(comment.submission.id),
                               str(comment.submission.shortlink),
                               str(comment.submission.score), str(comment.id), str(comment.score),
                               int(comment.created_utc),
                               str(comment.body), str(comment.author)))
            db.commit()
            comdone.add(comment.id)
            db = sqlite3.connect("Cdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Cdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (str(comment.submission.title), str(comment.submission.id), str(comment.submission.permalink),
                            str(comment.submission.shortlink), str(comment.submission.author), str(comment.author), str(comment.id),
                            int(comment.created_utc), str(comment.body), int(comment.score),
                            str(comment.author_flair_css_class), int(comment.created_utc)))
            db.commit()
            # print(str(comment.body).encode("utf-8"))
            find_penny(comment)


while True:
    try:
        mods = []
        r = obot.login()
        subreddit = r.subreddit('rwby')
        for moderator in subreddit.moderator():
            mods.append(str(moderator))
        print("The " + str(subreddit) + " Moderators: " + str(mods))
        # com_stream(subreddit, load_previous_comments())
        com_stream(subreddit, load_previous_comments())
    except Exception as e:
        print(e)
        print("Waiting 20 seconds to restart")
        time.sleep(20)
        pass
