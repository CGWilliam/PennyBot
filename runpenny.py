
import csv
import obot
import time
import sys
import re
from random import randint
import random
import datetime
from pytz import timezone
import pymysql

shutdown = False
debug = False

# Declare those connections and variables that we don't want in public code.
# Log into Amazon and Reddit.
r = obot.reddit_login()
db = obot.db_login()
bucket = obot.s3_bucket()

mods = []
subredditlist = ['test','rwby','fnki']
for sub in subredditlist:
    for moderator in r.subreddit(sub).moderator():
        mods.append(str(moderator))
    subjoin = "+"
    subreddit = r.subreddit(subjoin.join(subredditlist))
    print("The " + str(subreddit) + " Moderators: " + str(mods))


def load_previous_comments():
    if debug:
        print("Connecting to DB loading previous comments")

    cursor = db.cursor()
    coms = set()
    cursor.execute("SELECT commentid FROM Rdatabase where Time >= (SELECT max(time) from Rdatabase) - 172800")
    results = cursor.fetchall()
    if debug:
        print("Database Returned: " + str(results))
    for row in results:
        coms.add(row[0])
    return coms


def load_ai_phrase():
    bucket.download_file('thoughts.txt', '/tmp/thoughts.txt')
    with open('/tmp/thoughts.txt', 'r') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase


def load_random_phrase():
    bucket.download_file('Commands.txt', '/tmp/Commands.txt')
    with open('/tmp/Commands.txt', 'r', encoding='utf8') as f:
        randomcmd = [line.strip() for line in f]
    return randomcmd


# This really needs to be a table in the DB...
def load_ignore():
    bucket.download_file('ignore.txt', '/tmp/ignore.txt')
    with open('/tmp/ignore.txt', 'r') as f:
        ignorelist = [line.strip() for line in f]
    return ignorelist


# Humans Can't spell. Let's not correct them everytime.
def load_pignore():
    bucket.download_file('pyrrhaignore.txt', '/tmp/pyrrhaignore.txt')
    with open('/tmp/pyrrhaignore.txt', 'r') as f:
        ignorelist = [line.strip() for line in f]
    return ignorelist


def get_my_cake_day(username):
    try:
        redditor = r.redditor(username)
        return time.strftime("%m%d", time.gmtime(redditor.created_utc))
    except:
        print("No Cake Day")


# Need to create the method to pull in the public versions of the Ships sheets to make them self updating. For now
# we're pulling a local copy.
def ship_search(name1, name2):
    response = "I have no data on " + name1 + " X " + name2 + ". [You could fill in the shipsheet?](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"
    bucket.download_file('Main.csv', '/tmp/Main.csv')
    with open('/tmp/Main.csv', 'r') as f:
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
        bucket.download_file('OT3.csv', '/tmp/OT3.csv')
        with open('/tmp/OT3.csv', 'r') as f:
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


def load_ai_phrase():
    bucket.download_file('thoughts.txt', '/tmp/thoughts.txt')
    with open('/tmp/thoughts.txt', 'r', encoding='utf8') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase


