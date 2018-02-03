
import obot
import sqlite3
import time
from datetime import datetime
from random import randint
import random


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
            db = sqlite3.connect("Sdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Sdatabase VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (str(submission.title), str(submission.id), str(submission.permalink),
                            str(submission.shortlink), str(submission.author), str(submission.link_flair_css_class),
                            str(submission.author_flair_css_class), str(submission.author_flair_text), submission.score,
                            submission.view_count, int(submission.created_utc)))
            db.commit()
            subdone.add(submission.id)
            print(str(submission.title).encode("utf-8"))
            title = str(submission.title).lower()
            if "penny" in title:
                choice = (randint(0, 25))
                if choice == 0:
                    submission.reply("Who is that good looking, [FLYING robot?](https://i.redd.it/eu8gr7v5zmay.jpg) \n PennyBot approves this post!")

                elif choice == 1:
                    submission.reply("Who is that good looking [unique robot?](http://i.imgur.com/Rnz1bCL.jpg) \n PennyBot approves this post!")

                elif choice == 2:
                    submission.reply("Who is that good looking robot? [Have some more!](https://i.imgur.com/wiGF22P.jpg) \n PennyBot approves this post!")

                elif choice == 3:
                    submission.reply("Who is that good looking [sassy robot?](https://pbs.twimg.com/media/C-hZJP2UMAE8IFY.jpg) \n PennyBot approves this post!")

                elif choice == 4:
                    submission.reply("Who is that good looking [fancy robot?](https://68.media.tumblr.com/d0effe0dbd0ea1c429e558dfef0b81a2/tumblr_ojbc7tpM9k1v51a66o1_1280.png) \n PennyBot approves this post!")

                elif choice == 5:
                    submission.reply("Who is that good looking [futuristic robot?](https://img03.deviantart.net/75f3/i/2016/047/c/6/rwby_future__penny___model_4_1_persephone_by_dishwasher1910-d9s0vqu.png) \n PennyBot approves this post!")

                elif choice == 6:
                    submission.reply("Who is that good looking [lewd robot?](https://i.redd.it/h5gsbtlie0dz.jpg) \n PennyBot approves this post!")

                elif choice == 7:
                    submission.reply("Who is that good looking [studious robot?](http://i.imgur.com/HXLeXlZ.jpg) \n PennyBot approves this post!")

                elif choice == 8:
                    submission.reply("Who is that good looking [upgraded robot?](https://pbs.twimg.com/media/Cww1vJ2UAAAaor7.jpg) \n PennyBot approves this post!")

                elif choice == 9:
                    submission.reply("Who is that good looking [complimentary robot?](http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd/tumblr_op65fsrFIk1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 10:
                    submission.reply("Who is that good looking [Daft robot](http://68.media.tumblr.com/385d66859553b5d71a3db4887d3fb593/tumblr_mwmpry5OrN1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 11:
                    submission.reply("Who is that good looking [embarrassed robot?](http://68.media.tumblr.com/580087351aaa29f0317c0ea029e89222/tumblr_o7ly1gp0L91v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 12:
                    submission.reply("Who is that good looking [bespectacled robot?](https://pbs.twimg.com/media/Cjl3sOsUoAEXmF8.jpg) \n PennyBot approves this post!")

                elif choice == 13:
                    submission.reply("Who is that good looking [GIANT robot?](https://pre07.deviantart.net/4e04/th/pre/f/2015/270/8/7/in_soviet_remnant__penny_picks_up_you_from_street_by_alloyrabbit-d9b53dv.jpg) \n PennyBot approves this post!")

                elif choice == 14:
                    submission.reply("Who is that good looking [chibi robot?](https://pbs.twimg.com/media/CpxOyXvVYAA0I_C.jpg) \n PennyBot approves this post!")

                elif choice == 15:
                    submission.reply("Who is that good looking [beautiful robot?](http://68.media.tumblr.com/71ec005d638d9aa48cea24d3068ad6b5/tumblr_nr06tytjAR1qgc33ho1_1280.png) \n PennyBot approves this post!")

                elif choice == 16:
                    submission.reply("Who is that good looking [long-haired robot?](http://68.media.tumblr.com/18557564772b10b3e0e37a9a6dd6b108/tumblr_nzbrywHwLU1tm709uo1_1280.png) \n PennyBot approves this post!")

                elif choice == 17:
                    submission.reply("Who is that good looking [industrious robot?](https://pbs.twimg.com/media/CaOXjmRUsAAZA4C.png) \n PennyBot approves this post!")

                elif choice == 18:
                    submission.reply("Who is that good looking [alluring robot?](https://pre08.deviantart.net/05fe/th/pre/f/2017/041/8/9/_c__penny___rwby_by_likesac-daykrub.jpg) \n PennyBot approves this post!")

                elif choice == 19:
                    submission.reply("Who is that good looking [smiling robot?](https://pre10.deviantart.net/6a08/th/pre/i/2016/327/7/9/rwby___penny_by_jalsze-dapdz5y.png) \n PennyBot approves this post!")

                elif choice == 20:
                    submission.reply("Who is that good looking [beastly robot?](http://68.media.tumblr.com/19d7f808ab270462b444d8fdedb4b218/tumblr_olvkfvPUvs1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 21:
                    submission.reply("Who is that good looking [confident robot?](http://68.media.tumblr.com/be69d4300fa9e61722ba611637704590/tumblr_oisy8e03h81vr5n5ao1_1280.png) \n PennyBot approves this post!")

                elif choice == 22:
                    submission.reply("Who is that good looking [cute robot?](https://68.media.tumblr.com/9c4d4d4ef059d96c8ce2912bb8b7a72b/tumblr_oucywnvxvQ1wsuugto1_1280.jpg) \n PennyBot approves this post!")

                elif choice == 23:
                    submission.reply("Who is that good looking [regretful robot?](https://68.media.tumblr.com/bdfb9403e45e2bc1b4e030648e2efa7e/tumblr_ogmghfg7O11v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 24:
                    submission.reply("Who is that good looking [neko robot?](https://68.media.tumblr.com/da07b4aca99e20027e4f95614f86e268/tumblr_o80qhi64Qv1v66ox3o1_1280.png) \n PennyBot approves this post!")

                elif choice == 25:
                    submission.reply("Who is that good looking [smiling robot?](https://i.redd.it/nm54dow2e0d01.jpg) \n PennyBot approves this post!")

                elif choice == 26:
                    submission.reply("Who is that good looking [angelic robot?](https://i.imgur.com/AMEIZBW.jpg) \n PennyBot approves this post!")

                elif choice == 27:
                    submission.reply("Who is that [startled robot?](https://78.media.tumblr.com/3ebb5768e12c8de1b93ce9c6d9c42fcf/tumblr_inline_p240ohOKq51qjss6b_500.png) \n PennyBot approves this post!")

                else:
                    submission.reply("Who is that good looking robot? \n Pennybot stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)")

                print("I found a Penny! in post: " + submission.id + " At: " + str(datetime.now()))


while True:
    try:
        mods = []
        r = obot.login()
        subredditlist = ['fnki','rwby']
        for sub in subredditlist:
            for moderator in r.subreddit(sub).moderator():
                mods.append(str(moderator))
        subjoin = "+"
        subreddit = r.subreddit(subjoin.join(subredditlist))
        print("The " + str(subreddit) + " Moderators: " + str(mods))
        sub_stream(subreddit, load_previous_submissions())
    except Exception as e:
        print(e)
        print("Waiting 20 seconds to restart")
        time.sleep(20)
        pass
