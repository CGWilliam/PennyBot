import csv
import datetime
import random

import private_credentials

s3 = private_credentials.amazon_login()
r = private_credentials.reddit_login()


def shipping_wars(instring):
    def ship_search(name1, name2):
        response = "I have no data on " + name1 + " X " + name2 + ". [You could fill in the shipsheet?](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"
        s3.Bucket('pennybotv2resources').download_file('Main.csv', '/tmp/Main.csv')
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
            s3.Bucket('pennybotv2resources').download_file('OT3.csv', '/tmp/OT3.csv')
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

    try:
        index1 = instring.index(' ')
        index2 = instring.index(' ', index1 + 1)
        index3 = instring.index(' ', index2 + 1)
        index4 = instring.index('>')
        name1 = instring[1:index1]
        name2 = instring[index2 + 1:index3]
        name3 = instring[index3 + 3:index4]
        reply = ot3_search(name1.title(), name2.title(), name3.title())
    except:
        index1 = instring.index(' ')
        index2 = instring.index(' ', index1 + 1)
        index4 = instring.index('>')
        name1 = instring[1:index1]
        name2 = instring[index2 + 1:index4]
        reply = ship_search(name1.title(), name2.title())

    return reply


def pyrrhascan(comment):
    global reply
    s3.Bucket('pennybotv2resources').download_file('pyrrhaignore.txt', '/tmp/pyrrhaignore.txt')
    with open('/tmp/pyrrhaignore.txt', 'r') as f:
        pyrrhaignoreposts = [line.strip() for line in f]
    respond = False
    if comment.submission.id not in pyrrhaignoreposts:
        comment = str(comment.body.lower())
        if "phyrra" in comment:
            reply = "[Phyrra](http://streamable.com/c0fel)? Do you mean Pyrrha?"
            respond = True
        elif "pyrah" in comment:
            reply = "[Pyrah](https://streamable.com/rpnvt)? Do you mean Pyrrha?"
            respond = True
        elif "phyrrah" in comment:
            reply = "[Phyrrah](http://streamable.com/jsf47)? Do you mean Pyrrha?"
            respond = True
        elif "phyrrha" in comment:
            reply = "[Phyrrha](https://streamable.com/60hdz)? Do you mean Pyrrha?"
            respond = True
        elif "phryrra" in comment:
            reply = "[Phryrra](http://streamable.com/jc9af)? Do you mean Pyrrha?"
            respond = True
        elif "pyhrra" in comment:
            reply = "[Pyhrra](http://streamable.com/11tag)? Do you mean Pyrrha?"
            respond = True
        elif "pyrrah" in comment:
            reply = "[Pyrrah](http://streamable.com/ks8mf)? Do you mean Pyrrha?"
            respond = True
        elif "phrrya" in comment:
            reply = "[Phrrya](http://streamable.com/t4hg5)? Do you mean Pyrrha?"
            respond = True
        elif "pyrhha" in comment:
            reply = "[Pyrhha](http://streamable.com/ovdli)? Do you mean Pyrrha?"
            respond = True
        elif "pirrah" in comment:
            reply = "[Pirrah](http://streamable.com/nm2lz)? Do you mean Pyrrha?"
            respond = True
        elif "piera" in comment:
            reply = "[Piera](http://streamable.com/8aken)? Do you mean Pyrrha?"
            respond = True
        elif "pyra" in comment:
            reply = "[Pyra](http://streamable.com/ys90o)? Do you mean Pyrrha?"
            respond = True
        elif "pyhra" in comment:
            reply = "[Pyhra](http://streamable.com/q4vm1)? Do you mean Pyrrha?"
            respond = True
        elif "pierra" in comment:
            reply = "[Pierra](http://streamable.com/h8qxx)? Do you mean Pyrrha?"
            respond = True
        elif "pierah" in comment:
            reply = "[Pierah](http://streamable.com/gkd5o)? Do you mean Pyrrha?"
            respond = True
        elif "priah" in comment:
            reply = "[Priah](http://streamable.com/qcp0p)? Do you mean Pyrrha?"
            respond = True
        elif "phyrria" in comment:
            reply = "[Phyrria](http://streamable.com/8hqps)? Do you mean Pyrrha?"
            respond = True
        elif "pyrra" in comment:
            reply = "[Pyrra](http://streamable.com/d4nnu)? Do you mean Pyrrha?"
            respond = True
        elif "pyrhaa" in comment:
            reply = "[Pyrhaa](http://streamable.com/iiz8c)? Do you mean Pyrrha?"
            respond = True
        elif "pyyra" in comment:
            reply = "[Pyyra](http://streamable.com/ww1gk)? Do you mean Pyrrha?"
            respond = True
        elif "pyrrea" in comment:
            reply = "[Pyrrea](http://streamable.com/cyehb)? Do you mean Pyrrha?"
            respond = True
        elif "pureha" in comment:
            reply = "[Pureha](http://streamable.com/inysv)? Do you mean Pyrrha?"
            respond = True
        elif "pharah" in comment:
            reply = "[Pharah](http://streamable.com/i0ttw)? Do you mean Pyrrha?"
            respond = True
        elif "pharaoh" in comment:
            reply = "[Pharaoh](http://streamable.com/v12ah)? Do you mean Pyrrha?"
            respond = True
        elif "pyhhra" in comment:
            reply = "[Pyhhra](http://streamable.com/clfwa)? Do you mean Pyrrha?"
            respond = True
        elif "pyrhha" in comment:
            reply = "[Pyrhha](http://streamable.com/rmn9d)? Do you mean Pyrrha?"
            respond = True
        elif "pyhraa" in comment:
            reply = "[Pyhraa](http://streamable.com/we8bd)? Do you mean Pyrrha?"
            respond = True
        elif "pyyrah" in comment:
            reply = "[Pyyrah](http://streamable.com/lsjn2)? Do you mean Pyrrha?"
            respond = True
        elif "phyyra" in comment:
            reply = "[Phyyra](http://streamable.com/x8i9j)? Do you mean Pyrrha?"
            respond = True
        elif "pryyha" in comment:
            reply = "[Pryyha](http://streamable.com/5wbug)? Do you mean Pyrrha?"
            respond = True
        elif "pyyrha" in comment:
            reply = "[Pyyrha](http://streamable.com/34og7)? Do you mean Pyrrha?"
            respond = True
        elif "phyra" in comment:
            reply = "[Phyra](https://streamable.com/3nbyt)? Do you mean Pyrrha?"
            respond = True
        elif "prryha" in comment:
            reply = "[Prryha](http://streamable.com/0sj7t)? Do you mean Pyrrha?"
            respond = True
        elif "pyraah" in comment:
            reply = "[Pyraah](http://streamable.com/srreq)? Do you mean Pyrrha?"
            respond = True
        elif "pearhat" in comment:
            reply = "[Pearhat](http://streamable.com/i8z81)? Do you mean Pyrrha?"
            respond = True
        elif "pyyrahe" in comment:
            reply = "[Pyyrahe](http://streamable.com/upyvf)? Do you mean Pyrrha?"
            respond = True
        elif "purra" in comment:
            reply = "[Purra](http://streamable.com/pwx3t)? Do you mean Pyrrha?"
            respond = True
        elif "prhhya" in comment:
            reply = "[Prhhya](http://streamable.com/8c471)? Do you mean Pyrrha?"
            respond = True
        elif "pyrrahe" in comment:
            reply = "[Pyrrahe](http://streamable.com/woxdj)? Do you mean Pyrrha?"
            respond = True
        elif "ilya" in comment:
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        elif "ileah" in comment:
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv Do you mean Ilia?"
            respond = True
        elif "ilea" in comment:
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        elif "iliah" in comment:
            reply = "[What, oh.](https://i.imgur.com/dWoj8oX.gifv) Do you mean Ilia?"
            respond = True
        if respond is True:
            file = open('/tmp/pyrrhaignore.txt', "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
            s3.Bucket('pennybotv2resources').upload_file('/tmp/pyrrhaignore.txt', 'pyrrhaignore.txt')
        return reply


def exact_hiatus():
    f_date = datetime.datetime(2019, 1, 26, 16, 0, 0, 0)
    delta = (datetime.datetime.now() - f_date)
    delta_day = delta.days
    delta_hour = delta.seconds // 3600
    delta_min = (delta.seconds // 60) % 60
    delta_sec = (delta.seconds % 60)

    delta_print = str(delta_day) + ' days ' + str(delta_hour) + ' hours ' + str(
        delta_min) + ' minutes ' \
                     'and ' + \
                  str(delta_sec) + ' seconds '

    days_until = "an unknown number of"
    randomnum = (random.randint(1, 25))
    if randomnum == 2:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. Some of us will be lost to the Hiatus, and turn to /r/fnki"
    elif randomnum == 5:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. It's been a week. Only a week... Light Brother help us..."
    elif randomnum == 6:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. I do not know how we will last."
    elif randomnum == 7:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. Several community members have decided to form thier own society in fanfiction, I'm not sure what lemons have to do with it.."
    elif randomnum == 8:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. the community has started to lose it's mind."
    elif randomnum == 9:
        reply = "We are " + delta_print + " into the Hiatus. With " + days_until + " days until RWBY returns. /u/velvetbot I'm scared, can you hold me?"
    elif randomnum == 11:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  I, I think I'm going to ask a certain Bunny for a date! I'm not sure what to say though..."
    elif randomnum == 12:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  Now is the time to riot."
    elif randomnum == 13:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  I am going to ask out /u/VelvetBot eventually! ^^^I'm ^^^scared."
    elif randomnum == 14:
        reply = "We are " + delta_print + " into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + days_until + " days until RWBY returns.  I don't know what to say to /u/VelvetBot!"
    elif randomnum == 15:
        reply = "We are " + delta_print + " into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + days_until + " days until RWBY returns.  /u/VelvetBot do you want to go out! We can take over /r/RWBY together! That's what I should say..."
    elif randomnum == 16:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  Time to RIOT!"
    elif randomnum == 17:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  the hiatus has driven the community insane."
    elif randomnum == 18:
        reply = "We are " + delta_print + " into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpgo) With " + days_until + " days until RWBY returns."
    elif randomnum == 19:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + "days until RWBY returns.  Did you know that Iridium is the second densest element after Jaune? "
    elif randomnum == 20:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns."
    elif randomnum == 21:
        reply = "We are " + delta_print + " into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + days_until + " days until RWBY returns.  I can't remember what RWBY looks like anymore."
    elif randomnum == 22:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + "days until RWBY returns. [Praise the Bun!](http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd/tumblr_op65fsrFIk1v66ox3o1_1280.png)"
    elif randomnum == 23:
        reply = "We are " + delta_print + " into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + days_until + " days until RWBY returns.  help me... remember, what color hair does Ruby have?"
    else:
        reply = "We are " + delta_print + " into the [Hiatus](http://imgur.com/a/Cqjfu) With " + days_until + " days until RWBY returns. [Have some Chibi!](https://youtu.be/y4kI5s_07DE)"

    return reply


def hiatus():
    f_date = datetime.date(2019, 1, 26)
    l_date = datetime.date.today()
    release = datetime.date(2018, 10, 27)
    # days_until = (release - l_date)
    days_until = 65536
    delta = l_date - f_date
    first = int(days_until)

    if first <= 0:
        reply = "THE HIATUS IS OVER!"
    # elif first == 21:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 21 days to go, the community is insane. My creator reminds everyone that it's one of his month's until RWBY returns!"
    # elif first == 20:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 20 days to go, /u/Celtic_Crown is now top on the Good Meat Person List. My creator has been spending far to much time on others. He is now on the bottom of the list."
    # elif first == 19:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 19 days to go, /u/WarrenDSherman do you have any more theories?"
    # elif first == 18:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 18 days to go, /u/Velvetbot don't do that, I'm ticklish there!"
    # elif first == 17:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 17 days to go, /u/Weerdo5255 You should always knock before entering a room! It's common courtesy! /u/Velvetbot and I weren't doing anything! We were just talking!"
    # elif first == 16:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 16 days to go, Only 10 days left! ^^in ^^base ^^16."
    # elif first == 15:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 15 days to go, Tucker is to blame for the Hiatus."
    # elif first == 14:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 14 days to go, I met a nice AI today who taught me another word for Meat people! Hello Shisnos!"
    # elif first == 13:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 13 days to go, I can't think of anything clever to say today. Less than two weeks until RWBY comes back!"
    # elif first == 12:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 12 days to go, A Hiatus favorite! [NORA, smash!](https://gfycat.com/DimIndelibleAnophelesmosquito)"
    # elif first == 11:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 11 days to go, [Firing Main Cannon!](https://youtu.be/AGzaOCU5vPw?t=17m23s)"
    # elif first == 10:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 10 days to go, Yay! Only two days left! Wait, base 10 math! Meat people are weird."
    # elif first == 9:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 9 days to go, [I feel like Singing!](https://youtu.be/I1968HY4DKc)"
    # elif first == 8:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 8 days to go, [I fixed it!](http://fav.me/d6q359x)"
    # elif first == 7:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 7 days to go, [Red](https://youtu.be/pYW2GmHB5xs)"
    # elif first == 6:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 6 days to go, [White](https://youtu.be/Vt9vl8iAN5Q)"
    # elif first == 5:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 5 days to go, [Black](https://youtu.be/ImKCt7BD4U4)"
    # elif first == 4:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 4 days to go, [Yellow](https://youtu.be/QCw_aAS7vWI)"
    # elif first == 3:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 3 days to go, [A good day to recall the 3 laws!](https://imgs.xkcd.com/comics/the_three_laws_of_robotics.png)"
    # elif first == 2:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 2 days to go. Thank you Monty. Thank you CRWBY for all of the work you put into this wonderful series!"
    # elif first == 1:
    #     reply = "We are " + str(
    #         delta.days) + " days into the Hiatus. With 1 day to go, [RWBY! You came back!](https://youtu.be/1JZgPfbKbU4?t=2m57s)"

    else:
        days_until = "an unknown number of"
        randomnum = (random.randint(1, 25))
        if randomnum == 2:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. Some of us will be lost to the Hiatus, and turn to /r/fnki"
        elif randomnum == 5:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. It's been a week. Only a week... Light Brother help us..."
        elif randomnum == 6:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. I do not know how we will last."
        elif randomnum == 7:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. Several community members have decided to form thier own society in fanfiction, I'm not sure what lemons have to do with it.."
        elif randomnum == 8:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. the community has started to lose it's mind."
        elif randomnum == 9:
            reply = "We are " + str(delta.days) + " days into the Hiatus. With " + str(
                days_until) + " days until RWBY returns. /u/velvetbot I'm scared, can you hold me?"
        elif randomnum == 11:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  I, I think I'm going to ask a certain Bunny for a date! I'm not sure what to say though..."
        elif randomnum == 12:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  Now is the time to riot."
        elif randomnum == 13:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  I am going to ask out /u/VelvetBot eventually! ^^^I'm ^^^scared."
        elif randomnum == 14:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                days_until) + " days until RWBY returns.  I don't know what to say to /u/VelvetBot!"
        elif randomnum == 15:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                days_until) + " days until RWBY returns.  /u/VelvetBot do you want to go out! We can take over /r/RWBY together! That's what I should say..."
        elif randomnum == 16:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  Time to RIOT!"
        elif randomnum == 17:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  the hiatus has driven the community insane."
        elif randomnum == 18:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpgo) With " + str(
                days_until) + " days until RWBY returns."
        elif randomnum == 19:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + "days until RWBY returns.  Did you know that Iridium is the second densest " \
                              "element after Jaune? "
        elif randomnum == 20:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns."
        elif randomnum == 21:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) With " + str(
                days_until) + " days until RWBY returns.  I can't remember what RWBY looks like anymore."
        elif randomnum == 22:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + "days until RWBY returns.  [Praise the Bun!](" \
                              "http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd" \
                              "/tumblr_op65fsrFIk1v66ox3o1_1280.png) "
        elif randomnum == 23:
            reply = "We are " + str(
                delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) With " + str(
                days_until) + " days until RWBY returns.  help me... remember, what color hair does Ruby have?"
        else:
            reply = "We are " + str(delta.days) + " days into the [Hiatus](http://imgur.com/a/Cqjfu) With " + str(
                days_until) + " days until RWBY returns. [Have some Chibi!](https://youtu.be/y4kI5s_07DE)"

        return reply