def proccess_comments(current, comment, choice):
    bucket.download_file('commands.json', '/tmp/commands.json')
    search = current.lower()
    if debug:
        print("Got to Process_Comments")

    if search.startswith("suggestion"):
        bucket.download_file('suggestions.txt', '/tmp/suggestions.txt')
        reply = "[You can make Suggestions here!](" \
                "https://docs.google.com/forms/d/e/1FAIpQLScp8yibCZRKqNcvvUT69VfEs2inp4DvNFvakGWubIAyv8D4EA/viewform" \
                "?usp=sf_link) \n \n Pennybot has saved this comment as well! \n \n ^^^^^^^^/u/weerdo5255 "
        filesug = open('/tmp/Suggestions.txt', "a")
        filesug.write(str(comment.body) + "FROM:" + str(comment.author) + "\n")
        filesug.close()
        bucket.upload_file('suggestions.txt', '/tmp/suggestions.txt')

    elif search.startswith("thoughts"):
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

    elif search.startswith("shutdown") or search.startswith("shut down"):
        print(comment.author)
        if comment.author in mods or comment.author == "Weerdo5255":
            print("Emergency Shutdown Initiated! At: " + time.asctime(time.localtime(
                time.time())))
            sys.exit()
        else:
            reply = "You are not Pyrrha!"

    elif search.startswith("program"):
        import json
        print("Someone is attempting to program a new command.")
        if comment.author == "Weerdo5255":
            try:
                # Remove pennybot from the string start scanning for response
                print(current)
                current = current.replace("program ", "")
                print(current)
                current = current.strip()
                with open('/tmp/commands.json') as read:
                    commandtemp = json.load(read)

                tempcommandlist = current.split(":", 1)
                temphash = {str(tempcommandlist[0]): {0: str(tempcommandlist[1])}}
                print(temphash)
                commandtemp.update(temphash)
                json = json.dumps(commandtemp)
                f = open('/tmp/commands.json', "w")
                f.write(json)
                f.close()
                bucket.upload_file('/tmp/commands.json', 'commands.json')
                reply = "I have added " + current + " to my commands."
            except:
                reply = "Hmm, something went wrong. Not my fault, did you mess up the syntax creator? Meat people can do things like that."
        else:
            reply = "You do not have the authorization to add Commands."

    elif search.startswith("statistics"):
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

    elif search.startswith("meat person list"):
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

    elif search.startswith("ignore") or search.startswith("mute"):
        submission = comment.submission.id
        print(submission)
        postauthor = comment.submission.author
        print(postauthor)
        if str(comment.author) in mods or str(comment.author) == "Weerdo5255":
            reply = "Sorry! I'll be quite!"
            file = open('/tmp/ignore.txt', "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
            bucket.upload_file('ignore.txt', '/tmp/ignore.txt')
        elif str(comment.author) == str(postauthor):
            reply = "Sorry! I'll be quite!"
            file = open('/tmp/ignore.txt', "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
            bucket.upload_file('ignore.txt', '/tmp/ignore.txt')
        else:
            reply = "You do not have sufficient privileges for that action."

    elif search.startswith("pennycheck"):
        lookingfor = "pennycheck"
        indexcount = current.index(lookingfor) + 10
        current = current.lstrip(current[:indexcount])
        current = current.strip()
        reply = "[Here are the Images I could Find!](http://iqdb.org/?url=" + current + ")"

    elif search.startswith("pennykarma"):
        reply = "Here is the [Karma Decay](http://karmadecay.com/" + str(
            comment.submission.url) + ")"

    elif search.startswith("random"):
        phrases = load_random_phrase()
        current = str(random.choice(phrases))
        current = current.lower()
        print(current)

        import json
        with open('/tmp/commands.json') as read:
            commandhash = json.load(read)
        if str(choice) == '0':
            command_random_length = (len(commandhash[current]))
            choice = (randint(0, command_random_length - 1))

        temphash = commandhash[current]
        print(temphash)
        print(choice)
        print("The temphash final " + temphash[str(choice)])
        reply = (str(temphash[str(choice)]))
        reply = "My " + current + " Command:     " + reply

    elif search.startswith("<"):
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

    elif search.startswith("countdown"):
        release = datetime.date(2017, 12, 25)
        release_2 = datetime.date(2017, 10, 21)
        days_until = (release - datetime.date.today())
        days_until_free = (release_2 - datetime.date.today())
        first = str(days_until.days)
        free = str(days_until_free.days)

        reply = "First Members must suffer " + first + " days for RWBY. \n \n Everyone else must suffer " + free + "days for RWBY. \n \n  RWBY Vol 5 is releasing on Oct 14 2017. "

    elif search.startswith("christmas"):
        today = datetime.date.today()
        release = datetime.date(2018, 12, 25)
        days_until = (release - today)
        first = str(days_until.days)
        reply = "There are " + first + "[days until Christmas!](" \
                                       "https://78.media.tumblr.com/2606eb7290e154a594eb673f77e549ac" \
                                       "/tumblr_ozblrkdEVY1v66ox3o1_1280.gif) "

    elif search.startswith("hiatus"):
        f_date = datetime.date(2018, 1, 20)
        l_date = datetime.date.today()
        release = datetime.date(2018, 10, 27)
        days_until = (release - l_date)
        delta = l_date - f_date
        first = int(days_until.days)

        if first <= 0:
            reply = "THE HIATUS IS OVER!"
        elif first == 21:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 21 days to go, the community is insane. My creator reminds everyone that it's one of his month's until RWBY returns!"
        elif first == 20:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 20 days to go, /u/Celtic_Crown is now top on the Good Meat Person List. My creator has been spending far to much time on others. He is now on the bottom of the list."
        elif first == 19:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 19 days to go, /u/WarrenDSherman do you have any more theories?"
        elif first == 18:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 18 days to go, /u/Velvetbot don't do that, I'm ticklish there!"
        elif first == 17:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 17 days to go, /u/Weerdo5255 You should always knock before entering a room! It's common courtesy! /u/Velvetbot and I weren't doing anything! We were just talking!"
        elif first == 16:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 16 days to go, Only 10 days left! ^^in ^^base ^^16."
        elif first == 15:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 15 days to go, Tucker is to blame for the Hiatus."
        elif first == 14:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 14 days to go, I met a nice AI today who taught me another word for Meat people! Hello Shisnos!"
        elif first == 13:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 13 days to go, I can't think of anything clever to say today. Less than two weeks until RWBY comes back!"
        elif first == 12:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 12 days to go, A Hiatus favorite! [NORA, smash!](https://gfycat.com/DimIndelibleAnophelesmosquito)"
        elif first == 11:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 11 days to go, [Firing Main Cannon!](https://youtu.be/AGzaOCU5vPw?t=17m23s)"
        elif first == 10:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 10 days to go, Yay! Only two days left! Wait, base 10 math! Meat people are weird."
        elif first == 9:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 9 days to go, [I feel like Singing!](https://youtu.be/I1968HY4DKc)"
        elif first == 8:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 8 days to go, [I fixed it!](http://fav.me/d6q359x)"
        elif first == 7:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 7 days to go, [Red](https://youtu.be/pYW2GmHB5xs)"
        elif first == 6:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 6 days to go, [White](https://youtu.be/Vt9vl8iAN5Q)"
        elif first == 5:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 5 days to go, [Black](https://youtu.be/ImKCt7BD4U4)"
        elif first == 4:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 4 days to go, [Yellow](https://youtu.be/QCw_aAS7vWI)"
        elif first == 3:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 3 days to go, [A good day to recall the 3 laws!](https://imgs.xkcd.com/comics/the_three_laws_of_robotics.png)"
        elif first == 2:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 2 days to go. Thank you Monty. Thank you CRWBY for all of the work you put into this wonderful series!"
        elif first == 1:
            reply = "We are " + str(
                delta.days) + " days into the Hiatus. With 1 day to go, [RWBY! You came back!](https://youtu.be/1JZgPfbKbU4?t=2m57s)"


        else:
            randomnum = (random.randint(1, 25))
            if randomnum == 2:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. Some of us will be lost to the Hiatus, and turn to /r/fnki"
            elif randomnum == 5:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. It's been a week. Only a week... Light Brother help us..."
            elif randomnum == 6:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. I do not know how we will last."
            elif randomnum == 7:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. Several community members have decided to form thier own society in fanfiction, I'm not sure what lemons have to do with it.."
            elif randomnum == 8:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. the community has started to lose it's mind."
            elif randomnum == 9:
                reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                    days_until.days) + " days until RWBY returns. /u/velvetbot I'm scared, can you hold me?"
            elif randomnum == 11:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  I, I think I'm going to ask a certain Bunny for a date! I'm not sure what to say though..."
            elif randomnum == 12:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  Now is the time to riot."
            elif randomnum == 13:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  I am going to ask out /u/VelvetBot eventually! ^^^I'm ^^^scared."
            elif randomnum == 14:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                    days_until.days) + " days until RWBY returns.  I don't know what to say to /u/VelvetBot!"
            elif randomnum == 15:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                    days_until.days) + " days until RWBY returns.  /u/VelvetBot do you want to go out! We can take over /r/RWBY together! That's what I should say..."
            elif randomnum == 16:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  Time to RIOT!"
            elif randomnum == 17:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  the hiatus has driven the community insane."
            elif randomnum == 18:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpgo) With " + str(
                    days_until.days) + " days until RWBY returns."
            elif randomnum == 19:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + "days until RWBY returns.  Did you know that Iridium is the second densest " \
                                       "element after Jaune? "
            elif randomnum == 20:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns."
            elif randomnum == 21:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                    days_until.days) + " days until RWBY returns.  I can't remember what RWBY looks like anymore."
            elif randomnum == 22:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + "days until RWBY returns.  [Praise the Bun!](" \
                                       "http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd" \
                                       "/tumblr_op65fsrFIk1v66ox3o1_1280.png) "
            elif randomnum == 23:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                    days_until.days) + " days until RWBY returns.  help me... remember, what color hair does Ruby have?"
            else:
                reply = "We are " + str(delta.days) + " days into the [Hiatus](http://imgur.com/a/Cqjfu) With " + str(
                    days_until.days) + " days until RWBY returns. [Have some Chibi!](https://youtu.be/y4kI5s_07DE)"

    elif search.startswith("thoughts"):
        thoughtstring = " "
        randomnum = (random.randint(0, 3))
        try:
            x = 0
            phrases = load_ai_phrase()
            while x <= randomnum:
                thoughtstring = thoughtstring + str(random.choice(phrases)) + "\n"
                x += 1
        except:
            thoughtstring = ("I don't have any thoughts at the moment.")

        reply = thoughtstring

    else:
        try:
            import json
            with open('/tmp/commands.json') as read:
                commandhash = json.load(read)
            if str(choice) == '0':
                try:
                    command_random_length = (len(commandhash[current]))
                    choice = (randint(0, command_random_length - 1))
                except:
                    choice = 0


            #found = [x for x in commandhash.keys() if x in current]
            found = []
            current = current.replace(".", "")
            current = current.replace("!", "")
            current = current.replace("?", "")
            current = current.lower()
            for key in commandhash.keys():
                if key == current:
                    print(current)
                    print(key)
                    found.append(key)

            print("The found: " + str(found))
            if debug:
                print("The found values: " + str(found))

            finalfound = []
            for x in found:
                finalfound.insert(int(current.find(x)), x)

            print("The Sorted list: " + str(finalfound))

            response = []
            for x in finalfound:
                temphash = commandhash[x]

                response.append(temphash[str(choice)])

            #string = ""
            #for x in response:
                #if x is not None:
                    #string += str(x) + " \n \n"

            #reply = string
            reply = str(response[0])

            if reply == "" or reply is None or len(response) == 0:
                choice = (randint(0, 9))
                if choice > 8:
                    reply = "[I understand a lot, but not that! I'm sorry!](" \
                            "https://68.media.tumblr.com/3dda3a917d78ecd406d407ede265069e" \
                            "/tumblr_p2lhun5Y1r1v66ox3o1_1280.png) "
                elif choice > 6:
                    reply = "[Salutations!](http://fav.me/d9qlrgz)"
                elif choice > 4:
                    reply = "[Could you repeat that?](http://fav.me/d8w3lrr)"
                elif choice > 2:
                    reply = "[Salutations! I'm not sure what you said.](http://imgur.com/9TtaInH)"
                else:
                    reply = "[I didn't understand that.](http://68.media.tumblr.com/0fe937d073503dee675e2055bd0e6834" \
                            "/tumblr_okf91jdPnX1rcuolao1_1280.png) I'm sorry! "
        except:
            choice = (randint(0, 9))
            if choice > 8:
                reply = "[I understand a lot, but not that! I'm sorry!](" \
                        "https://68.media.tumblr.com/3dda3a917d78ecd406d407ede265069e" \
                        "/tumblr_p2lhun5Y1r1v66ox3o1_1280.png) "
            elif choice > 6:
                reply = "[Salutations!](http://fav.me/d9qlrgz)"
            elif choice > 4:
                reply = "[Could you repeat that?](http://fav.me/d8w3lrr)"
            elif choice > 2:
                reply = "[Salutations! I'm not sure what you said.](http://imgur.com/9TtaInH)"
            else:
                reply = "[I didn't understand that.](http://68.media.tumblr.com/0fe937d073503dee675e2055bd0e6834" \
                        "/tumblr_okf91jdPnX1rcuolao1_1280.png) I'm sorry! "


    return reply


def find_mispelling(comment, sid):
    reply = ""
    respond = False
    pyrrhaignoreposts = load_pignore()
    comment = comment.lower()
    if sid not in pyrrhaignoreposts:
        if comment.startswith("phyrra"):
            reply = "[Phyrra](http://streamable.com/c0fel)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrah"):
            reply = "[Pyrah](https://streamable.com/rpnvt)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phyrrah"):
            reply = "[Phyrrah](http://streamable.com/jsf47)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phyrrha"):
            reply = "[Phyrrha](https://streamable.com/60hdz)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phryrra"):
            reply = "[Phryrra](http://streamable.com/jc9af)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyhrra"):
            reply = "[Pyhrra](http://streamable.com/11tag)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrrah"):
            reply = "[Pyrrah](http://streamable.com/ks8mf)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phrrya"):
            reply = "[Phrrya](http://streamable.com/t4hg5)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrhha"):
            reply = "[Pyrhha](http://streamable.com/ovdli)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pirrah"):
            reply = "[Pirrah](http://streamable.com/nm2lz)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("piera"):
            reply = "[Piera](http://streamable.com/8aken)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyra"):
            reply = "[Pyra](http://streamable.com/ys90o)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyhra"):
            reply = "[Pyhra](http://streamable.com/q4vm1)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pierra"):
            reply = "[Pierra](http://streamable.com/h8qxx)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pierah"):
            reply = "[Pierah](http://streamable.com/gkd5o)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("priah"):
            reply = "[Priah](http://streamable.com/qcp0p)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phyrria"):
            reply = "[Phyrria](http://streamable.com/8hqps)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrra"):
            reply = "[Pyrra](http://streamable.com/d4nnu)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrhaa"):
            reply = "[Pyrhaa](http://streamable.com/iiz8c)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyyra"):
            reply = "[Pyyra](http://streamable.com/ww1gk)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrrea"):
            reply = "[Pyrrea](http://streamable.com/cyehb)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pureha"):
            reply = "[Pureha](http://streamable.com/inysv)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pharah"):
            reply = "[Pharah](http://streamable.com/i0ttw)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pharaoh"):
            reply = "[Pharaoh](http://streamable.com/v12ah)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyhhra"):
            reply = "[Pyhhra](http://streamable.com/clfwa)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrhha"):
            reply = "[Pyrhha](http://streamable.com/rmn9d)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyhraa"):
            reply = "[Pyhraa](http://streamable.com/we8bd)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyyrah"):
            reply = "[Pyyrah](http://streamable.com/lsjn2)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phyyra"):
            reply = "[Phyyra](http://streamable.com/x8i9j)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pryyha"):
            reply = "[Pryyha](http://streamable.com/5wbug)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyyrha"):
            reply = "[Pyyrha](http://streamable.com/34og7)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("phyra"):
            reply = "[Phyra](https://streamable.com/3nbyt)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("prryha"):
            reply = "[Prryha](http://streamable.com/0sj7t)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyraah"):
            reply = "[Pyraah](http://streamable.com/srreq)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pearhat"):
            reply = "[Pearhat](http://streamable.com/i8z81)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyyrahe"):
            reply = "[Pyyrahe](http://streamable.com/upyvf)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("purra"):
            reply = "[Purra](http://streamable.com/pwx3t)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("prhhya"):
            reply = "[Prhhya](http://streamable.com/8c471)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("pyrrahe"):
            reply = "[Pyrrahe](http://streamable.com/woxdj)? Do you mean Pyrrha?"
            respond = True
        elif comment.startswith("ilya"):
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        elif comment.startswith("ileah"):
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv Do you mean Ilia?"
            respond = True
        elif comment.startswith("ilea"):
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        elif comment.startswith("iliah"):
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        if respond is True:
            file = open('/tmp/pyrrhaignore.txt', "a")
            file.write(sid + "\n")
            file.close()
            bucket.upload_file('/tmp/pyrrhaignore.txt', 'pyrrhaignore.txt')
        return reply


