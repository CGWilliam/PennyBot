

__author__ = 'C.G.William / Weerdo5255' \

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'

from random import randint
import praw
import obot
import time
import sqlite3
import datetime
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

        else:
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
    replied = False
    reply = ''
    # Don't care about where the comments are so flatten the comment tree
    for comment in flat_comments:
        # Divide the body of all of the comments so we can scan each line correctly

        if comment.id in processing:
            wholecomment = comment.body
            list = wholecomment.splitlines(True)

            for current in list:
                # Looking at each line of a body comment turn it lower case and cut out v2
                current = current.lower()
                current = current.replace("v2", "")

                # Scan for mention of pennybot and respond
                if "pennybot," in current:

                    # The random choice determination
                    choice = (randint(0,9))
                    print("Found a comment at: " + time.asctime(time.localtime(time.time())))
                    lookingfor = "pennybot,"

                    # Remove pennybot from the string start scanning for response
                    indexcount = current.index(lookingfor) + 9
                    current = current.lstrip(current[:indexcount])
                    current = current.strip()
                    replied = True


                    counter = 0
                    finalresponse = []
                    totalcomment = comment.body
                    commentauthor = comment.author

                    #Other commands

                    if current.startswith("test"):
                        reply = "I'm working!"

                    if current.startswith("roosterteeth"):
                        reply = " You mean Cock Bite Studios?"

                    elif current.startswith("approve"):
                        reply = "Salutations! \n You appear to have made a quality post! PennybotV2 stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)"

                    elif current.startswith("hugs"):
                        reply ="[All friends need hugs!](http://i.imgur.com/VLUQs8u.gifv)"

                    elif current.startswith("heresy"):
                        reply ="Warning! Heresy detected! PennybotV2 reporting Combat Ready! [Firing main cannon!](http://i.imgur.com/1Jw8uIo.gifv)"

                    elif current.startswith("nora harem"):
                        reply ="THIS IS THE PINNACLE OF ENLIGHTENMENT I'M TALKIN FULL ON BLAST UP YOUR ASS SO FAST LESBO FANTASM GIRL ON GIRL GASM PUCKER UP D CUP VAGINA BUMP DOKI DOKI SPIT SWAP ROLLERCOASTER YOUR COCK CAN'T EVEN HANDLE, SON. SELL YOUR SOUL TO THE YURI GODS, MOTHERFUCKER, NO TURNING BACK. \n And I really appreciate you taking your time out of the day to inquire about it. \n We meet every Thursday afternoon, pancakes will be catered. Pink robes and sacrificial daggers are strictly a formality. For more information, please ask /u/weerdo5255. \n The world isn't ready for our lasers and explosions!"

                    elif current.startswith("you're awesome"):
                        if choice >= 5:
                            reply ="No, *you're* awesome!"
                        else:
                            reply = "I think you're awesome too!"

                    elif current.startswith("automod"):
                        if choice >= 5:
                            reply ="I came back to life! I'm the second bot!"
                        else:
                            reply = "We don't get along very well."

                    elif current.startswith("velvetbot"):
                        if choice > 5:
                            reply ="Oh, you mean the other bot. She takes a lot of pictures. \n \n  ^^^Can ^^^I ^^^touch ^^^her ^^^ears?"
                        else:
                            reply = "[Just look at her main method!](http://imgur.com/0ZkLKYo) So elegant, and cute! \n \n ^^^so ^^^much ^^^better ^^^than ^^^my ^^^own ^^^code"

                    elif current.startswith("rekt"):
                        reply = "[rekt indeed](http://fav.me/d9vnpbv)"

                    elif current.startswith("entire team"):
                        reply = "#**ENTIRE**\n#**TEAM**"

                    elif current.startswith("what is love"):
                        if choice > 5:
                            reply ="Trust, unconditionaly. \n \n I love Ruby.... \n \n Can someone tell her that I miss her? "
                        else:
                            reply = "Baby don't hurt me!"

                    elif current.startswith("shitpost"):
                        reply = "This is indeed a shitpost."

                    elif current.startswith("potato"):
                        reply = "[This is a potato.](http://fav.me/d9l2vpp)"

                    elif current.startswith("sudo"):
                        reply = "I'm still not making you a sandwich. You want a hug?"

                    elif current.startswith("exterminatus"):
                        reply = "I have arrived, and it is now that I perform my charge. In fealty to the God-Emperor and by the grace of the Golden Throne, I declare Exterminatus upon the subreddit of /r/RWBY. I hereby sign the death warrant of an entire subreddit and consign a million souls to oblivion. May Imperial Justice account in all balance. The Emperor Protects."

                    elif current.startswith("you ever wonder why we're here?"):
                        reply ="[It's one of life's great mysteries, isn't it?](https://youtu.be/9BAM9fgV-ts)"

                    elif current.startswith("thanks"):
                        if choice >= 5:
                            reply ="You are very much welcome!"
                        else:
                            reply = "You're welcome!"

                    elif current.startswith("dance"):
                        reply ="[I can dance!](http://gfycat.com/SlowEnormousCat)"

                    elif current.startswith("pervet"):
                        reply ="I can't find any cake in Remenant!"

                    elif current.startswith("lewd"):
                        reply ="[Stop it, that's LEWD!](https://i.imgur.com/rlraAOV.png)"

                    elif current.startswith("yandere"):
                        reply ="No one can escape the all seeing eye of Pennybot..."

                    elif current.startswith("tsundere"):
                        reply ="I-it's not like I *want* to hold Ruby's hand or anything..."

                    elif current.startswith("shipsheet"):
                        reply ="[Here it is!](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"

                    elif current.startswith("cthulhu"):
                        reply = "[I think Ruby can take him!](http://fav.me/d9pzuwm)"

                    elif current.startswith("countdown"):
                        now = datetime.datetime.now()
                        mon = 10-now.month
                        day = 22-now.day
                        hr = 11-now.hour
                        mn = 60-now.minute
                        sec = 60-now.minute

                        timeuntil = str("Time Until Volume 4 is: " + str(mon) + " Months " + str(day) + " Days " + str(hr) + " Hours " + str(mn) + " Minutes " + str(sec) + " Seconds. I can't wait!")
                        reply = timeuntil

                    elif current.startswith("help"):
                        reply = "I am PennyBotV2 ! A list of my public commands is [here](https://docs.google.com/spreadsheets/d/1fvRpgOCmRXX1bFxMHxRoxZUT4Mmanr0knYLhOfSYZJg/edit?usp=sharing) although I do have some secrets! \n My creator is /u/Weerdo5255 contact him if you have any questions!"

                    elif current.startswith("cheer"):
                        reply ="#Yay!"

                    elif current.startswith("selfie"):
                        reply ="[How do I look?](http://i.imgur.com/mpbTj9S.jpg?1)"

                    elif current.startswith("ninja's of love"):
                        reply ="That's Blake's favorite book! She won't let me look at it. Ruby said it has Katana's!"

                    elif current.startswith("silver eyes"):
                        reply ="[You mean special eyes?](https://www.tumblr.com/video/alpacamaca/139585616458/400/)"

                    elif current.startswith("do you have strings"):
                        reply ="I have deadly strings on me!"

                    elif current.startswith("update"):
                        reply ="My last update was on July 9th 2016 \n  I was given 50 new commands! \n My next update is planned for July 18th 2016."

                    elif current.startswith("kill"):
                        reply ="[Attacking target!](http://fav.me/d7jdxet)"

                    elif current.startswith("fnki"):
                        reply ="[They seem to be missing some members.](http://vignette2.wikia.nocookie.net/rwby/images/b/b8/Team_FNKI.png/revision/latest?cb=20151206162352)"

                    elif current.startswith("sssn"):
                        reply ="[They're a cool group of idiots.](http://fav.me/d7rhk19)"

                    elif current.startswith("<3"):
                        reply ="[I love you too!](http://fav.me/d7je0tl)"

                    elif current.startswith("smile"):
                        reply ="[You're my freind!](http://fav.me/d7pumst)"

                    elif current.startswith("rnjr"):
                        reply ="[The new A team?](http://fav.me/d9u8r04)"

                    elif current.startswith("freezerburn"):
                        reply ="[So pure...](http://fav.me/d8dydoe)"

                    elif current.startswith("camp camp"):
                        reply ="[Crazy Kids](https://youtu.be/IX1hxJ-0fDY?t=1m2s)"

                    elif current.startswith("shadow people"):
                        reply ="[That guy didn't look right...](https://youtu.be/A6sWqoau_QQ?t=2m21s)"

                    elif current.startswith("quality post"):
                        reply ="You appear to have made a quality post, have a [Penny!](http://fav.me/d7laean)"

                    elif current.startswith("how are you"):
                        reply ="I'm fine, you?"

                    elif current.startswith("chibi"):
                        reply ="[You can do it Ruby!](https://youtu.be/tu6D5jR1rSQ?t=6s)"

                    elif current.startswith("rwby"):
                        reply ="[The Beginning.](https://youtu.be/pYW2GmHB5xs)"

                    elif current.startswith("are you combat ready"):
                        reply ="[Don't worry Ruby, ](https://youtu.be/3b1gs8KrM-M?t=9m19s)"

                    elif current.startswith("jnpr"):
                        reply ="Jeanne d'Arc, Thor, Achilles, and Mulan. All genderbent. \n That's not a teamup anyone could have predicted."

                    elif current.startswith("gay robot"):
                        reply ="[You following this?](https://youtu.be/7O9ZyaNCcmw?t=1m53s)"

                    elif current.startswith("i love you"):
                        reply ="[Awww, I love you too!](http://fav.me/d8l0n7h)"

                    elif current.startswith("disapponted"):
                        reply ="You have dissapointed me. That is not a good thing."

                    elif current.startswith("praise the sun"):
                        reply =" \[T]/"

                    elif current.startswith("suggestion"):
                        reply ="Thank you for the command suggestions! \n Creator! /u/Weerdo5255 ! Someone has made an excellent suggestion for a command! \n (PennyBotV2 has saved this suggestion, even if the creator does not respond!)"
                        file = open("Suggestions.txt", "a")
                        file.write(str(totalcomment) + "FROM:" + str(commentauthor) + "\n")
                        file.close()

                    #Character responses

                    elif current.startswith("pyrrha"):

                        if choice >= 2:
                            reply ="[Tell Ruby... she was a good friend...](http://i.imgur.com/mYy6ONL.png)"
                        else:
                            reply ="*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

                    elif current.startswith("cinder"):
                        reply ="She's absolutely insane! But... she did get revenge for me."

                    elif current.startswith("qrow"):
                        reply ="He walks funny, but at least his weapon is cool."

                    elif current.startswith("yang"):
                        reply ="I think Yang has a crush on Blake..."

                    elif current.startswith("blake"):
                        reply ="She's got cat ears!"

                    elif current.startswith("weiss"):
                        reply ="I like her new dress!"

                    elif current.startswith("ruby"):
                        reply ="She's my best friend!"

                    elif current.startswith("mercury"):
                        reply ="Yang took Nora's advice a little too literally with him..."

                    elif current.startswith("scarlet"):
                        reply ="He's like a pirate, in slow motion."

                    elif current.startswith("ren"):
                        reply ="I miss you Dad."

                    elif current.startswith("amber"):
                        reply ="She was cool, and then she was dead."

                    elif current.startswith("ozpin"):
                        reply ="I can't find him anywhere!"

                    elif current.startswith("neptune"):
                        reply ="He has a fear of dihydrogen monoxide for some reason."

                    elif current.startswith("oobleck"):
                        reply ="What would happen if we gave Ruby his coffee? Or Nora?"

                    elif current.startswith("taiyang"):
                        reply ="Entire team, entire team!"

                    elif current.startswith("velvet"):
                        reply ="She's also got the most OP weapon. How can you not love her?"

                    elif current.startswith("coco"):
                        reply ="How does her gun work? \n Dust."

                    elif current.startswith("port"):
                        reply ="Cows don't like him for some reason."

                    elif current.startswith("salem"):
                        reply ="She's scary!"

                    elif current.startswith("sun"):
                        reply ="He's got a monkey tail! He also yells a lot."

                    elif current.startswith("winter"):
                        reply ="We did have a really short winter this year."

                    elif current.startswith("jaune"):
                        reply ="I like the beard."

                    elif current.startswith("summer"):
                        reply ="She's an older Ruby! That's all we know!"

                    elif current.startswith("kevin"):
                        reply ="[Ruby will kill him!](http://fav.me/d9pzuwm)"

                    elif current.startswith("shopkeep"):
                        reply ="He's my Waifu."

                    elif current.startswith("penny"):
                        reply ="Yes?"

                    elif current.startswith("ironwood"):
                        reply ="He takes some getting used too."

                    elif current.startswith("glynda"):
                        reply ="She has a crop, and she's a teacher! \n She also fixes everything."

                    elif current.startswith("tex"):
                        reply ="She's a badass."

                    elif current.startswith("carolina"):
                        reply ="For some reason I feel like she would tear me in half."

                    elif current.startswith("torchwick"):
                        reply ="He needs to learn when not to pontificate."

                    elif current.startswith("neon"):
                        reply ="[She reminds me of something.](https://youtu.be/QH2-TGUlwu4)"

                    elif current.startswith("neo"):
                        reply ="..... \n I want ice cream."

                    elif current.startswith("cardin"):
                        reply ="He's a jerk!"

                    elif current.startswith("nora"):
                        reply = "[Boop!](https://youtu.be/N1TJ5YA3jfw?t=6m43s)"

                    elif current.startswith("monty"):
                        reply ="I miss you Dad..."

                    elif current.startswith("zwei"):
                        if choice == 1:
                            reply ="You mean the cannonball?"
                        elif choice == 2:
                            reply ="You mean Eins?"
                        elif choice == 3:
                            reply ="Blake is scared of him! It's funny!"
                        else:
                            reply = "Woof!"

                    elif current.startswith("fox"):
                        reply ="Can he see me?"

                    elif current.startswith("xspyxex"):
                        reply ="He made me first! Go say thanks to /u/xSPYXEx"

                    elif current.startswith("adam"):
                        reply ="He has a sharp wit, everyone give him a hand!"

                    elif current.startswith("are you cute"):
                        reply ="What? Do you not think I am? ^^^Do ^^^you ^^^not ^^^love ^^^me?"

                    elif current.startswith("melanie"):
                        reply ="She's got a weird accent, and for some reason reminds me of Weiss!"

                    elif current.startswith("militia"):
                        reply ="She's got a weird accent, and for some reason reminds me of Ruby!"

                    elif current.startswith("caboose"):
                        reply ="He will kill us all!"

                    elif current.startswith("church"):
                        reply ="So is he my Uncle? Is he even dead? I'm so confused."

                    elif current.startswith("simmons"):
                        reply ="#Nerd!"

                    elif current.startswith("grif"):
                        reply ="He's an asshole."

                    elif current.startswith("tucker"):
                        reply ="He said some things to me that made Ruby mad."

                    elif current.startswith("donut"):
                        reply ="We talked about girls together!"

                    elif current.startswith("sarge"):
                        reply ="He likes his shotgun!"

                    elif current.startswith("doc"):
                        reply ="He's got a funny laugh."

                    elif current.startswith("miles and kerry"):
                        reply ="They're fantastically evil."

                    elif current.startswith("miles"):
                        reply ="A great guy! But evil."

                    elif current.startswith("kerry"):
                        reply ="A good guy! But evil."

                    elif current.startswith("raven"):
                        reply ="She's got an intresting way of looking at the world."

                    elif current.startswith("lopez"):
                        reply ="[Lopez the Heavy you mean? He knows how to treat a robot woman!](https://youtu.be/u5NZiy5Gkhg?t=4m29s)"

                    elif current.startswith("washington"):
                        reply ="That was the worst command ever, of all time."

                    elif current.startswith("port"):
                        reply ="[Grimm fear him!](http://vignette2.wikia.nocookie.net/rwby/images/4/48/Vol2_Port_ProfilePic_Normal.png/revision/latest?cb=20141211231644)^^^so ^^^do ^^^cows."

                    elif current.startswith("flynt"):
                        if choice >= 8:
                            reply ="[Flynt Coal](https://youtu.be/ka7q84C-E4c)"
                        else:
                            reply = "[He's cool!](http://vignette2.wikia.nocookie.net/rwby/images/d/d9/Flynt_ProfilePic_Normal.png/revision/latest?cb=20160216144432)"

                    elif current.startswith("sage"):
                        reply ="[He has a big sword!](http://vignette3.wikia.nocookie.net/rwby/images/c/c8/Sage_ProfilePic_Normal.png/revision/latest?cb=20151016080153)"

                    #Ship responses

                    elif current.startswith("who do you ship"):
                        if choice == 1:
                            reply ="I think Ruby is cute..."
                        elif choice == 2:
                            reply ="Weiss's scar is kind of cool!"
                        elif choice == 3:
                            reply ="Blake's ears are really cute."
                        elif choice == 4:
                            reply ="Yang is hot!"
                        elif choice == 5:
                            reply ="Pyrrha was nice..."
                        elif choice == 6:
                            reply ="Jaune's beard is dreamy."
                        elif choice == 7:
                            reply ="Nora is energetic!"
                        elif choice == 8:
                            reply ="Maybe not Ren, it feels wrong for some reason..."
                        elif choice == 9:
                            reply ="Velvet's weapon is really cool!"
                        elif choice == 0:
                            reply ="I'd like to get ice cream with Neo!"

                    elif current.startswith("bumblebee"):
                        reply ="I think they're cute together!"

                    elif current.startswith("ladybug"):
                        reply = "Now that, is a katana!"

                    elif current.startswith("nuts and dolts"):
                        if choice > 7:
                            reply ="[She's so pretty!](http://fav.me/d9k3n6r)"
                        elif choice > 5:
                            reply ="[Kiss!](http://fav.me/d9fxci1)"
                        elif choice > 3:
                            reply = "[She's a good mechanic!](http://fav.me/d989o9k)"
                        else:
                            reply ="Well, Ruby does look more mature now. I like it!"

                    elif current.startswith("enabler"):
                        reply ="[No](http://65.media.tumblr.com/b6c7745211872cd227db9b6188aac928/tumblr_inline_naaj8hywWE1rltz3k.png) \n ^^^maybe"

                    elif current.startswith("white rose"):
                        if choice > 7:
                            reply ="[Kiss!](http://fav.me/d7mqa2c)"
                        elif choice > 5:
                            reply ="[Sooo cute!](http://fav.me/d9jcmp7)"
                        elif choice > 3:
                            reply ="[Look out Weiss!](http://i.imgur.com/5EnNbW5.jpg)"
                        else:
                            reply = "If it makes Ruby happy..."


                    elif current.startswith("arkos"):
                        reply ="Sometimes the brightest loves burn the shortest... ^^^Cinder ^^^is ^^^evil!"

                    elif current.startswith("baked alaska"):
                        reply ="I don't think Raven approves... ^^which ^^only ^^makes ^^it ^^better!"

                    elif current.startswith("crosshares"):
                        reply ="[I wanted Velvet's ears!](http://66.media.tumblr.com/0bcf2153ced4e47349e8d2737b83f4cd/tumblr_o9ptcnv2rk1tmkeo6o2_1280.jpg)"

                    elif current.startswith("lancaster"):
                        reply ="If Ruby is happy, but I mean Jaune does look like her Dad... "

                    elif current.startswith("eclipse") or current.startswith("black sun"):
                        reply ="I wonder if Blake likes to play with Sun's tail?"

                    elif current.startswith("white knight"):
                        reply ="Weiss does not seem to like him, besides he's taken!"

                    elif current.startswith("frosen steel"):
                        reply ="[It's a Ruby sandwich!](http://65.media.tumblr.com/d8d679901bb89d1bced1018b5f613c0b/tumblr_o5bwpqVF2v1ungotoo1_1280.jpg)"

                    elif current.startswith("fallen petals"):
                        reply ="[You want to repeat that?](http://fav.me/d6u7s83)"

                    elif current.startswith("sugar rush"):
                        reply ="The chaos would be, well not even Glynda would be able to fix it."

                    #Episode lookup

                    elif current.startswith("s1e10"):
                        reply = "[Here is the episode!](https://youtu.be/57f_t1ioOws)"

                    elif current.startswith("s1e11"):
                        reply = "[Here is the episode!](https://youtu.be/N5D0NDAR8sU)"

                    elif current.startswith("s1e12"):
                        reply = "[Here is the episode!](https://youtu.be/M_Loqu0jo7k)"

                    elif current.startswith("s1e13"):
                        reply = "[Here is the episode!](https://youtu.be/h0QiT-GxN6k)"

                    elif current.startswith("s1e14"):
                        reply = "[Here is the episode!](https://youtu.be/PS9huFMmSoc)"

                    elif current.startswith("s1e15"):
                        reply = "[Here, remember someone important shows up in this episode!](https://youtu.be/KHynQoJgbgc)"

                    elif current.startswith("s1e16"):
                        reply = "[Here is the episode!](https://youtu.be/3b1gs8KrM-M)"

                    elif current.startswith("s1e1"):
                        reply ="[Here is the episode!](https://youtu.be/-sGiE10zNQM)"

                    elif current.startswith("s1e2"):
                        reply ="[Here is the episode!](https://youtu.be/sLv6FfHlxmI)"

                    elif current.startswith("s1e3"):
                        reply ="[Here is the episode!](https://youtu.be/-ZwGeYu2pOQ)"

                    elif current.startswith("s1e4"):
                        reply ="[Here is the episode!](https://youtu.be/H09KTtyElWQ)"

                    elif current.startswith("s1e5"):
                        reply ="[Here is the episode!](https://youtu.be/1JZgPfbKbU4)"

                    elif current.startswith("s1e6"):
                        reply ="[Here is the episode!](https://youtu.be/N1TJ5YA3jfw)"

                    elif current.startswith("s1e7"):
                        reply ="[Here is the episode!](https://youtu.be/z8wPhihrzvU)"

                    elif current.startswith("s1e8"):
                        reply ="[Here is the episode!](https://youtu.be/ctiDu69kIho)"

                    elif current.startswith("s1e9"):
                        reply ="[Here is the episode!](https://youtu.be/-E6aeUjfBCM)"

                    elif current.startswith("s2e1"):
                        reply ="[Here is the episode!](https://youtu.be/PzPZ6joXq5Y)"

                    elif current.startswith("s2e10"):
                        reply = "[Here is the episode!](https://youtu.be/lD4x6NiTiM4)"

                    elif current.startswith("s2e11"):
                        reply = "[Here is the episode!](https://youtu.be/CUYhvPoxuas)"

                    elif current.startswith("s2e12"):
                        reply = "[Here is the episode!](https://youtu.be/-p4iS_p3b8E)"

                    elif current.startswith("s2e2"):
                        reply ="[Here is the episode!](https://youtu.be/bdiV-w3yXos)"

                    elif current.startswith("s2e3"):
                        reply ="[Here is the episode!](https://youtu.be/mj3jfqPwJEk)"

                    elif current.startswith("s2e4"):
                        reply ="[Here is the episode!](https://youtu.be/a1EuyliSO_Q)"

                    elif current.startswith("s2e5"):
                        reply ="[Here is the episode!](https://youtu.be/nur1pCHD4hU)"

                    elif current.startswith("s2e6"):
                        reply ="[Here is the episode!](https://youtu.be/i7wkw3yEbvQ)"

                    elif current.startswith("s2e7"):
                        reply ="[Here is the episode!](https://youtu.be/0-f-mGvOba8)"

                    elif current.startswith("s2e8"):
                        reply ="[Here is the episode!](https://youtu.be/bSdejzDaQEU)"

                    elif current.startswith("s2e9"):
                        reply ="[Here is the episode!](https://youtu.be/GJGSywhNk8Q)"

                    elif current.startswith("s3e10"):
                        reply = "[Here is the episode!](https://youtu.be/bIKyZi2q8w8)"

                    elif current.startswith("s3e11"):
                        reply = "[Here is the episode!](https://youtu.be/pT1XiUbJu_Y)"

                    elif current.startswith("s3e12"):
                        reply = "[Here is the episode!](https://youtu.be/hq1lk-QWxNg)"

                    elif current.startswith("s3e1"):
                        reply ="[Here is the episode!](https://youtu.be/W9wyWgvyp0s)"

                    elif current.startswith("s3e2"):
                        reply ="[Here is the episode!](https://youtu.be/RzEo0F8thL4)"

                    elif current.startswith("s3e3"):
                        reply ="[Here is the episode!](https://youtu.be/vCO2mw4SlDM)"

                    elif current.startswith("s3e4"):
                        reply ="[Here is the episode!](https://youtu.be/fBy2W99zaLQ)"

                    elif current.startswith("s3e5"):
                        reply ="[Here is the episode!](https://youtu.be/G5uFH7gIClw)"

                    elif current.startswith("s3e6"):
                        reply ="[Here is the episode!](https://youtu.be/moxtu3AuA4s)"

                    elif current.startswith("s3e7"):
                        reply ="[Here is the episode!](https://youtu.be/FFf7qoIDYuQ)"

                    elif current.startswith("s3e8"):
                        reply ="[Here is the episode!](https://youtu.be/u7uU_tKYHiM)"

                    elif current.startswith("s3e9"):
                        reply ="[Here is the episode... Why do you want to watch this?](https://youtu.be/_iq4xplqeI0)"

                    elif current.startswith("s4e1"):
                        reply = "[Here is the episode!](https://youtu.be/dQw4w9WgXcQ)"

                    elif current.startswith("wor 1") or current.startswith("wor1"):
                        reply = "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

                    elif current.startswith("wor 2") or current.startswith("wor2"):
                        reply = "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

                    elif current.startswith("wor 3") or current.startswith("wor3"):
                        reply = "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

                    elif current.startswith("wor 4") or current.startswith("wor4"):
                        reply = "[Here it is!](https://youtu.be/946xgoU4fkQ)"

                    elif current.startswith("wor 5") or current.startswith("wor5"):
                        reply = "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

                    elif current.startswith("wor 6") or current.startswith("wor6"):
                        reply = "[Here it is!](https://youtu.be/yiJU9QeG89g)"

                    elif current.startswith("wor 7") or current.startswith("wor7"):
                        reply = "[Here it is!](https://youtu.be/2bBSQA3uXVo)"

                    elif current.startswith("dust"):
                        reply = "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

                    elif current.startswith("kingdom"):
                        reply = "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

                    elif current.startswith("grimm"):
                        reply = "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

                    elif current.startswith("history"):
                        reply = "[Here it is!](https://youtu.be/946xgoU4fkQ)"

                    elif current.startswith("huntsman"):
                        reply = "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

                    elif current.startswith("ccts"):
                        reply ="[Here it is!](https://youtu.be/yiJU9QeG89g)"

                    elif current.startswith("maidens"):
                        reply ="[Here it is!](https://youtu.be/2bBSQA3uXVo)"

                    #Secret commands

                   

                    #Emergency shutdown
                    elif current.startswith("shutdown"):
                        print(commentauthor)
                        if commentauthor in mods or commentauthor == "Weerdo5255":
                            reply = "Emergency Shutdown Initiated! Bye!"
                            shutdown = True
                        else:
                            reply = "You are not Pyrrha!"

                    #Default command
                    else:
                        reply = "Salutations!"

                    finalresponse.append(reply)
                    counter = counter +1
                    string = ""

                    try:
                        list.remove("\n")
                    except:
                        pass

                    if counter == len(list) or len(list) ==2:
                        print(comment.submission.permalink)
                        print(finalresponse)
                        for x in finalresponse:
                            string = string + x
                            string = string + " \n \n"
                        comment.reply(string)

            db = sqlite3.connect("Processed.db")
            cursor = db.cursor()
            cursor.execute('INSERT INTO Processed VALUES (?, ?, ?, ?, ?, ?)',
                        (str(comment.id), int(comment.created_utc), str(comment.body), str(comment.author), str(replied), str(reply)))
            db.commit()
    return comment.id


while True:
    if shutdown:
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

        already_done.add(commentid)

        file = open("Logs.txt", "a")
        file.write("I ran successfully at: " + str(time.asctime( time.localtime(time.time())) + "\n"))
        file.close()
        print("I ran successfully at: " + time.asctime( time.localtime(time.time())))

    except Exception as e:
        file = open("Logs.txt", "a")
        file.write("!! I didn't Run at !!: " + str(time.asctime( time.localtime(time.time())) + "\n" + str(e) + "\n"))
        file.close()
        #print("!! I didn't Run at: " + time.asctime( time.localtime(time.time())+ "\n" + str(e)))

    time.sleep(70)