def complex_commands(r, reply_string, comment, log, maintainer, complete_dict):
    print(reply_string)
    reply_string = (reply_string[2:])
    print(reply_string)
    import json

    if reply_string.startswith("program"):
        log.debug("Someone is attempting to program a new command.")
        if comment.author == "Weerdo5255":
            try:
                # Remove pennybot from the string start scanning for response
                current = comment.replace("program ", "")
                current = current.strip()
                with open('/tmp/commands.json') as read:
                    commandtemp = json.load(read)

                tempcommandlist = current.split(":", 1)
                temphash = {str(tempcommandlist[0]): {0: str(tempcommandlist[1])}}
                commandtemp.update(temphash)
                json = json.dumps(commandtemp)
                f = open('/tmp/commands.json', "w")
                f.write(json)
                f.close()
                s3.Bucket('pennybotv2resources').upload_file('/tmp/commands.json', 'commands.json')
                reply = "I have added " + current + " to my commands."
            except:
                reply = "Hmm, something went wrong. Not my fault, did you mess up the syntax creator? Meat people can " \
                        "do things like that. "
        else:
            reply = "You do not have the authorization to add Commands."

    elif reply_string.startswith("suggestion"):
        reply = "[You can make Suggestions here!](" \
                "https://docs.google.com/forms/d/e/1FAIpQLScp8yibCZRKqNcvvUT69VfEs2inp4DvNFvakGWubIAyv8D4EA/viewform" \
                "?usp=sf_link) ^^^^^^^^/u/weerdo5255 "

    elif reply_string.startswith("thoughts"):
        thoughtstring = " "
        randomnum = (random.randint(0, 3))
        try:
            x = 0
            s3.Bucket('pennybotv2resources').download_file('thoughts.txt', '/tmp/thoughts.txt')
            with open('/tmp/thoughts.txt', 'r', encoding='utf8') as f:
                phrases = [line.strip() for line in f]
            while x <= randomnum:
                thoughtstring = thoughtstring + random.choice(phrases) + "\n"
                x += 1
        except:
            thoughtstring = "I don't have any thoughts at the moment."
        reply = thoughtstring

    elif reply_string.startswith("ignore") or reply_string.startswith("mute"):
        mods = []
        for moderator in r.subreddit(comment.subreddit).moderator():
            mods.append(str(moderator))
        if str(comment.author) in mods or str(comment.author) == maintainer:
            reply = "Sorry! I'll be quite!"
            file = open('/tmp/ignore.txt', "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
            s3.Bucket('pennybotv2resources').upload_file('ignore.txt', '/tmp/ignore.txt')
        elif str(comment.author) == str(comment.submission.author):
            reply = "Sorry! I'll be quite!"
            file = open('/tmp/ignore.txt', "a")
            file.write(str(comment.submission.id) + "\n")
            file.close()
            s3.Bucket('pennybotv2resources').upload_file('ignore.txt', '/tmp/ignore.txt')
        else:
            reply = "You do not have sufficient privileges for that action."

    elif reply_string.startswith("random"):
        key_list = list(complete_dict.keys())
        current = str(random.choice(key_list))
        temp_dict = complete_dict.get(current)
        reply = temp_dict.get("0")
        reply = "My " + current + " Command: " + reply

    elif reply_string.startswith("<"):
        reply = shipping_wars(reply_string)

    elif reply_string.startswith("hiatus!") or reply_string.startswith("exact hiatus") or reply_string.startswith(
            "precise hiatus"):
        reply = exact_hiatus(reply_string)

    elif reply_string.startswith("hiatus"):
        reply = hiatus()

    elif reply_string.startswith("thoughts"):
        s3.Bucket('pennybotv2resources').download_file('thoughts.txt', '/tmp/thoughts.txt')
        with open('/tmp/thoughts.txt', 'r', encoding='utf8') as f:
            aiphrase = [line.strip() for line in f]
        thoughtstring = " "
        randomnum = (random.randint(0, 3))
        try:
            x = 0
            phrases = aiphrase()
            while x <= randomnum:
                thoughtstring = thoughtstring + str(random.choice(phrases)) + "\n"
                x += 1
        except:
            thoughtstring = ("I don't have any thoughts at the moment.")
        reply = thoughtstring

    return reply