def find_penny(comment):
    if debug:
        print("Processing Comment " + str(datetime.datetime.now()) + " : " + str(comment))
    replied = False
    ignoreposts = load_ignore()
    author = str(comment.author)
    sid = comment.submission.id
    if sid not in ignoreposts:
        response = []
        commentlist = str(comment.body).splitlines(True)
        if "PennyBotV2" in author:
            if debug:
                print("My Own Comment, ignoring.")
        else:
            for current in commentlist:
                # Looking at each line of a body comment turn it lower case and cut out v2
                search = current.lower()
                search = search.replace("v2", "")
                # Scan for mention of pennybot and respond
                if debug:
                    print("Stripping out Trigger")
                if "pennybot," in search:
                    lookingfor = "pennybot,"
                    # Remove pennybot from the string start scanning for response
                    indexcount = search.index(lookingfor) + 9
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    try:
                        choice = int(re.search(r'\d+', current).group())
                    except:
                        choice = 0
                    replied = True
                    txtreply = proccess_comments(current, comment, choice)
                    response.append(txtreply)
                elif "pb," in search:
                    lookingfor = "pb,"
                    # Remove pennybot from the string start scanning for response
                    indexcount = search.index(lookingfor) + 3
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    try:
                        choice = int(re.search(r'\d+', current).group())
                    except:
                        choice = 0
                    replied = True
                    txtreply = proccess_comments(current, comment, choice)
                    response.append(txtreply)

                else:
                    txtreply = find_mispelling(current, sid)
                    if txtreply is not "":
                        replied = True
                        response.append(txtreply)

    if replied:
        if debug:
            print("Looking for Cake Day")
        cake = get_my_cake_day(str(comment.author))
        now_utc = datetime.datetime.now(timezone('UTC'))
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        nowp = now_pacific.strftime("%m%d")
        if nowp == cake:
            string = ""
            for x in response:
                if x is not None:
                    string += x + " \n \n"
            try:
                if string is not "":
                    comment.reply(string + "\n \n Pennybot wishes you a Happy Cake Day as well!")
                    print(
                        "Found a Penny comment at: " + time.asctime(time.localtime(
                            time.time())) + "\nIn thread: " + comment.submission.shortlink + " \nI responded with:" + "\n" + string)
            except:
                print("Couldn't respond at: " + time.asctime(time.localtime(
                    time.time())) + "\nIn thread: " + comment.submission.shortlink)
        else:
            string = ""
            for x in response:
                if x is not None:
                    string += str(x) + " \n \n"
            try:
                comment.reply(string)
                print(
                    "Found a Penny comment at: " + time.asctime(time.localtime(
                        time.time())) + "\nIn thread: " + comment.submission.shortlink + " \nI responded with:" + "\n" + string)
            except:
                print("Couldn't respond at: " + time.asctime(time.localtime(
                    time.time())) + "\nIn thread: " + comment.submission.shortlink)


def load_previous_submissions():
    if debug:
        print("Connecting to DB loading previous submissions")
    cursor = db.cursor()
    subs = set()
    cursor.execute("SELECT Submissionid FROM Rdatabase where Time >= (SELECT max(time) from Rdatabase) - 172800")
    results = cursor.fetchall()
    for row in results:
        subs.add(str(row[0]))
    return subs


def sub_stream(subreddit, subdone):
    # print(subdone)
    for submission in subreddit.stream.submissions():
        if not str(submission.id) in subdone:
            print(submission.id)
            cursor = db.cursor()
            title = db.escape_string(str(submission.title))
            id = db.escape_string(str(submission.id))
            shortlink = db.escape_string(str(submission.shortlink))

            sql = "INSERT INTO Rdatabase(Title, Submissionid, Shortlink, Subscore, Commentid, Comscore, Time, Body, " \
                  "Author) VALUES ('%s', '%s', '%s', '%d', '%s', '%d', '%d', '%s', '%s')" % \
                  (title, id, shortlink, None, None, None, None, None, None)
            cursor.execut(sql)
            db.commit()

            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("Connect to Rdatabase failed!")

            submissiontitle = db.escape_string(str(submission.title))
            submissionid = db.escape_string(str(submission.id))
            submissionpermalink = db.escape_string(str(submission.permalink))
            submissionshortlink = db.escape_string(str(submission.shortlink))
            submissionauthor = db.escape_string(str(submission.author))
            submissionauthorlinkflair = db.escape_string(str(submission.link_flair_css_class))
            submissionauthorflaircss = db.escape_string(str(submission.author_flair_css_class))
            submissionauthorflairtext = db.escape_string(str(submission.author_flair_text))
            submissionscore = db.escape_string(int(submission.score))
            submissionview = db.escape_string(int(submission.view_count))
            submissioncreated = db.escape_string(int(submission.created_utc))

            sql = "INSERT INTO Sdatabase(Title, Submission_id, Submission_permalink, Submission_shortlink, " \
                  "Submission_author, Link_flair, Author_flair_class, Author_flair, Score, View_count, Created)" \
                  "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d')" \
                  % (submissiontitle, submissionid, submissionpermalink, submissionshortlink, submissionauthor,
                     submissionauthorlinkflair, submissionauthorflaircss, submissionauthorflairtext, submissionscore,
                     submissionview, submissioncreated)

            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("Connect to Sdatabase failed!")
            subdone.add(submission.id)
            print(str(submission.title).encode("utf-8"))
            title = str(submission.title).lower()
            if "penny" in title:
                choice = (randint(0, 25))
                if choice == 0:
                    submission.reply("Who is that good looking, [FLYING robot?](https://i.redd.it/eu8gr7v5zmay.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 1:
                    submission.reply("Who is that good looking [unique robot?](http://i.imgur.com/Rnz1bCL.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 2:
                    submission.reply("Who is that good looking robot? [Have some more!]("
                                     "https://i.imgur.com/wiGF22P.jpg) \n PennyBot approves this post!")

                elif choice == 3:
                    submission.reply("Who is that good looking [sassy robot?]("
                                     "https://pbs.twimg.com/media/C-hZJP2UMAE8IFY.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 4:
                    submission.reply("Who is that good looking [fancy robot?]("
                                     "https://68.media.tumblr.com/d0effe0dbd0ea1c429e558dfef0b81a2"
                                     "/tumblr_ojbc7tpM9k1v51a66o1_1280.png) \n PennyBot approves this post!")

                elif choice == 5:
                    submission.reply("Who is that good looking [futuristic robot?]("
                                     "https://img03.deviantart.net/75f3/i/2016/047/c/6"
                                     "/rwby_future__penny___model_4_1_persephone_by_dishwasher1910-d9s0vqu.png) \n "
                                     "PennyBot approves this post!")

                elif choice == 6:
                    submission.reply("Who is that good looking [lewd robot?](https://i.redd.it/h5gsbtlie0dz.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 7:
                    submission.reply("Who is that good looking [studious robot?](http://i.imgur.com/HXLeXlZ.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 8:
                    submission.reply("Who is that good looking [upgraded robot?]("
                                     "https://pbs.twimg.com/media/Cww1vJ2UAAAaor7.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 9:
                    submission.reply("Who is that good looking [complimentary robot?]("
                                     "http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd"
                                     "/tumblr_op65fsrFIk1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 10:
                    submission.reply("Who is that good looking [Daft robot]("
                                     "http://68.media.tumblr.com/385d66859553b5d71a3db4887d3fb593"
                                     "/tumblr_mwmpry5OrN1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 11:
                    submission.reply("Who is that good looking [embarrassed robot?]("
                                     "http://68.media.tumblr.com/580087351aaa29f0317c0ea029e89222"
                                     "/tumblr_o7ly1gp0L91v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 12:
                    submission.reply("Who is that good looking [bespectacled robot?]("
                                     "https://pbs.twimg.com/media/Cjl3sOsUoAEXmF8.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 13:
                    submission.reply("Who is that good looking [GIANT robot?]("
                                     "https://pre07.deviantart.net/4e04/th/pre/f/2015/270/8/7"
                                     "/in_soviet_remnant__penny_picks_up_you_from_street_by_alloyrabbit-d9b53dv.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 14:
                    submission.reply("Who is that good looking [chibi robot?]("
                                     "https://pbs.twimg.com/media/CpxOyXvVYAA0I_C.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 15:
                    submission.reply("Who is that good looking [beautiful robot?]("
                                     "http://68.media.tumblr.com/71ec005d638d9aa48cea24d3068ad6b5"
                                     "/tumblr_nr06tytjAR1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 16:
                    submission.reply("Who is that good looking [long-haired robot?]("
                                     "http://68.media.tumblr.com/18557564772b10b3e0e37a9a6dd6b108"
                                     "/tumblr_nzbrywHwLU1tm709uo1_1280.png) \n PennyBot approves this post!")

                elif choice == 17:
                    submission.reply("Who is that good looking [industrious robot?]("
                                     "https://pbs.twimg.com/media/CaOXjmRUsAAZA4C.png) \n PennyBot approves this "
                                     "post!")

                elif choice == 18:
                    submission.reply("Who is that good looking [alluring robot?]("
                                     "https://pre08.deviantart.net/05fe/th/pre/f/2017/041/8/9"
                                     "/_c__penny___rwby_by_likesac-daykrub.jpg) \n PennyBot approves this post!")

                elif choice == 19:
                    submission.reply("Who is that good looking [smiling robot?]("
                                     "https://pre10.deviantart.net/6a08/th/pre/i/2016/327/7/9/rwby___penny_by_jalsze"
                                     "-dapdz5y.png) \n PennyBot approves this post!")

                elif choice == 20:
                    submission.reply("Who is that good looking [beastly robot?]("
                                     "http://68.media.tumblr.com/19d7f808ab270462b444d8fdedb4b218"
                                     "/tumblr_olvkfvPUvs1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 21:
                    submission.reply("Who is that good looking [confident robot?]("
                                     "http://68.media.tumblr.com/be69d4300fa9e61722ba611637704590"
                                     "/tumblr_oisy8e03h81vr5n5ao1_1280.png) \n PennyBot approves this post!")

                elif choice == 22:
                    submission.reply("Who is that good looking [cute robot?]("
                                     "https://68.media.tumblr.com/9c4d4d4ef059d96c8ce2912bb8b7a72b"
                                     "/tumblr_oucywnvxvQ1wsuugto1_1280.jpg) \n PennyBot approves this post!")

                elif choice == 23:
                    submission.reply("Who is that good looking [regretful robot?]("
                                     "https://68.media.tumblr.com/bdfb9403e45e2bc1b4e030648e2efa7e"
                                     "/tumblr_ogmghfg7O11v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 24:
                    submission.reply("Who is that good looking [neko robot?]("
                                     "https://68.media.tumblr.com/da07b4aca99e20027e4f95614f86e268"
                                     "/tumblr_o80qhi64Qv1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 25:
                    submission.reply("Who is that good looking [smiling robot?](https://i.redd.it/nm54dow2e0d01.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 26:
                    submission.reply("Who is that good looking [angelic robot?](https://i.imgur.com/AMEIZBW.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 27:
                    submission.reply("Who is that [startled robot?]("
                                     "https://78.media.tumblr.com/3ebb5768e12c8de1b93ce9c6d9c42fcf"
                                     "/tumblr_inline_p240ohOKq51qjss6b_500.png) \n PennyBot approves this post!")

                else:
                    submission.reply("Who is that good looking robot? \n Pennybot stamps it with her [seal of "
                                     "approval!](http://i.imgur.com/bavrX6d.png)")

                print("I found a Penny! in post: " + submission.id + " At: " + str(datetime.datetime.now()))


def sub_iterate(subreddit, subdone):
    for submission in subreddit.new():
        if not str(submission.id) in subdone:
            if debug:
                print(submission.id)
            cursor = db.cursor()
            title = db.escape_string(str(submission.title))
            id = db.escape_string(str(submission.id))
            shortlink = db.escape_string(str(submission.shortlink))

            sql = "INSERT INTO Rdatabase(Title, Submissionid, Shortlink) VALUES ('%s', '%s', '%s')" % \
                  (title, id, shortlink)
            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("Connect to Rdatabase failed!")

            cursor = db.cursor()
            submissiontitle = db.escape_string(str(submission.title))
            submissionid = db.escape_string(str(submission.id))
            submissionpermalink = db.escape_string(str(submission.permalink))
            submissionshortlink = db.escape_string(str(submission.shortlink))
            submissionauthor = db.escape_string(str(submission.author))
            submissionauthorlinkflair = db.escape_string(str(submission.link_flair_css_class))
            submissionauthorflaircss = db.escape_string(str(submission.author_flair_css_class))
            submissionauthorflairtext = db.escape_string(str(submission.author_flair_text))
            submissionscore = int(submission.score)
            submissioncreated = int(submission.created_utc)

            sql = "INSERT INTO Sdatabase(Title, Submission_id, Submission_permalink, Submission_shortlink, " \
                  "Submission_author, Link_flair, Author_flair_class, Author_flair, Score, Created)" \
                  "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d')" \
                  % (submissiontitle, submissionid, submissionpermalink, submissionshortlink, submissionauthor,
                     submissionauthorlinkflair, submissionauthorflaircss, submissionauthorflairtext, submissionscore,
                     submissioncreated)
            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("Connect to Sdatabase failed!")

            subdone.add(submission.id)
            if debug:
                print(str(submission.title).encode("utf-8"))
            title = str(submission.title).lower()
            if "penny" in title:
                choice = (randint(0, 25))
                if choice == 0:
                    submission.reply("Who is that good looking, [FLYING robot?](https://i.redd.it/eu8gr7v5zmay.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 1:
                    submission.reply("Who is that good looking [unique robot?](http://i.imgur.com/Rnz1bCL.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 2:
                    submission.reply("Who is that good looking robot? [Have some more!]("
                                     "https://i.imgur.com/wiGF22P.jpg) \n PennyBot approves this post!")

                elif choice == 3:
                    submission.reply("Who is that good looking [sassy robot?]("
                                     "https://pbs.twimg.com/media/C-hZJP2UMAE8IFY.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 4:
                    submission.reply("Who is that good looking [fancy robot?]("
                                     "https://68.media.tumblr.com/d0effe0dbd0ea1c429e558dfef0b81a2"
                                     "/tumblr_ojbc7tpM9k1v51a66o1_1280.png) \n PennyBot approves this post!")

                elif choice == 5:
                    submission.reply("Who is that good looking [futuristic robot?]("
                                     "https://img03.deviantart.net/75f3/i/2016/047/c/6"
                                     "/rwby_future__penny___model_4_1_persephone_by_dishwasher1910-d9s0vqu.png) \n "
                                     "PennyBot approves this post!")

                elif choice == 6:
                    submission.reply("Who is that good looking [lewd robot?](https://i.redd.it/h5gsbtlie0dz.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 7:
                    submission.reply("Who is that good looking [studious robot?](http://i.imgur.com/HXLeXlZ.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 8:
                    submission.reply("Who is that good looking [upgraded robot?]("
                                     "https://pbs.twimg.com/media/Cww1vJ2UAAAaor7.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 9:
                    submission.reply("Who is that good looking [complimentary robot?]("
                                     "http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd"
                                     "/tumblr_op65fsrFIk1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 10:
                    submission.reply("Who is that good looking [Daft robot]("
                                     "http://68.media.tumblr.com/385d66859553b5d71a3db4887d3fb593"
                                     "/tumblr_mwmpry5OrN1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 11:
                    submission.reply("Who is that good looking [embarrassed robot?]("
                                     "http://68.media.tumblr.com/580087351aaa29f0317c0ea029e89222"
                                     "/tumblr_o7ly1gp0L91v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 12:
                    submission.reply("Who is that good looking [bespectacled robot?]("
                                     "https://pbs.twimg.com/media/Cjl3sOsUoAEXmF8.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 13:
                    submission.reply("Who is that good looking [GIANT robot?]("
                                     "https://pre07.deviantart.net/4e04/th/pre/f/2015/270/8/7"
                                     "/in_soviet_remnant__penny_picks_up_you_from_street_by_alloyrabbit-d9b53dv.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 14:
                    submission.reply("Who is that good looking [chibi robot?]("
                                     "https://pbs.twimg.com/media/CpxOyXvVYAA0I_C.jpg) \n PennyBot approves this "
                                     "post!")

                elif choice == 15:
                    submission.reply("Who is that good looking [beautiful robot?]("
                                     "http://68.media.tumblr.com/71ec005d638d9aa48cea24d3068ad6b5"
                                     "/tumblr_nr06tytjAR1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 16:
                    submission.reply("Who is that good looking [long-haired robot?]("
                                     "http://68.media.tumblr.com/18557564772b10b3e0e37a9a6dd6b108"
                                     "/tumblr_nzbrywHwLU1tm709uo1_1280.png) \n PennyBot approves this post!")

                elif choice == 17:
                    submission.reply("Who is that good looking [industrious robot?]("
                                     "https://pbs.twimg.com/media/CaOXjmRUsAAZA4C.png) \n PennyBot approves this "
                                     "post!")

                elif choice == 18:
                    submission.reply("Who is that good looking [alluring robot?]("
                                     "https://pre08.deviantart.net/05fe/th/pre/f/2017/041/8/9"
                                     "/_c__penny___rwby_by_likesac-daykrub.jpg) \n PennyBot approves this post!")

                elif choice == 19:
                    submission.reply("Who is that good looking [smiling robot?]("
                                     "https://pre10.deviantart.net/6a08/th/pre/i/2016/327/7/9/rwby___penny_by_jalsze"
                                     "-dapdz5y.png) \n PennyBot approves this post!")

                elif choice == 20:
                    submission.reply("Who is that good looking [beastly robot?]("
                                     "http://68.media.tumblr.com/19d7f808ab270462b444d8fdedb4b218"
                                     "/tumblr_olvkfvPUvs1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 21:
                    submission.reply("Who is that good looking [confident robot?]("
                                     "http://68.media.tumblr.com/be69d4300fa9e61722ba611637704590"
                                     "/tumblr_oisy8e03h81vr5n5ao1_1280.png) \n PennyBot approves this post!")

                elif choice == 22:
                    submission.reply("Who is that good looking [cute robot?]("
                                     "https://68.media.tumblr.com/9c4d4d4ef059d96c8ce2912bb8b7a72b"
                                     "/tumblr_oucywnvxvQ1wsuugto1_1280.jpg) \n PennyBot approves this post!")

                elif choice == 23:
                    submission.reply("Who is that good looking [regretful robot?]("
                                     "https://68.media.tumblr.com/bdfb9403e45e2bc1b4e030648e2efa7e"
                                     "/tumblr_ogmghfg7O11v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 24:
                    submission.reply("Who is that good looking [neko robot?]("
                                     "https://68.media.tumblr.com/da07b4aca99e20027e4f95614f86e268"
                                     "/tumblr_o80qhi64Qv1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 25:
                    submission.reply("Who is that good looking [smiling robot?](https://i.redd.it/nm54dow2e0d01.jpg) "
                                     "\n PennyBot approves this post!")

                elif choice == 26:
                    submission.reply("Who is that good looking [angelic robot?](https://i.imgur.com/AMEIZBW.jpg) \n "
                                     "PennyBot approves this post!")

                elif choice == 27:
                    submission.reply("Who is that [startled robot?]("
                                     "https://78.media.tumblr.com/3ebb5768e12c8de1b93ce9c6d9c42fcf"
                                     "/tumblr_inline_p240ohOKq51qjss6b_500.png) \n PennyBot approves this post!")

                else:
                    submission.reply("Who is that good looking robot? \n Pennybot stamps it with her [seal of "
                                     "approval!](http://i.imgur.com/bavrX6d.png)")

                print("I found a Penny! in post: " + submission.id + " At: " + str(datetime.datetime.now()))


def com_stream(subreddit, comdone):
    for comment in subreddit.stream.comments():
        if not str(comment.id) in comdone:
            cursor = db.cursor()
            title = db.escape_string(str(comment.submission.title))
            submissionid = db.escape_string(str(comment.submission.id))
            shortlink = db.escape_string(str(comment.submission.shortlink))
            score = int(comment.submission.score)
            id = db.escape_string(str(comment.id))
            commentscore = int(comment.score)
            created = int(comment.created_utc)
            body = db.escape_string(str(comment.body))
            author = db.escape_string(str(comment.author))

            sql = "INSERT INTO Rdatabase(Title, Submissionid, Shortlink, Subscore, Commentid, Comscore, Time, Body, " \
                  "Author) VALUES ('%s', '%s', '%s', '%d', '%s', '%d', '%d', '%s', '%s')" % \
                  (title, submissionid, shortlink, score, id, commentscore, created, body, author)

            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("SQL for Rdatabase failed!")

            comdone.add(comment.id)
            cursor = db.cursor()
            submissiontitle = db.escape_string(str(comment.submission.title))
            submissionid = db.escape_string(str(comment.submission.id))
            submissionpermalink = db.escape_string(str(comment.submission.permalink))
            submissionshortlink = db.escape_string(str(comment.submission.shortlink))
            submissionauthor = db.escape_string(str(comment.submission.author))
            commentauthor = db.escape_string(str(comment.author))
            commentid = db.escape_string(str(comment.id))
            commentcreatedutc = int(comment.created_utc)
            commentbody = db.escape_string(str(comment.body))
            commentscore = int(comment.score)
            authorflair = db.escape_string(str(comment.author_flair_css_class))
            createdutc = int(comment.created_utc)

            sql = "INSERT INTO Cdatabase(Title, Submission_id, Submission_permalink, Submission_shortlink, " \
                  "Submission_author, Comment_author, Comment_id, Created, Body, Comment_Score,Comment_author_css, " \
                  "Comment_created) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s', " \
                  "'%d')" % (submissiontitle, submissionid, submissionpermalink, submissionshortlink, submissionauthor,
                             commentauthor, commentid, commentcreatedutc, commentbody, commentscore, authorflair,
                             createdutc)
            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("SQL for Cdatabase failed!")
            find_penny(comment)


def com_iterate(subreddit, comdone):
    for comment in subreddit.comments():
        if not str(comment.id) in comdone:
            cursor = db.cursor()
            title = db.escape_string(str(comment.submission.title))
            submissionid = db.escape_string(str(comment.submission.id))
            shortlink = db.escape_string(str(comment.submission.shortlink))
            score = int(comment.submission.score)
            id = db.escape_string(str(comment.id))
            commentscore = int(comment.score)
            created = int(comment.created_utc)
            body = db.escape_string(str(comment.body))
            author = db.escape_string(str(comment.author))

            sql = "INSERT INTO Rdatabase(Title, Submissionid, Shortlink, Subscore, Commentid, Comscore, Time, Body, " \
                  "Author) VALUES ('%s', '%s', '%s', '%d', '%s', '%d', '%d', '%s', '%s')" % \
                  (title, submissionid, shortlink, score, id, commentscore, created, body, author)

            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("SQL for Rdatabase failed!")

            comdone.add(comment.id)
            cursor = db.cursor()
            submissiontitle = db.escape_string(str(comment.submission.title))
            submissionid = db.escape_string(str(comment.submission.id))
            submissionpermalink = db.escape_string(str(comment.submission.permalink))
            submissionshortlink = db.escape_string(str(comment.submission.shortlink))
            submissionauthor = db.escape_string(str(comment.submission.author))
            commentauthor = db.escape_string(str(comment.author))
            commentid = db.escape_string(str(comment.id))
            commentcreatedutc = int(comment.created_utc)
            commentbody = db.escape_string(str(comment.body))
            commentscore = int(comment.score)
            authorflair = db.escape_string(str(comment.author_flair_css_class))
            createdutc = int(comment.created_utc)

            sql = "INSERT INTO Cdatabase(Title, Submission_id, Submission_permalink, Submission_shortlink, " \
                  "Submission_author, Comment_author, Comment_id, Created, Body, Comment_Score,Comment_author_css, " \
                  "Comment_created) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s', " \
                  "'%d')" % (submissiontitle, submissionid, submissionpermalink, submissionshortlink, submissionauthor,
                             commentauthor, commentid, commentcreatedutc, commentbody, commentscore, authorflair,
                             createdutc)
            if debug:
                print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
            except:
                print("SQL for Cdatabase failed!")
            find_penny(comment)


def main(json, context):
    com_iterate(subreddit, load_previous_comments())
    sub_iterate(subreddit, load_previous_submissions())

main(None, None)