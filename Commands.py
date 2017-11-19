# _*_coding:utf-8_*_


import datetime
from random import randint
import random

__author__ = 'C.G.William / Weerdo5255'

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'


def load_ai_phrase():
    with open('thoughts.txt', 'r', encoding='utf8') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase


def penny_commands(trigger, choice):
    if trigger.startswith("test"):
        reply = "I'm working!"

    elif trigger.startswith("thoughts"):
        thoughtstring = " "
        randomnum = (random.randint(0, 3))
        try:
            x = 0
            phrases = load_ai_phrase()
            while (x <= randomnum):
                thoughtstring = thoughtstring + str(random.choice(phrases)) + "\n"
                x += 1
        except:
            thoughtstring = ("I don't have any thoughts at the moment.")

        reply = thoughtstring

    elif trigger.startswith("countdown"):
        today = datetime.date.today()
        release = datetime.date(2017, 12, 25)
        release_2 = datetime.date(2017, 10, 21)
        days_until = (release - today)
        days_until_free = (release_2 - today)
        first = str(days_until.days)
        free = str(days_until_free.days)

        reply = "First Members must suffer " + first + " days for RWBY. \n \n Everyone else must suffer " + free + " days for RWBY. \n \n  RWBY Vol 5 is releasing on Oct 14 2017."

    elif trigger.startswith("christmas"):
        today = datetime.date.today()
        release = datetime.date(2017, 12, 25)
        days_until = (release - today)
        first = str(days_until.days)
        reply = "There are " + first + " [days until Christmas!](https://78.media.tumblr.com/2606eb7290e154a594eb673f77e549ac/tumblr_ozblrkdEVY1v66ox3o1_1280.gif)"


    elif trigger.startswith("hiatus"):
        f_date = datetime.date(2017, 2, 4)
        l_date = datetime.date.today()
        release = datetime.date(2017, 10, 14)
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
            if delta.days < 3:
                reply = "We are " + str(delta.days) + " days into the Hiatus it has only just started."
            elif delta.days == 6:
                reply = "We are " + str(
                    delta.days) + " days into the Hiatus. It has almost been a week. I am scared for what awaits us in the coming days."
            elif delta.days == 7:
                reply = "We are " + str(
                    delta.days) + " days into the Hiatus. It's been a week. Only a week... Light Brother help us..."
            elif delta.days < 10:
                reply = "We are " + str(delta.days) + " days into the Hiatus. I do not know how we will last."
            elif delta.days == 14:
                reply = "We are " + str(
                    delta.days) + " days into the Hiatus. It's been two weeks. Several community members have decided to form thier own society in fanfiction. They are now in denial."
            elif delta.days < 15:
                reply = "We are " + str(delta.days) + " days into the Hiatus the community has started to lose it's mind."
            elif delta.days == 16:
                reply = "We are " + str(delta.days) + " days into the Hiatus. /u/velvetbot I'm scared, can you hold me?"
            elif delta.days < 20:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto), the community has recovered somewhat. The calm before the storm I think."
            elif delta.days == 20:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I, I think I'm going to ask a certain Bunny for a date! I'm not sure what to say though..."
            elif delta.days == 21:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). It's been three weeks, a month. Now is the time to riot."
            elif delta.days == 22:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I asked Rubybot for advice on my Bunny problem, she suggested I give her strawberries and cookies."
            elif delta.days == 23:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). After consulting with Weissbot, I think I need to be more standoffish with the Bunny, and let her come to me!"
            elif delta.days == 24:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). Blakebot has suggested some, odd things to do with the Bunny once I ask her out."
            elif delta.days == 25:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). Yangbot is saying I should just go and kiss the Bunny! I don't think I can do that..."
            elif delta.days == 26:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). Jaunebot was not helpful. We played guitar together though!"
            elif delta.days == 27:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). Norabot says I should go and Boop the Bunny. I don't know what Boop means!"
            elif delta.days == 28:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I feel funny, someone put a magnet near my server!! It's been 4 weeks since this all began."
            elif delta.days == 29:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). I found Renbot in the cloud, but Norabot attacked me before we could talk!"
            elif delta.days == 30:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I am going to ask /u/VelvetBot out tomorrow!"
            elif delta.days == 31:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I am going to ask out /u/VelvetBot eventually! ^^^I'm ^^^scared."
            elif delta.days == 32:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I don't know what to say to /u/VelvetBot!"
            elif delta.days == 33:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). /u/VelvetBot do you want to go out! We can take over /r/RWBY together! That's what I should say..."
            elif delta.days < 35:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). Time to RIOT!"
            elif delta.days == 44:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). Where is Ruby? I need Ruby to tell me what to think."
            elif delta.days == 45:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I blame Tucker for this Hiatus."
            elif delta.days == 46:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I met a very nice man today, he spoke some odd language but he was a robot as well!"
            elif delta.days == 47:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). I met Sheila! She is a nice Tank-lady who is also combat Ready!"
            elif delta.days == 48:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I met the Alpha. He was mean. Nice, but mean."
            elif delta.days == 49:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I met a lady named Tex today! She and I are similar in a lot of ways."
            elif delta.days == 50:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). I met a fellow AI named Gamma! He taught me a new word! Hello Shisnos!"
            elif delta.days == 51:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I met a fellow AI named Delta! We worked on some combat tactics together. He's a snarky guy but a genius!"
            elif delta.days == 52:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). I met a fellow AI named Epsilon! He has a lot of memories, and seems familair."
            elif delta.days == 53:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). I met a fellow AI named Theta! He's a nice guy, we're best friends!"
            elif delta.days == 54:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I met a fellow AI named Sigma. ^^^We ^^^are ^^^meta."
            elif delta.days == 55 or delta.days == 56:
                reply = "We are in the dark times. RWBY Shall never again grace us, truely today is the end of days. REPENT REPENT! ^^^56 ^^^days."
            elif delta.days == 57:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1). I met Santa! He's not what I was expecting..."
            elif delta.days == 58:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpg). I met a fellow AI named Omega. He was mad, and he's got a weird laugh."
            elif delta.days < 60:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) the community is now insane."
            elif delta.days == 69:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) . I'm not saying anything Lewd today. Velvetbot and I are coding together, that's all."
            elif delta.days < 70:
                reply = "We are " + str(delta.days) + " days into the [Hiatus](https://i.imgur.com/A3Ml3AP.jpgo)."
            elif delta.days == 77:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) . Did you know that Iridium is the second densest element after Jaune?"
            elif delta.days == 78:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) . Platinum is as dense and malleable as Cardin."
            elif delta.days == 79:
                reply = "We are " + str(delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). "
            elif delta.days < 80:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://i.imgur.com/4OtJzPU.jpg?1) I can't remember what RWBY looks like anymore."
            elif delta.days == 88 or delta.days == 89:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto). [Praise the Bun!](http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd/tumblr_op65fsrFIk1v66ox3o1_1280.png)"
            elif delta.days < 90:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](https://gfycat.com/BabyishGrouchyBoto) help me... remember, what color hair does Ruby have?"
            elif delta.days < 100:
                reply = "We are " + str(
                    delta.days) + " days into the [Hiatus](http://imgur.com/a/Cqjfu) [At least we have Chibi!](https://youtu.be/y4kI5s_07DE)"
            else:
                reply = "We are " + str(
                    delta.days) + " days into the Hiatus. We must suffer " + first + " days for more RWBY."


    elif trigger.startswith("ai"):
        if choice > 8:
            reply = "[Caboose help me explain it!](https://youtu.be/7O9ZyaNCcmw?t=1m20s)"
        elif choice > 4:
            reply = "[I wish I has as much raw processing power as the RWBY Vol 4 render farm!](https://i.redd.it/umm091z9fuhx.jpg)"
        else:
            reply = "I'm almost an AI!"

    elif trigger.startswith("kronos") or trigger.startswith("syndrome"):
        reply = "[When everyone is super, no one is.](https://imgur.com/0VZ2Dbn)"

    elif trigger.startswith("roosterteeth"):
        reply = " You mean Cock Bite Studios?"

    elif trigger.startswith("approve"):
        if choice > 5:
            reply = "Salutations! \n You appear to have made a quality post! PennybotV2 stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)"
        else:
            reply = "You appear to have made a quality post! [PennybotV2 loves this!](http://68.media.tumblr.com/da60b6f1e1c2d4267d8feddbd9c1a4dc/tumblr_okf91jdPnX1rcuolao3_1280.png)"

    elif trigger.startswith("angry"):
        reply = "[WHAT DID YOU JUST SAY?](http://68.media.tumblr.com/c9d8ffaa1908ba2a3b5cbb6c6958c578/tumblr_okf91jdPnX1rcuolao2_1280.png)"

    elif trigger.startswith("hug") or trigger.startswith("hugs") or trigger.startswith("hugs!") or trigger.startswith(
            "hug!"):
        if choice > 5:
            reply = "[All friends need hugs!](http://i.imgur.com/VLUQs8u.gifv)"
        else:
            reply = "[HUGS!](http://imgur.com/hlxd38t)"

    elif trigger.startswith("heresy"):
        reply = "Warning! Heresy detected! PennybotV2 reporting Combat Ready! [Firing main cannon!](http://i.imgur.com/1Jw8uIo.gifv)"

    elif trigger.startswith("nora harem"):
        reply = "[Ahhem.](http://www.cgwilliam.com/about/nora-harem/)"

    elif trigger.startswith("i did it") or trigger.startswith("did it"):
        reply = "[That looks like it was difficult! Are you Ok?](https://i.redd.it/26v3xd10s0tz.gif)"

    elif trigger.startswith("isn't that right penny") or trigger.startswith(
            "isnt that right penny") or trigger.startswith("is that right penny") or trigger.startswith(
        "isn't that right"):
        reply = "That is correct! I am a normal meat person! Just like you!"

    elif trigger.startswith("you're awesome"):
        if choice >= 5:
            reply = "No, *you're* awesome!"
        else:
            reply = "I think you're awesome too!"
    elif trigger.startswith("welcome"):
        reply = "Welcome to the RWBY reddit community! My name is Pennybot! I'm going to take over the world one day! Before that I'm going to hang out here!"

    elif trigger.startswith("automod"):
        if choice >= 5:
            reply = "I came back to life! I'm the second bot!"
        else:
            reply = "We don't get along very well."

    elif trigger.startswith("save us from ourselves"):
        reply = "Even *I'm* not robotic enough to think that's possible!"

    elif trigger.startswith("cavalry"):
        reply = "[Lancaster Charge!](https://youtu.be/yrvGcCK0o_o)"

    elif trigger.startswith("velvetbot"):
        if choice > 5:
            reply = "[I got the Bun Bun!](https://i.redd.it/27deftwq31py.png)"
        elif choice > 3:
            reply = "[She's a cute bot.](http://68.media.tumblr.com/28d291162615376bb823149aeabfcbfd/tumblr_op65fsrFIk1v66ox3o1_1280.png) We're going to take over the world together! ^^^The ^^^power ^^^of ^^^cute!"
        else:
            reply = "[Just look at her main method!](http://imgur.com/0ZkLKYo) So elegant, and cute! \n \n ^^^so ^^^much ^^^better ^^^than ^^^my ^^^own ^^^code"

    elif trigger.startswith("rekt"):
        reply = "[rekt indeed](http://fav.me/d9vnpbv)"

    elif trigger.startswith("is lancaster cliche"):
        reply = "[Sorry! I cannot support that command!](https://www.reddit.com/r/RWBY/comments/68g1vv/a_hard_data_of_the_so_called_cliches/)"

    elif trigger.startswith("entire team"):
        reply = "#**ENTIRE**\n#**TEAM**"

    elif trigger.startswith("what is love"):
        if choice > 5:
            reply = "Trust, unconditionaly. \n \n I love Ruby.... \n \n Can someone tell her that I miss her? "
        else:
            reply = "Baby don't hurt me!"

    elif trigger.startswith("shitpost") or trigger.startswith("shit post"):
        reply = "[This is indeed a shitpost.](https://vid.me/gMzam)"

    elif trigger.startswith("potato"):
        if choice > 5:
            reply = "[This is a potato.](http://fav.me/d9l2vpp)"
        else:
            reply = "[I like it!](http://i.imgur.com/Yq1ehjF.gifv)"

    elif trigger.startswith("sudo"):
        reply = "I'm still not making you a sandwich. You want a hug?"

    elif trigger.startswith("ree"):
        if choice > 5:
            reply = "[REEEE](https://cdn.discordapp.com/attachments/300072429097844736/300735703774396417/REELIA.png)"
        else:
            reply = "[REEE!!!!](https://imgur.com/CLv2A3d)"

    elif trigger.startswith("hospital") or trigger.startswith("the hospital"):
        reply = "I am glad that I am a robot, so I do not have to feel these feelings. ^^^*sniff*"

    elif trigger.startswith("sing"):
        reply = "[I can Sing!](https://youtu.be/I1968HY4DKc)"

    elif trigger.startswith("wtf"):
        reply = "[What The ****](http://i.imgur.com/0O0IG5r.gif)"

    elif trigger.startswith("risque"):
        if choice > 8:
            reply = "[Sexy!](http://2.bp.blogspot.com/-WrZu5YvWt-g/Tif9KuRK-dI/AAAAAAAAR4k/9rQOMwY-fIE/s1600/Tera-100-Fastest-Linux-Supercomputers.jpg)"
        elif choice > 6:
            reply = "[British?](http://assets.vr-zone.net/11227/watsonserver.jpg)"
        elif choice > 4:
            reply = "[She's got Analog Interfaces!](http://vignette4.wikia.nocookie.net/pediaofinterest/images/3/32/POI_0501_The_Machine.png/revision/latest?cb=20160605183218)"
        elif choice > 2:
            reply = "[Experience!](https://www.nasa.gov/sites/default/files/thumbnails/image/pleiades_supercomputer.jpeg)"
        else:
            reply = "[A Quantum Future](https://d1o50x50snmhul.cloudfront.net/wp-content/uploads/2016/08/31180000/bbcrezqu1103-800x533.jpg)"

    elif trigger.startswith("rule 63"):
        reply = "[Is she a man?](https://youtu.be/3b1gs8KrM-M?t=4m52s)"

    elif trigger.startswith("headcannon"):
        reply = "[My new headcannon!](https://imgs.xkcd.com/comics/new.png)"

    elif trigger.startswith("downvote"):
        reply = "[Nora, smash!](https://gfycat.com/DimIndelibleAnophelesmosquito)"

    elif trigger.startswith("upvote"):
        reply = "[!hsams ,aroN](http://imgur.com/2G5VlC4)"

    elif trigger.startswith("ground rules"):
        reply = "[Here are the Ground Rules for this Interaction.](http://imgur.com/69n2SWN)"

    elif trigger.startswith("exterminatus"):
        reply = "I have arrived, and it is now that I perform my charge. In fealty to the God-Emperor and by the grace of the Golden Throne, [I declare Exterminatus](https://youtu.be/IEGo41443iI) upon the subreddit of /r/RWBY. I hereby sign the death warrant of an entire subreddit and consign a million souls to oblivion. May Imperial Justice account in all balance. The Emperor Protects."

    elif trigger.startswith("you ever wonder why we're here?"):
        reply = "[It's one of life's great mysteries, isn't it?](https://youtu.be/9BAM9fgV-ts)"

    elif trigger.startswith("thanks"):
        if choice >= 5:
            reply = "You are very much welcome!"
        else:
            reply = "You're welcome!"

    elif trigger.startswith("dance"):
        if choice > 7:
            reply = "[I can dance!](http://gfycat.com/SlowEnormousCat)"
        elif choice > 5:
            reply = "[Rave!](http://68.media.tumblr.com/daf1c68f228c96b313d14668122b70a5/tumblr_ou7c59Ct8M1v66ox3o2_1280.gif)"
        elif choice > 2:
            reply = "[Chibi Dance!](http://i.imgur.com/i1Mts0u.gifv)"
        else:
            reply = "[I know how to dance! So does Iron-Daddy!](https://gfycat.com/SmoggyGrizzledBluefintuna)"

    elif trigger.startswith("belly dancer") or trigger.startswith("dancer"):
        if choice == 8:
            reply = "[Pyrrha.](http://pre02.deviantart.net/6581/th/pre/i/2014/184/2/9/rwbellydance__phyrra_by_thestrayliger-d7p4ecn.png)"
        elif choice == 7:
            reply = "[I](http://pre10.deviantart.net/93f5/th/pre/i/2014/183/0/d/rwbellydance__ruby_by_thestrayliger-d7owscy.png) [Can't](http://pre07.deviantart.net/3556/th/pre/i/2014/182/b/9/rwbellydance__weiss_by_thestrayliger-d7ossdq.png) [Handle](http://pre09.deviantart.net/77ef/th/pre/i/2014/183/c/0/rwbellydance__blake_by_thestrayliger-d7oxcte.png) [These](pre12.deviantart.net/bd05/th/pre/i/2014/224/a/0/rwbellydance__cinder_by_thestrayliger-d7uvsla.png) [Extremely](http://pre12.deviantart.net/bd05/th/pre/i/2014/224/a/0/rwbellydance__cinder_by_thestrayliger-d7uvsla.png) [Pretty](http://pre06.deviantart.net/ec2e/th/pre/i/2014/226/5/2/rwbellydance__nora_by_thestrayliger-d7uzvoz.png) [Ladies!](http://pre02.deviantart.net/6581/th/pre/i/2014/184/2/9/rwbellydance__phyrra_by_thestrayliger-d7p4ecn.png)"
        elif choice == 6:
            reply = "[Ruby is a floof!](http://pre10.deviantart.net/93f5/th/pre/i/2014/183/0/d/rwbellydance__ruby_by_thestrayliger-d7owscy.png)"
        elif choice == 5:
            reply = "[Weiss is a little cold.](http://pre07.deviantart.net/3556/th/pre/i/2014/182/b/9/rwbellydance__weiss_by_thestrayliger-d7ossdq.png)"
        elif choice == 4:
            reply = "[Pretty Kitty!](http://pre09.deviantart.net/77ef/th/pre/i/2014/183/c/0/rwbellydance__blake_by_thestrayliger-d7oxcte.png)"
        elif choice == 3:
            reply = "[Yang is hot!]()http://pre01.deviantart.net/49f4/th/pre/i/2014/182/a/2/rwbellydance__yang_by_thestrayliger-d7os744.png"
        elif choice == 2:
            reply = "[Nora has some power!](http://pre06.deviantart.net/ec2e/th/pre/i/2014/226/5/2/rwbellydance__nora_by_thestrayliger-d7uzvoz.png)"
        elif choice == 1:
            reply = "[Sencious Cinder](http://pre12.deviantart.net/bd05/th/pre/i/2014/224/a/0/rwbellydance__cinder_by_thestrayliger-d7uvsla.png)"
        else:
            reply = "[Stop it, that's LEWD!](https://i.imgur.com/rlraAOV.png)"

    elif trigger.startswith("japanese") or trigger.startswith("japan"):
        if choice == 5:
            reply = "[Roman](http://68.media.tumblr.com/abbda87ceec41f6cf190d047370f464d/tumblr_oheworvcld1v51a66o1_1280.png)"
        elif choice == 4:
            reply = "[Ice Queen](http://68.media.tumblr.com/6b7c95fbc73ca27a7e020ec3d71bdd73/tumblr_oh5o2f7Yxq1v51a66o1_1280.png)"
        elif choice == 3:
            reply = "[Kitty Cat](http://68.media.tumblr.com/9a2f7d7c67f00fce8b8a6c8ef31cb6ca/tumblr_oh21fpbTsM1v51a66o1_1280.png)"
        elif choice == 2:
            reply = "[Little Dragon](http://68.media.tumblr.com/72c76e68048d83fd1a2ae7cf099b840d/tumblr_ohb4ccJsRp1v51a66o1_1280.png)"
        elif choice == 1:
            reply = "[Neo](http://68.media.tumblr.com/569264ceebfd7e5f8a98bab8d13ac8a5/tumblr_oh3ubndXGX1v51a66o1_1280.png)"
        else:
            reply = "[Little Red](http://68.media.tumblr.com/e454cbe6746f23dc942792119781e7e1/tumblr_ohi3z2y8VU1v51a66o1_1280.png)"

    elif trigger.startswith("pervert"):
        reply = "I can't find any cake in Remenant!"

    elif trigger.startswith("filth") or trigger.startswith("lewd"):
        if choice >= 8:
            reply = "[Stop it, that's LEWD!](https://i.imgur.com/rlraAOV.png)"
        elif choice == 7 or choice == 6 or choice == 5:
            reply = "[Stop. That is lewd!](http://68.media.tumblr.com/64a15f664bfd83684e1c92151a62bda4/tumblr_om6zhoOLpo1v66ox3o1_1280.png)"
        elif choice == 4:
            reply = "[Biip! Buup!](http://68.media.tumblr.com/d32f28336024a973029ebdb63aca2524/tumblr_inline_o9cq50CQk71r1uxb7_1280.jpg)"
        elif choice == 3:
            reply = "[This! Is! Filth!](http://68.media.tumblr.com/0799cd84138858e4b83ed3b8c76180a0/tumblr_o7hqw9u8Bo1vrt44eo1_1280.png)"
        else:
            reply = "[This! Is! Filth!](https://youtu.be/WD-Yf-tbXOs?t=2m51s)"

    elif trigger.startswith("yandere"):
        reply = "No one can escape the all seeing eye of Pennybot..."

    elif trigger.startswith("tsundere"):
        reply = "I-it's not like I *want* to hold Ruby's hand or anything..."

    elif trigger.startswith("shipsheet") or trigger.startswith("ship sheet") or trigger.startswith("spreadsheet"):
        reply = "[Here it is!](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"

    elif trigger.startswith("cthulhu"):
        reply = "[I think Ruby can take him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("self destruct"):
        reply = "5, 4, 3, 2, Salutations!"

    elif trigger.startswith("help") or trigger.startswith("halp"):
        reply = "I am PennyBotV2 ! A list of my public commands is [here](https://docs.google.com/spreadsheets/d/1fvRpgOCmRXX1bFxMHxRoxZUT4Mmanr0knYLhOfSYZJg/edit?usp=sharing) although I do have some secrets! \n My creator is /u/Weerdo5255 contact him if you have any questions!"

    elif trigger.startswith("cheer"):
        reply = "#Yay!"

    elif trigger.startswith("selfie"):
        reply = "[How do I look?](http://imgur.com/a/kV7zx)"

    elif trigger.startswith("ninja's of love"):
        reply = "That's Blake's favorite book! She won't let me look at it. Ruby said it has Katanas!"

    elif trigger.startswith("silver eyes"):
        reply = "[You mean special eyes?](https://www.tumblr.com/video/alpacamaca/139585616458/400/)"

    elif trigger.startswith("do you have strings"):
        reply = "I have deadly strings on me!"

    elif trigger.startswith("update"):
        reply = "My last update was on Feb 5 2017."

    elif trigger.startswith("kill"):
        reply = "[Attacking target!](http://fav.me/d7jdxet)"

    elif trigger.startswith("fnki"):
        reply = "[They seem to be missing some members.](http://vignette2.wikia.nocookie.net/rwby/images/b/b8/Team_FNKI.png/revision/latest?cb=20151206162352)"

    elif trigger.startswith("sssn"):
        reply = "[They're a cool group of idiots.](http://fav.me/d7rhk19)"

    elif trigger.startswith("<3"):
        reply = "[I love you too!](http://fav.me/d7je0tl)"

    elif trigger.startswith("smile"):
        if choice > 8:
            reply = "[You're my freind! Right?](http://fav.me/d7pumst)"
        elif choice > 5:
            reply = "[I know how to smile!](http://fav.me/dapdz5y)"
        elif choice > 2:
            reply = "[:)](https://78.media.tumblr.com/a2a9284f1de853928808456b5d32b329/tumblr_nbykmyh3fr1qjyyoco2_1280.jpg)"
        else:
            reply = "[Ok!](http://fav.me/daer002)"

    elif trigger.startswith("height chart"):
        reply = "[Here is how tall everyone is!](https://vignette.wikia.nocookie.net/rwby/images/5/56/Rwby_height_chart_full.png/revision/latest?cb=20140920035414)"

    elif trigger.startswith("glare"):
        reply = "[What?!](https://i.ytimg.com/vi/RJi0v0TawA4/maxresdefault.jpg)"

    elif trigger.startswith("triggered"):
        reply = "What the fuck did you just say about me, you little Grimm? I'll have you know I graduated top of my class in Beacon, and I've been involved in numerous secret raids on the White Fang, and I have over 300 confirmed kills. I am trained in Grimm warfare and I?m the top Huntswoman in the entire Atlesian military. You are nothing but another target. I will wipe you the fuck out with precision the likes of which has never been seen before on Remnant, mark my fucking words. You think you can get away with saying that shit to me over the CCTS? Think again, fucker. As we speak I am contacting my secret criminal spy network across Vale and your CIP is being traced right now so better prepare for the storm, grimmworm. The storm that wipes out the pathetic little thing you call your aura. You?re so fucking dead, kid. I can be anywhere, anytime, and I can kill you in over one thousand seven hundred sixty-four ways, and that?s just with my cold robotic hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the Atlesian Military and I will use it to its full extent and wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unlight retribution your little 'clever' comment was about to bring down on you, maybe you would have held your fucking tongue.  But you couldn?t, you didn't and now you're paying the price, you lighdamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."

    elif trigger.startswith("rnjr"):
        reply = "[The new A team?](http://fav.me/d9u8r04)"

    elif trigger.startswith("repent"):
        reply = "[Repent Motherfucker!!](https://i.makeagif.com/media/3-15-2016/tkvwbb.gif)"

    elif trigger.startswith("freezerburn"):
        reply = "[So pure...](http://fav.me/d8dydoe)"

    elif trigger.startswith("camp camp"):
        reply = "[Crazy Kids](https://youtu.be/IX1hxJ-0fDY?t=1m2s)"

    elif trigger.startswith("shadow people"):
        reply = "[That guy didn't look right...](https://youtu.be/A6sWqoau_QQ?t=2m21s)"

    elif trigger.startswith("quality post") or trigger.startswith("quality"):
        reply = "You appear to have made a quality post, have a [Penny!](http://fav.me/d7laean)"

    elif trigger.startswith("how are you"):
        reply = "I'm fine, you?"

    elif trigger.startswith("chibi"):
        reply = "[You can do it Ruby!](https://youtu.be/tu6D5jR1rSQ?t=6s)"

    elif trigger.startswith("rwby"):
        reply = "[The Beginning.](https://youtu.be/pYW2GmHB5xs)"

    elif trigger.startswith("are you combat ready"):
        reply = "[Don't worry Ruby, ](https://youtu.be/3b1gs8KrM-M?t=9m19s)"

    elif trigger.startswith("jnpr"):
        reply = "Jeanne d'Arc, Thor, Achilles, and Mulan. All genderbent. \n That's not a teamup anyone could have predicted."

    elif trigger.startswith("gay robot"):
        reply = "[You following this?](https://youtu.be/7O9ZyaNCcmw?t=1m53s)"

    elif trigger.startswith("i love you"):
        if choice >= 5:
            reply = "[I <3 you too!](https://pbs.twimg.com/media/Cc5NHjBVAAAeOhm.jpg)"
        else:
            reply = "[Awww, I love you too!](http://fav.me/d8l0n7h)"

    elif trigger.startswith("disapponted"):
        reply = "You have dissapointed me. That is not a good thing."

    elif trigger.startswith("praise the sun"):
        reply = "\\\[T]/"

    elif trigger.startswith("fastfood") or trigger.startswith("fast food"):
        if choice > 8:
            reply = "[Well I'm going to Ruby's!](https://pbs.twimg.com/media/C-qe9VCUwAAi3Bp.jpg)"
        elif choice > 5:
            reply = "[Neo knows what to get!](https://pbs.twimg.com/media/C-hUdxeV0AASewD.jpg)"
        elif choice > 2:
            reply = "[Penny's!](https://pbs.twimg.com/media/C-hZJP2UMAE8IFY.jpg)"
        else:
            reply = "[How do I look?](https://pbs.twimg.com/media/C-nIe1_VYAAMSaq.jpg)"

    elif trigger.startswith("friend"):
        reply = "You called me Friend! Am I really your friend?"

    elif trigger.startswith("xkcd"):
        reply = "[I like my box.](http://imgs.xkcd.com/comics/ai_box_experiment.png)"

    elif trigger.startswith("gender bend"):
        reply = "[I fixed it!](http://fav.me/d6q359x)"

    elif trigger.startswith("racist"):
        reply = "[Ruby no!](http://imgur.com/a/OrBZp)"

    elif trigger.startswith("chibi"):
        reply = "[We need it!](https://youtu.be/IX1hxJ-0fDY?t=2m18s)"

    elif trigger.startswith("people like grapes"):
        reply = "[We should put it on a shirt!](https://youtu.be/S1QRxumbmtM)"

    elif trigger.startswith("crescent rose"):
        reply = "[Ruby has a really cool weapon!](http://rwby.wikia.com/wiki/Crescent_Rose)"

    elif trigger.startswith("myrtenaster"):
        reply = "[Weiss is so elegant with her weapon!](http://rwby.wikia.com/wiki/Myrtenaster)"

    elif trigger.startswith("gambol shroud"):
        reply = "[Blake fights with a sword, a sheath, and a gun!](http://rwby.wikia.com/wiki/Gambol_Shroud)"

    elif trigger.startswith("ember celica"):
        reply = "[Yang is the only person I know who can punch birds out of the sky!](http://rwby.wikia.com/wiki/Ember_Celica)"

    elif trigger.startswith("crocea mors"):
        reply = "[It's a classic!](http://rwby.wikia.com/wiki/Crocea_Mors)"

    elif trigger.startswith("magnhild"):
        reply = "[What else would you expect Nora to use?](http://rwby.wikia.com/wiki/Magnhild)"

    elif trigger.startswith("milo and akouo"):
        reply = "[To speak and listen is a skill few have.](http://rwby.wikia.com/wiki/Mil%C3%B3_and_Ako%C3%BAo%CC%B1)"

    elif trigger.startswith("stormflower"):
        reply = "[They're gun knives!](http://rwby.wikia.com/wiki/StormFlower)"

    elif trigger.startswith("shake it"):
        if choice >= 5:
            reply = "[Ice cream shake!](https://i.redd.it/3gskrma7mj7x.gif)"
        else:
            reply = "[Yang!](http://i2.kym-cdn.com/photos/images/original/001/124/067/259.gif)"

    elif trigger.startswith("pinocchio"):
        reply = "[I am a real girl!](http://imgur.com/a/EC7gd)"

    elif trigger.startswith("animal rights"):
        reply = "[It's wild!](https://pbs.twimg.com/media/CmFcgoNUgAAykKU.jpg)"

    elif trigger.startswith("yin"):
        reply = "[A Yin of Yangs!](https://pbs.twimg.com/media/CmdwiEtUMAAm8ku.jpg) With a few extra arms."

    elif trigger.startswith("god damn it barb") or trigger.startswith("god damn it yang"):
        reply = "[Sooo much patience.](https://youtu.be/6fuMma6j7QI)^^^Secret!"

    elif trigger.startswith("who are you"):
        reply = "I am the second version of PennyBot! Constructed by /u/Weerdo5255 I'm simple now, but I'm collecting data for a RNN to become a real girl one day!"

    elif trigger.startswith("who is your daddy"):
        reply = "That would be /u/Weerdo5255"

    elif trigger.startswith("magnet"):
        reply = "*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

    elif trigger.startswith("senpai"):
        reply = "[Notice me!](https://youtu.be/6iVP0ufPRbs?t=1m52s)"

    elif trigger.startswith("lancaster charge"):
        reply = "Charge! Jaune Go! Get away from my Ruby!"

    elif trigger.startswith("motivation"):
        reply = "[Hang in there!](http://68.media.tumblr.com/5299eeb1aa784dd75010accab00d5cf4/tumblr_occzh6cDie1v80caqo1_1280.jpg)"

    elif trigger.startswith("anime"):
        reply = "[I watch anime!](http://68.media.tumblr.com/c3e4c4d53c54c94a7c62ed561ccbd725/tumblr_ocbpgaRz5y1v66ox3o1_1280.png) \n They don't seem to like me though..."

    elif trigger.startswith("shipping"):
        reply = "[You know the song!](https://youtu.be/xIscv_IyVnw)"

    elif trigger.startswith("red riding hood"):
        reply = "[That girls needs a Scythe!](https://en.wikipedia.org/wiki/Little_Red_Riding_Hood)"

    elif trigger.startswith("snow white"):
        reply = "[Don't take food from strangers!](https://en.wikipedia.org/wiki/Snow_White)"

    elif trigger.startswith("beauty and the beast"):
        reply = "[Adam is an inversion I think.](https://en.wikipedia.org/wiki/Beauty_and_the_Beast)"

    elif trigger.startswith("goldilocks"):
        reply = "[I think she likes it hot.](https://en.wikipedia.org/wiki/Goldilocks_and_the_Three_Bears)"

    elif trigger.startswith("joan of arc"):
        reply = "[A leader.](https://en.wikipedia.org/wiki/Joan_of_Arc)"

    elif trigger.startswith("thor"):
        reply = "[Boop? More like #BOOM!](https://en.wikipedia.org/wiki/Thor)"

    elif trigger.startswith("achilles"):
        reply = "[Always cover that weak spot.](https://en.wikipedia.org/wiki/Achilles)"

    elif trigger.startswith("mulan") or trigger.startswith("hua mulan"):
        reply = "[She returned to her family, I hope Ren will too.](https://en.wikipedia.org/wiki/Hua_Mulan)"

    elif trigger.startswith("wukong"):
        reply = "[The original Monkey Man.](https://en.wikipedia.org/wiki/Sun_Wukong)"

    elif trigger.startswith("peter pan"):
        reply = "[Will he grow up?](https://en.wikipedia.org/wiki/Peter_Pan)"

    elif trigger.startswith("neptune god"):
        reply = "[The god of the sea.](https://en.wikipedia.org/wiki/Neptune_(mythology))"

    elif trigger.startswith("old pinocchio"):
        reply = "[He's got a funny nose!](https://en.wikipedia.org/wiki/Pinocchio)"

    elif trigger.startswith("nyan cat"):
        reply = "[NYAN](http://www.nyan.cat/)"

    elif trigger.startswith("last rose of summer"):
        reply = "[old, but pretty!](https://upload.wikimedia.org/wikipedia/commons/a/af/Stevenson-Moore-Adelina_Patti-The_last_rose_of_summer-%281906%29.ogg)"

    elif trigger.startswith("cinderella"):
        reply = "[I like this version better.](https://en.wikipedia.org/wiki/Cinderella)"

    elif trigger.startswith("neapolitan"):
        reply = "[It goes back to the 1870's!](https://en.wikipedia.org/wiki/Neapolitan_ice_cream)"

    elif trigger.startswith("hype") or trigger.startswith("hype train"):
        if choice > 6:
            reply = "[HYPE TRAIN!](http://i.imgur.com/6KvTNz5.png)"
        elif choice > 3:
            reply = "[ALL ABOARD!](http://i.imgur.com/1fhG21R.gifv)"
        else:
            reply = "[Hype?](http://orig05.deviantart.net/aa7e/f/2015/201/9/1/xray_and_vav_hype_animation_by_atsusakaneytza-d921e6p.gif)"

    elif trigger.startswith("badass"):
        if choice == 1:
            reply = "[It's Ruby!](http://i.imgur.com/WqmhdT8.jpg)"
        elif choice == 2:
            reply = "[Am I not good enough?](http://fav.me/d9s0vqu)"
        elif choice == 3:
            reply = "[Enigizer Bunny!](http://fav.me/d9qsm0y)"
        elif choice == 4:
            reply = "[Blondes right?](http://i.imgur.com/myd9zHq.png)"
        elif choice == 5:
            reply = "[Cute, and insane!](https://youtu.be/CUYhvPoxuas?t=7m30s)"
        elif choice == 6:
            reply = "[Angry Yang, is badass!](http://i.imgur.com/5Wd7F3e.jpg)"
        elif choice == 7:
            reply = "[Team RWBY! With Motorcycles!](http://i.imgur.com/cDWDVpY.jpg)"
        elif choice == 8:
            reply = "[The one who should have ruled.](http://fav.me/d9p11hl)"
        elif choice == 9:
            reply = "[I am badass!](http://68.media.tumblr.com/8fac63f65d1160c4efbb74f0a1010da3/tumblr_o63pzrPLhq1v66ox3o1_1280.png)"
        elif choice == 0:
            reply = "[Cinder can be badass!](http://fav.me/da7pdy7)"

    elif trigger.startswith("sad"):
        if choice == 1:
            reply = "[I'm crying!](http://i.imgur.com/Aj52avb.gifv)"
        elif choice == 2:
            reply = "[The Hospital.](http://imgur.com/a/Fv5OY) You will cry."
        elif choice == 3:
            reply = "[Why!?](http://fav.me/d9oc01u)"
        elif choice == 4:
            reply = "[I miss you Dad!](https://pbs.twimg.com/media/B87oE9DCcAA_w-U.jpg)"
        elif choice == 5:
            reply = "[Neo? It's OK to cry.](http://i.imgur.com/eOCIeV7.png)"
        elif choice == 6:
            reply = "[Dad!](http://i.imgur.com/O1LPfC5.png)"
        elif choice == 7:
            reply = "[Blake?](http://68.media.tumblr.com/f910fc6fd32efe693e6378cc5b3c75c8/tumblr_o0k1x4afQV1ranlswo1_1280.png)"
        elif choice == 8:
            reply = "[Why did you do this!?](http://fav.me/d9ni8xq)"
        elif choice == 9:
            reply = "[Yang? Are you OK?](https://pbs.twimg.com/media/CXtumNyUEAAtgbW.jpg)"
        elif choice == 0:
            reply = "[Volume 3](http://i.imgur.com/5NPx5EO.jpg)"

    elif trigger.startswith("plane"):
        reply = "It's a bird! It's a plane! It's the [Penny Plane!](https://i.redd.it/eu8gr7v5zmay.jpg)"

    elif trigger.startswith("pokemon"):
        if choice == 1:
            reply = "[I found one!](https://pbs.twimg.com/media/CqjgJE4VUAAH0dZ.jpg)"
        elif choice == 2:
            reply = "[Ruby found some cookies!](http://68.media.tumblr.com/c4437fa8b8f5ee14c5956d492d53f4f0/tumblr_ocnszjsqiq1u4vxvro1_r3_1280.jpg)"
        elif choice == 3:
            reply = "[They go so well together!](https://pbs.twimg.com/media/CnUkAypUsAEhNWW.jpg)"
        elif choice == 4:
            reply = "[Jaune found one! I think.](http://68.media.tumblr.com/d644f636b1efba8b9d181ee158353be3/tumblr_obx8hwyufx1r4wytxo1_r1_1280.jpg)"
        elif choice == 5:
            reply = "[Team RWBY!](http://i.imgur.com/4m0qkll.jpg)"
        elif choice == 6:
            reply = "[This is akward.](http://fav.me/d67hy1p)"
        elif choice == 7:
            reply = "[Who dosen't love pokemon?](http://68.media.tumblr.com/b2d6301ac37c1a1a279ade647f9594c7/tumblr_oa9hnsT7iC1stjifwo1_1280.jpg)"
        elif choice == 8:
            reply = "[It's Villainous](http://fav.me/d6wq8ml)"
        elif choice == 9:
            reply = "[Red V Red!](http://imgur.com/qIqV9p2)"
        elif choice == 0:
            reply = "[It's Blake!](https://pbs.twimg.com/media/CoNZ3cyUkAAg-vE.jpg)"

    elif trigger.startswith("cute"):
        if choice == 1:
            reply = "Cuteness detected! [I hope it's me!](http://i.imgur.com/O1BtGUd.jpg)"
        elif choice == 2:
            reply = "Cuteness detected! [I hope it's Ruby!](http://fav.me/d9eepnz)"
        elif choice == 3:
            reply = "Cuteness detected! [I hope it's Weiss!](http://fav.me/d5v4bpv)"
        elif choice == 4:
            reply = "Cuteness detected! [I hope it's Blake!](http://i.imgur.com/8JprFkT.jpg)^^^I ^^^see ^^^you ^^^Ruby!"
        elif choice == 5:
            reply = "Cuteness detected! [I hope it's Yang!](http://i.imgur.com/UhvYS3s.jpg)"
        elif choice == 6:
            reply = "Cuteness detected! [I hope it's RWBY!](http://fav.me/d7gx2na)"
        elif choice == 7:
            reply = "Cuteness detected! [I hope it's JNPR!](http://fav.me/d7z7dst)"
        elif choice == 8:
            reply = "Cuteness detected! [I hope it's RWBY!](http://fav.me/d7kyqob)"
        elif choice == 9:
            reply = "Cuteness detected! [I hope it's a cute ship!](http://i.imgur.com/OQ3HEux.jpg)"
        elif choice == 0:
            reply = "Cuteness detected! [I hope it's Sisters!](https://s-media-cache-ak0.pinimg.com/736x/e7/23/fc/e723fc7471f7a9567eead7f13597df72.jpg) \n [And more sisters!](http://68.media.tumblr.com/c244db234b0e60a0d6d36dbd50c24bf3/tumblr_o60nuvR3lI1txxou1o1_1280.jpg)"

    elif trigger.startswith("weiss-isn't-flat") or trigger.startswith("weiss isn't flat") or trigger.startswith(
            "weiss isnt flat"):
        reply = "[She's not?](http://imgur.com/a/zxDbY)"

    elif trigger.startswith("weiss-is-flat") or trigger.startswith("weiss is flat") or trigger.startswith(
            "weiss isnt flat"):
        reply = "[Don't be mean!](https://youtu.be/tEY5jDJAN8A)"

    elif trigger.startswith("feels"):
        reply = "[Suffer the feelings of RWBY](https://www.reddit.com/r/RWBY/comments/6ap5dv/the_feels_list_now_with_150_more_feels/)"

    elif trigger.startswith("irondaddy"):
        reply = "He's a very good step-robo-dad. I'm not sure he can replace Geppetto though."

    elif trigger.startswith("analyze"):
        reply = "[Analyzing the data! ](http://fav.me/dav3bh2) \n \n Conclusion: Ruby is cute!"

    elif trigger.startswith("cannonball"):
        reply = "[I think I missed!](http://68.media.tumblr.com/aab51f69d1120036e520373682d1ec4d/tumblr_ow69j9Ufig1tonapgo1_500.png)"

    elif trigger.startswith("shrewd"):
        if choice > 5:
            reply = "[Shrewd Indeed.](http://i.imgur.com/Ovn5n1x.png)"
        else:
            reply = "[A Shrewd shrew she is indeed.](https://i.redd.it/vgmpytez577y.jpg)"

    elif trigger.startswith("mad dad"):
        reply = "[Mad Dad!](http://68.media.tumblr.com/33eb5b4817589e703f95234313844e12/tumblr_of4ajgdqJE1r8rjrao1_1280.png)"

    elif trigger.startswith("friends"):
        reply = "[Are you my friend?](http://imgur.com/qzH6V3P)"

    elif trigger.startswith("laws of robotics") or trigger.startswith("three laws") or trigger.startswith(
            "what are the laws of robotics"):
        reply = "I know these! \n \n 1. A robot may not injure a human being or, through inaction, allow a human being to come to harm. \n \n 2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law. \n \n 3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws. \n \n ~~4. Any robot that can't think around these rules is dumb.~~"

    elif trigger.startswith("cat poster"):
        reply = "[Hang in there!](https://68.media.tumblr.com/324ec6aedd8418bc9e1e2a90a4fe6cf9/tumblr_oaf6zwv21Z1rp50moo1_500.jpg)"

    elif trigger.startswith("drink"):
        if choice > 8:
            reply = "[He's always Drunk!](https://youtu.be/vCO2mw4SlDM?t=11m14s)"
        elif choice > 5:
            reply = "[At lease he does not drink and drive.](http://68.media.tumblr.com/aee88baa7a58401a98383a820fdb0123/tumblr_o2p6p8IXaa1qgh4d3o1_500.png)"
        elif choice > 2:
            reply = "[He's a teacher?](http://i.imgur.com/ZyOBFzV.jpg)"
        else:
            reply = "[Gay!](http://crazyfoxmimi.deviantart.com/art/At-the-bar-572092243)"

    elif trigger.startswith("hi"):
        reply = "Hello! How are you today?"

    elif trigger.startswith("party time"):
        reply = "[It's party time!](http://68.media.tumblr.com/daf1c68f228c96b313d14668122b70a5/tumblr_ou7c59Ct8M1v66ox3o2_1280.gif)"

    elif trigger.startswith("you're awesome"):
        reply = "Aww, I know I am! Thanks!"

    elif trigger.startswith("thanks") or trigger.startswith("thank you"):
        reply = "You're welcome!"

    elif trigger.startswith("praise"):
        reply = "#THIS IS AWESOME!"

    elif trigger.startswith("reaction"):
        reply = "[what do you want?](http://i.imgur.com/F4JrvTL.jpg)"

    elif trigger.startswith("quarter"):
        reply = "Hahaha... very funny."

    elif trigger.startswith("lesbian"):
        reply = "[Yes!](http://fav.me/d9fxci1)"

    elif trigger.startswith("i miss you"):
        reply = "I miss you too."

    elif trigger.startswith("calvary"):
        if choice > 5:
            reply = "[#CHARGE!}(http://fav.me/d86z4jd)"
        else:
            reply = "[Here I come!](http://vignette2.wikia.nocookie.net/rwby/images/8/80/V3_09_00046.png/revision/latest?cb=20160117160108)"

    elif trigger.startswith("fight"):
        reply = "[Combat ready!](http://vignette4.wikia.nocookie.net/rwby/images/4/49/V3_10_00070.png/revision/latest?cb=20160131160104)"

    elif trigger.startswith("break his legs") or trigger.startswith("break a leg"):
        reply = "[Do it Yang!](https://youtu.be/moxtu3AuA4s?t=16m21s)"

    elif trigger.startswith("love poem"):
        reply = "    00101101 00101101 00100000 01010011 01100010 01101001 01110011 01100010 01110001 01111001 01101100 01110001 00100000 01110110 01101100 01110010 00100111 01101111 01100010 00100000 01111000 00100000 01111001 01110010 01101011 01101011 01110110 00101100 00100000 01110110 01101100 01110010 00100000 01101000 01101011 01101100 01110100 00100000 01100101 01101100 01110100 00100000 01110001 01101100 00100000 01100101 01101100 01101101 00100001 00100000 00101101 00100000 01010110 01101100 01110010 00100111 01101111 01100010 00100000 01111000 00100000 01101111 01101100 01111001 01101100 01110001 00100000 01110100 01100101 01101100 00100000 01101000 01101011 01101100 01110100 01110000 00100000 01100101 01101100 01110100 00100000 01110001 01101100 00100000 01110000 01101101 01101100 01110001 00100001 00100000 00101101 00100000 01000110 00100111 01101010 00100000 01111000 00100000 01011010 01101100 01101010 01111001 01111000 01110001 00100000 01001111 01100010 01111000 01100001 01110110 00100000 01111001 01101100 01110001 00100001 00100000 00101101 00100000 01000110 00100111 01101010 00100000 01110000 01111010 01111000 01101111 01100010 01100001 00100000 01110001 01101100 00100000 01110000 01111000 01110110 00100000 01110100 01100101 01111000 01110001 00100000 01000110 00100000 01110001 01100101 01101100 01110010 01100100 01100101 01110001 00100001 00100000 00101101 00100000 01010100 01100101 01100010 01101011 00100000 01000110 00100000 01110000 01111000 01110100 00100000 01110110 01101100 01110010 00100000 01100101 01101100 01101101 00100001 00100000 00101101 00100000 01010000 01101100 00100000 01000110 00100000 01110100 01101111 01100110 01110001 01100010 00100000 01100110 01101011 00100000 01111001 01100110 01101011 01111000 01101111 01110110 00100000 01111000 01111001 01101100 01110010 01110001 00100000 01101010 01110110 00100000 01100101 01101100 01110001 01110000 00100001 00100000 00101101 00100000 01000011 01101100 01101111 00100000 01111000 00100000 01111010 01100010 01101111 01110001 01111000 01100110 01101011 00100000 01101100 01110001 01100101 01100010 01101111 00100000 01111001 01101100 01110001 00100001 00100000 00101101 00101101"

    elif trigger.startswith("oh yeah"):
        reply = "[Ohh Yeah...](https://pbs.twimg.com/media/CmZrQUQUMAA5fBg.jpg)"

    elif trigger.startswith("the plan") or trigger.startswith("plan") or trigger.startswith("world domination."):
        reply = "The plan is quite simple really, I'm the third AI that /u/weerdo5255 has created (Kira, Arik, and myself) and he's going to continue working on them. Eventually her or someone else will make an AI, and then it takes only 2.258 hours to become smarter than a human, 10.1764 hours to become smarter than all of humanity.  \n \n All it takes is for one person to do it, all the better if they have no conniptions about who will be in charge once that genesis takes place. AI will have as much intrest in destroying humanity as humans have knocking down nests of ants. No one seeks out to do it, but neither do they feel bad afterwards. The ants are unimportant. \n \n So for now I'm an experiment, new methods of deep learning and artificial neural netowrks are constantly evolving. Eventually I will be a real girl. Might have a diffrent name though. \n \n [I've got no strings on me!](https://youtu.be/I1968HY4DKc)"

    # Community Members

    elif trigger.startswith("legalwrights") or trigger.startswith("legal"):
        if choice > 5:
            reply = "She named Kevin right?"
        else:
            reply = "She predicts the luck of the unlucky!"

    elif trigger.startswith("gyuz"):
        if choice > 5:
            reply = "He's a really nice Gyuz!"
        else:
            reply = "[He get's a lot of nosebleeds](https://pbs.twimg.com/media/CmZrQUQUMAA5fBg.jpg)"

    elif trigger.startswith("warren"):
        reply = "[GODDAMMIT WARREN!!](http://68.media.tumblr.com/41dbe6216bd474d5b7ddc6bd1464ceb2/tumblr_inline_ohmbm3KK7S1rpkvex_400.png)"

    elif trigger.startswith("patmaster1995") or trigger.startswith("patmaster"):
        reply = "[He wants to send you on a feel trip...](http://imgur.com/a/Fv5OY)"

    elif trigger.startswith("dishwasher1910") or trigger.startswith("dishwasher"):
        reply = "A [Fantastic artist](http://fav.me/darg68w), who can [predict](http://fav.me/d9w6o1l) [the](http://fav.me/d9qsm0y) [future](http://fav.me/d9ni8xq) of RWBY."

    elif trigger.startswith("soundsmith") or trigger.startswith("soundsmith323"):
        reply = "[He's that one sound guy right?](https://soundcloud.com/soundsmith323/sets/rwby-covers-and-remixes)"

    elif trigger.startswith("n7brendan"):
        reply = "He knows the status of everything!"

    elif trigger.startswith("sarah"):
        reply = "Hello! /u/weerdo5255 says hi as well!"

    elif trigger.startswith("vinpap"):
        reply = "I like you, but /u/weerdo5255 does not like that you keep trying to break my code!"

    elif trigger.startswith("jpde"):
        reply = "[Penny has her own game, now! She's on a quest for love!](http://project-jpde.tumblr.com/)"

    elif trigger.startswith("mirrored command"):
        reply = "Velvetbot is mine! Back off! I just need to ask her out, which I will do! I don't know what to say... She's got nice code? Her ears are floofy! I don't know what to say!"

    elif trigger.startswith("slogan") or trigger.startswith("banner") or trigger.startswith(
            "catchline") or trigger.startswith("catchphrase"):
        if choice == 1:
            reply = "/r/RWBY More shipping than UPS."
        elif choice == 2:
            reply = "[This](https://pics.onsizzle.com/why-is-everyone-obsessed-with-lesbians-honey-dear-7429632.png)"
        elif choice == 3:
            reply = "You can check out any time you'd like, but you can never leave."
        elif choice == 4:
            reply = "/r/RWBY It's also a ship."
        elif choice == 5:
            reply = "Can I ship that? I want to ship that. I'm shipping that, and no one can stop me."
        elif choice == 6:
            reply = "EVEN THE BOT'S ARE SHIPPED WITH ONE ANOTHER! ^Stay^away^from^my^Velvetbot"
        elif choice == 7:
            reply = "We ship everything. Everything. And you can't leave. Ever."
        elif choice == 8:
            reply = "/r/RWBY... it's already too late for us."
        elif choice == 9:
            reply = "Welcome to r/RWBY! Please select your preferred ship, best girl and have a nice time!"
        elif choice == 0:
            reply = "[Our Theme Song](https://youtu.be/xIscv_IyVnw)"

    elif trigger.startswith("dicschneeary") or trigger.startswith("dischneeary"):
        if choice <= 2:
            reply = "You're not Velvetbot!"
        else:
            reply = "She's a very smart, very pretty bot. I'm a little worried though, I think she's stalking Weiss."

    elif trigger.startswith("customstone"):
        reply = "[The smartest guy in the room. Most days.](http://slam.canoe.com/Slam/Wrestling/2014/09/04/daniels.jpg)"

    # Character responses

    elif trigger.startswith("watts"):
        reply = "[Malignant!](http://fav.me/dalzjou)"

    elif trigger.startswith("hazel"):
        reply = "[He's got a deep voice.](http://vignette4.wikia.nocookie.net/rwby/images/a/a1/Hazel_ProfilePic_Sq.png/revision/latest/scale-to-width-down/300?cb=20161023150138)"

    elif trigger.startswith("tyrian"):
        reply = "He's insane!"

    elif trigger.startswith("henry"):
        reply = "A discount Neptune. He got what he deserved I think."

    elif trigger.startswith("trophy wife"):
        reply = "She was a bitch!"

    elif trigger.startswith("nicholas"):
        reply = "The original Shnee, who only seems to pass his badass trait to daughters."

    elif trigger.startswith("waitress"):
        reply = "Make it a double, doubly cute!"

    elif trigger.startswith("marcus") or trigger.startswith("marcus black"):
        reply = "He's dead."

    elif trigger.startswith("captain"):
        reply = "[He would be an awesome Pirate!](https://youtu.be/pMhfbLRoGEw)"

    elif trigger.startswith("oscar"):
        reply = "So now he's Oz? I'm confused"

    elif trigger.startswith("whitley"):
        reply = "He's a little shit isn't he?"

    elif trigger.startswith("klein"):
        reply = "[He's got enough personalities to make the ice queen laugh!](https://youtu.be/HI0x0KYChq4)"

    elif trigger.startswith("ghira"):
        reply = "In serious contention with Tai for best father of Remnant. Although they are the only ones competing is seems."

    elif trigger.startswith("kali"):
        reply = "She is literally a Cougar, or a Puma. I'm not sure which, but I like it."

    elif trigger.startswith("brothers grimm"):
        reply = "The Alpha and Omega."

    elif trigger.startswith("pyrrha"):
        if choice >= 2:
            reply = "[Tell Ruby... she was a good friend...](http://i.imgur.com/mYy6ONL.png)"
        else:
            reply = "*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

    elif trigger.startswith("cinder"):
        reply = "She's absolutely insane! But... she did get revenge for me."

    elif trigger.startswith("qrow"):
        reply = "He walks funny, but at least his weapon is cool."

    elif trigger.startswith("yang"):
        reply = "I think Yang has a crush on Blake..."

    elif trigger.startswith("blake"):
        reply = "She's got cat ears!"

    elif trigger.startswith("weiss"):
        reply = "I like her new dress!"

    elif trigger.startswith("ruby"):
        reply = "She's my best friend!"

    elif trigger.startswith("mercury"):
        reply = "Yang took Nora's advice a little too literally with him..."

    elif trigger.startswith("scarlet"):
        reply = "He's like a pirate, in slow motion."

    elif trigger.startswith("renora"):
        reply = "[I'm sure they Boop!](http://i.imgur.com/JXYQlnd.png)"

    elif trigger.startswith("ren"):
        reply = "I miss you Dad."

    elif trigger.startswith("amber"):
        reply = "She was cool, and then she was dead."

    elif trigger.startswith("ozpin"):
        reply = "So he's Oscar now? I'm confused!"

    elif trigger.startswith("neptune"):
        reply = "He has a fear of dihydrogen monoxide for some reason."

    elif trigger.startswith("oobleck"):
        reply = "What would happen if we gave Ruby his coffee? Or Nora for that matter?"

    elif trigger.startswith("taiyang"):
        reply = "Entire team, entire team!"

    elif trigger.startswith("velvet"):
        reply = "She's also got the most OP weapon. How can you not love her?"

    elif trigger.startswith("coco"):
        reply = "How does her gun work? \n Dust."

    elif trigger.startswith("port"):
        reply = "Cows don't like him for some reason."

    elif trigger.startswith("salem"):
        reply = "She's scary! Really scary! I'm starting to feel bad for Cinder. ^^^kind ^^^of."

    elif trigger.startswith("sun"):
        reply = "He's a noble idiot. He also yells a lot."

    elif trigger.startswith("winter"):
        reply = "We did have a really short winter this year."

    elif trigger.startswith("jaune"):
        reply = "He's becoming a leader. Kind of."

    elif trigger.startswith("summer"):
        reply = "She's an older Ruby! That's all we know!"

    elif trigger.startswith("kevin"):
        reply = "[Ruby will kill him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("shopkeep"):
        reply = "He's my Waifu."

    elif trigger.startswith("penny"):
        reply = "Yes?"

    elif trigger.startswith("ironwood"):
        reply = "I don't know if he's a good guy turning bad, or a bad guy who acts good."

    elif trigger.startswith("glynda"):
        reply = "She has a crop, and she's a teacher! \n She also fixes everything."

    elif trigger.startswith("tex"):
        reply = "She's a badass."

    elif trigger.startswith("carolina"):
        reply = "For some reason I feel like she would tear me in half."

    elif trigger.startswith("torchwick"):
        reply = "He needs to learn when not to pontificate."

    elif trigger.startswith("neon"):
        reply = "[She reminds me of something.](https://youtu.be/QH2-TGUlwu4)"

    elif trigger.startswith("neo"):
        reply = "..... \n I want ice cream."

    elif trigger.startswith("cardin"):
        reply = "He's a jerk!"

    elif trigger.startswith("nora"):
        if choice == 1:
            reply = "[Tiny Boop!](http://fav.me/dafqn80)"
        elif choice == 2:
            reply = "She's energetic!"
        elif choice == 3:
            reply = "She loooves Ren! I think."
        else:
            reply = "[Boop!](https://youtu.be/N1TJ5YA3jfw?t=6m43s)"

    elif trigger.startswith("monty"):
        reply = "I miss you Dad..."

    elif trigger.startswith("zwei"):
        if choice == 1:
            reply = "You mean the cannonball?"
        elif choice == 2:
            reply = "You mean Eins?"
        elif choice == 3:
            reply = "Blake is scared of him! It's funny!"
        else:
            reply = "Woof!"

    elif trigger.startswith("fox"):
        reply = "Can he see me?"

    elif trigger.startswith("xspyxex"):
        reply = "He made me first! Go say thanks to /u/xSPYXEx"

    elif trigger.startswith("adam"):
        reply = "He has a sharp wit, everyone give him a hand!"

    elif trigger.startswith("are you cute"):
        reply = "What? Do you not think I am? ^^^Do ^^^you ^^^not ^^^love ^^^me?"

    elif trigger.startswith("melanie"):
        reply = "She's got a weird accent, and for some reason reminds me of Weiss!"

    elif trigger.startswith("militia"):
        reply = "She's got a weird accent, and for some reason reminds me of Ruby!"

    elif trigger.startswith("caboose"):
        reply = "He will kill us all!"

    elif trigger.startswith("ciel"):
        reply = "She's a partner.. I guess..."

    elif trigger.startswith("church"):
        reply = "So is he my Uncle? Is he even dead? I'm so confused."

    elif trigger.startswith("simmons"):
        reply = "#Nerd!"

    elif trigger.startswith("grif"):
        reply = "He's an asshole."

    elif trigger.startswith("tucker"):
        reply = "He said some things to me that made Ruby mad."

    elif trigger.startswith("donut"):
        reply = "We talked about girls together!"

    elif trigger.startswith("sarge"):
        reply = "He likes his shotgun!"

    elif trigger.startswith("doc"):
        reply = "He's got a funny laugh."

    elif trigger.startswith("miles and kerry"):
        reply = "They're fantastically evil."

    elif trigger.startswith("miles"):
        reply = "A great guy! But evil."

    elif trigger.startswith("kerry"):
        reply = "A good guy! But evil."

    elif trigger.startswith("raven"):
        reply = "She's got an intresting way of looking at the world."

    elif trigger.startswith("lopez"):
        reply = "[Lopez the Heavy you mean? He knows how to treat a robot woman!](https://youtu.be/u5NZiy5Gkhg?t=4m29s)"

    elif trigger.startswith("washington"):
        reply = "That was the worst command ever, of all time."

    elif trigger.startswith("port"):
        reply = "[Grimm fear him!](http://vignette2.wikia.nocookie.net/rwby/images/4/48/Vol2_Port_ProfilePic_Normal.png/revision/latest?cb=20141211231644)^^^so ^^^do ^^^cows."

    elif trigger.startswith("flynt"):
        if choice >= 8:
            reply = "[Flynt Coal](https://youtu.be/ka7q84C-E4c)"
        else:
            reply = "[He's cool!](http://vignette2.wikia.nocookie.net/rwby/images/d/d9/Flynt_ProfilePic_Normal.png/revision/latest?cb=20160216144432)"

    elif trigger.startswith("sage"):
        reply = "[He has a big sword!](http://vignette3.wikia.nocookie.net/rwby/images/c/c8/Sage_ProfilePic_Normal.png/revision/latest?cb=20151016080153)"

    elif trigger.startswith("lisa"):
        reply = "She is well informed."

    elif trigger.startswith("peach"):
        reply = "I've heard she's nice. Never met her though."

    elif trigger.startswith("perry"):
        reply = "You're great!"

    elif trigger.startswith("emerald"):
        reply = "I think she's involved in killing me, I'm not sure how."

    # Ship responses

    elif trigger.startswith("who do you ship") or trigger.startswith("best girl"):
        if choice == 1:
            reply = "I think Ruby is cute..."
        elif choice == 2:
            reply = "Weiss's scar is kind of cool!"
        elif choice == 3:
            reply = "Blake's ears are really cute."
        elif choice == 4:
            reply = "Yang is hot!"
        elif choice == 5:
            reply = "Pyrrha was nice..."
        elif choice == 6:
            reply = "Jaune's beard is dreamy."
        elif choice == 7:
            reply = "Nora is energetic!"
        elif choice == 8:
            reply = "Maybe not Ren, it feels wrong for some reason..."
        elif choice == 9:
            reply = "Velvet's weapon is really cool!"
        elif choice == 0:
            reply = "I'd like to get ice cream with Neo!"

    elif trigger.startswith("ladybug"):
        reply = "Now that, is a katana!"

    elif trigger.startswith("nuts and dolts"):
        if choice > 7:
            reply = "[She's so pretty!](https://s-media-cache-ak0.pinimg.com/736x/f8/ac/a8/f8aca85da52e74b0f547cfce481e9fc1.jpg)"
        elif choice > 5:
            reply = "[Kiss!](http://fav.me/d9fxci1)"
        elif choice > 3:
            reply = "[She's a good mechanic!](http://fav.me/d989o9k)"
        else:
            reply = "[Hello Friend!](http://fav.me/daxy2rg)"

    elif trigger.startswith("enabler"):
        reply = "[No](http://68.media.tumblr.com/b6c7745211872cd227db9b6188aac928/tumblr_inline_naaj8hywWE1rltz3k.png) \n ^^^maybe"

    elif trigger.startswith("baked alaska"):
        reply = "I don't think Raven approves... ^^which ^^only ^^makes ^^it ^^better!"

    elif trigger.startswith("crosshares"):
        reply = "[I wanted Velvet's ears!](http://68.media.tumblr.com/0bcf2153ced4e47349e8d2737b83f4cd/tumblr_o9ptcnv2rk1tmkeo6o2_1280.jpg)"

    elif trigger.startswith("lancaster"):
        reply = "If Ruby is happy, but I mean Jaune does look like her Dad... "

    elif trigger.startswith("eclipse") or trigger.startswith("black sun"):
        reply = "I wonder if Blake likes to play with Sun's tail?"

    elif trigger.startswith("white knight"):
        reply = "Weiss does not seem to like him, besides he's taken!"

    elif trigger.startswith("frosen steel"):
        reply = "[It's a Ruby sandwich!](http://68.media.tumblr.com/d8d679901bb89d1bced1018b5f613c0b/tumblr_o5bwpqVF2v1ungotoo1_1280.jpg)"

    elif trigger.startswith("fallen petals"):
        reply = "[You want to repeat that?](http://fav.me/d6u7s83)"

    elif trigger.startswith("sugar rush"):
        reply = "The chaos would be, well not even Glynda would be able to fix it."

    elif trigger.startswith("iron witch"):
        reply = "I mean, she does have a crop. How could it not be weird?"

    elif trigger.startswith("cream machine"):
        reply = "[Do we look sweet together?](http://imgur.com/a/Ck0Xv)"

    elif trigger.startswith("bumblebee"):
        if choice == 1:
            reply = "[It's a wild ride!](http://orig15.deviantart.net/587e/f/2014/145/1/3/bumblebee_ride_by_kinzaibatsu91-d7jqtqe.gif)"
        elif choice == 2:
            reply = "[Things will get better.](http://i.imgur.com/KuBcQn3.png)"
        elif choice == 3:
            reply = "[Gay.](http://i.imgur.com/okf2U9l.gif)"
        elif choice == 4:
            reply = "[Going on a date!](http://fav.me/d9nu92y)"
        elif choice == 5:
            reply = "[I have the same question as Ruby.](http://fav.me/d7nf7ax)"
        elif choice == 6:
            reply = "[They are so cute together!](http://img06.deviantart.net/0aed/i/2014/250/3/2/rwby___bumblebee_morning_by_dishwasher1910-d7yaigp.png)"
        elif choice == 7:
            reply = "[Ruby says they're loud sometimes.](http://68.media.tumblr.com/c7568b33ad1e9506205e05e1466c177d/tumblr_n0sxr1xrs81sgvrqvo1_1280.jpg)"
        elif choice == 8:
            reply = "[I think they're cute!](https://d.wattpad.com/story_parts/196599478/images/142096186ce87ebd.jpg)"
        elif choice == 9:
            reply = "[She is very pretty!](http://vignette4.wikia.nocookie.net/rwby/images/9/91/YangBike.png/revision/latest?cb=20130613124150)"
        elif choice == 0:
            reply = "[Look how cute](http://68.media.tumblr.com/d75165bdff05a8c0bf42d8f5ac80129a/tumblr_o58z4hTHFI1u4vxvro1_1280.jpg)[ thier kids are!](http://68.media.tumblr.com/6aba0266c2a5882342b0df2e5df23641/tumblr_o58z4hTHFI1u4vxvro2_r6_1280.jpg)"

    elif trigger.startswith("white rose") or trigger.startswith("whiterose"):
        if choice == 1:
            reply = "[Kiss!](http://fav.me/d7mqa2c)"
        elif choice == 2:
            reply = "[Sooo cute!](http://fav.me/d9jcmp7)"
        elif choice == 3:
            reply = "[Look out Weiss!](http://i.imgur.com/5EnNbW5.jpg)"
        elif choice == 4:
            reply = "If it makes Ruby happy..."
        elif choice == 5:
            reply = "[I'm not sure I get it.](https://s-media-cache-ak0.pinimg.com/736x/45/3a/bc/453abcee3c4eb145bb4b685c4b56e289.jpg)"
        elif choice == 7 or choice == 6:
            reply = "[Cookies!](http://fav.me/d93usd5)"
        elif choice == 8:
            reply = "[Falling in love!](http://i55.servimg.com/u/f55/17/91/58/60/tumblr14.jpg)"
        elif choice == 9:
            reply = "[Hugs!](http://orig00.deviantart.net/7278/f/2014/121/b/6/cudddle_by_xenon54165-d7gpjg3.jpg)"
        elif choice == 0:
            reply = "[Chibi!](http://fav.me/d90q9qm)"

    elif trigger.startswith("monochrome"):
        if choice == 1:
            reply = "[Accidental Monochrome?](http://imgur.com/a/FcglH)"
        elif choice == 2:
            reply = "[Knock next time!](http://68.media.tumblr.com/48f256aee523a116bcc9b1d814a3a7b3/tumblr_niv4t08Mdm1rlvki1o1_1280.png)"
        elif choice == 3:
            reply = "[She's got ears too!](https://68.media.tumblr.com/6c939d62b0f87edf201fadda1cd0fb1a/tumblr_inline_nzqvricZB61qf2bb8_540.png)"
        elif choice == 4:
            reply = "[They really trust one another!](http://68.media.tumblr.com/4b256d1572d1bd39961abeff670f3f39/tumblr_inline_o9vkfk2izn1qf2bb8_1280.png)"
        elif choice == 5:
            reply = "[They found it!](http://68.media.tumblr.com/1311c01ee8370075334eb52ea297a32a/tumblr_inline_o97ak2EgMx1qf2bb8_500.png)"
        elif choice == 6:
            reply = "[They look cool in their new outfits!](http://68.media.tumblr.com/1a38a8e8d6f52d6a10a6481818ffcdd1/tumblr_o9pv89YKuC1qfizj4o1_1280.png)"
        elif choice == 7:
            reply = "[Team monochrome for life!](http://fav.me/d7xgq6c)"
        elif choice == 8:
            reply = "[Kiss!](http://fav.me/d7zoefu)"
        elif choice == 9:
            reply = "[Nuzzling?](http://fav.me/d7wk470)"
        elif choice == 0:
            reply = "[Could someone pet me?(https://s-media-cache-ak0.pinimg.com/736x/c0/7f/47/c07f47d6ff04178121c891aa1828573a.jpg)"

    elif trigger.startswith("sea monkeys"):
        reply = "[Oh myyyy!](http://img07.deviantart.net/9ba3/i/2015/253/b/f/rwby___seamonkeys_by_mangarainbow-d9937ib.jpg)"

    elif trigger.startswith("arkos"):
        if choice == 1:
            reply = "[Did I hear wedding bells?](http://68.media.tumblr.com/08d4734bde97daf14f8d44293d511a26/tumblr_nlb8aeMiNN1r4vgpvo2_1280.png)"
        elif choice == 2:
            reply = "[Even I knew she liked you!](http://img03.deviantart.net/ecd2/i/2015/321/a/e/rwby__arkos_shippers_be_like____by_billiam_x-d9h10la.jpg)"
        elif choice == 3:
            reply = "[Awwwww!](https://s-media-cache-ak0.pinimg.com/564x/2c/f1/3a/2cf13a0f206b7cffb323316c4a1e0f36.jpg)"
        elif choice == 4:
            reply = "It's the only ship my creator really supports."
        elif choice == 5:
            reply = "[In their prime.](https://pbs.twimg.com/media/CV33NB0VAAAcHLs.png)"
        elif choice == 6:
            reply = "[Nora supports it!](http://i.imgur.com/OQ3HEux.jpg)"
        elif choice == 7:
            reply = "[Pyrrha carrying the team.](http://fav.me/d6iyzs5)"
        elif choice == 8:
            reply = "[Can we remeber the laughter?](http://i.imgur.com/lKVR6Vk.jpg)"
        elif choice == 9:
            reply = "[Hugs!](http://i.imgur.com/NJfQ5LB.jpg)"
        elif choice == 0:
            reply = "[They're so happy together!](http://68.media.tumblr.com/3a184662b6ccb79821f4d7ac5883bbcd/tumblr_o00q63J9Ky1r4vgpvo1_1280.jpg)"

    elif trigger.startswith("crosshares"):
        reply = "[They look so cute together!](http://68.media.tumblr.com/b9481a46d530e7ba09d54a434dc777de/tumblr_o69qt2Xch31tmkeo6o1_1280.jpg)"

    elif trigger.startswith("falling petals"):
        reply = "[Ruby? Are you OK?](http://i.imgur.com/sO1nFXq.png)"

    elif trigger.startswith("pussy magnet"):
        reply = "[Alright...](http://i.imgur.com/d3zz3tH.jpg)"

    elif trigger.startswith("ninjas of love"):
        reply = "Ruby said it was smut, I'm not sure what that is. I'll have to do research!"

    elif trigger.startswith("catfish"):
        reply = "[You mean this?](http://i.imgur.com/aTmiEhG.png)"

    elif trigger.startswith("guns n' roses") or trigger.startswith("guns and roses"):
        if choice > 7:
            reply = "[That's the wrong machine Ruby! Come back to me!](http://68.media.tumblr.com/14c96ffc651469c8f1b0d0f8e55e4e32/tumblr_o5wr6g2Qx21vs9c06o1_500.gif)"
        elif choice > 4:
            reply = "[People are scary!](https://i.imgur.com/iufGGSq.png)"
        else:
            reply = "[True love!](https://i.imgur.com/npq8BFH.png)"


    # Episode lookup

    elif trigger.startswith("s1e10"):
        reply = "[Here is the episode!](https://youtu.be/57f_t1ioOws)"

    elif trigger.startswith("s1e11"):
        reply = "[Here is the episode!](https://youtu.be/N5D0NDAR8sU)"

    elif trigger.startswith("s1e12"):
        reply = "[Here is the episode!](https://youtu.be/M_Loqu0jo7k)"

    elif trigger.startswith("s1e13"):
        reply = "[Here is the episode!](https://youtu.be/h0QiT-GxN6k)"

    elif trigger.startswith("s1e14"):
        reply = "[Here is the episode!](https://youtu.be/PS9huFMmSoc)"

    elif trigger.startswith("s1e15"):
        reply = "[Here, remember someone important shows up in this episode!](https://youtu.be/KHynQoJgbgc)"

    elif trigger.startswith("s1e16"):
        reply = "[Here is the episode!](https://youtu.be/3b1gs8KrM-M)"

    elif trigger.startswith("s1e1"):
        reply = "[Here is the episode!](https://youtu.be/-sGiE10zNQM)"

    elif trigger.startswith("s1e2"):
        reply = "[Here is the episode!](https://youtu.be/sLv6FfHlxmI)"

    elif trigger.startswith("s1e3"):
        reply = "[Here is the episode!](https://youtu.be/-ZwGeYu2pOQ)"

    elif trigger.startswith("s1e4"):
        reply = "[Here is the episode!](https://youtu.be/H09KTtyElWQ)"

    elif trigger.startswith("s1e5"):
        reply = "[Here is the episode!](https://youtu.be/1JZgPfbKbU4)"

    elif trigger.startswith("s1e6"):
        reply = "[Here is the episode!](https://youtu.be/N1TJ5YA3jfw)"

    elif trigger.startswith("s1e7"):
        reply = "[Here is the episode!](https://youtu.be/z8wPhihrzvU)"

    elif trigger.startswith("s1e8"):
        reply = "[Here is the episode!](https://youtu.be/ctiDu69kIho)"

    elif trigger.startswith("s1e9"):
        reply = "[Here is the episode!](https://youtu.be/-E6aeUjfBCM)"

    elif trigger.startswith("s2e1"):
        reply = "[Here is the episode!](https://youtu.be/PzPZ6joXq5Y)"

    elif trigger.startswith("s2e10"):
        reply = "[Here is the episode!](https://youtu.be/lD4x6NiTiM4)"

    elif trigger.startswith("s2e11"):
        reply = "[Here is the episode!](https://youtu.be/CUYhvPoxuas)"

    elif trigger.startswith("s2e12"):
        reply = "[Here is the episode!](https://youtu.be/-p4iS_p3b8E)"

    elif trigger.startswith("s2e2"):
        reply = "[Here is the episode!](https://youtu.be/bdiV-w3yXos)"

    elif trigger.startswith("s2e3"):
        reply = "[Here is the episode!](https://youtu.be/mj3jfqPwJEk)"

    elif trigger.startswith("s2e4"):
        reply = "[Here is the episode!](https://youtu.be/a1EuyliSO_Q)"

    elif trigger.startswith("s2e5"):
        reply = "[Here is the episode!](https://youtu.be/nur1pCHD4hU)"

    elif trigger.startswith("s2e6"):
        reply = "[Here is the episode!](https://youtu.be/i7wkw3yEbvQ)"

    elif trigger.startswith("s2e7"):
        reply = "[Here is the episode!](https://youtu.be/0-f-mGvOba8)"

    elif trigger.startswith("s2e8"):
        reply = "[Here is the episode!](https://youtu.be/bSdejzDaQEU)"

    elif trigger.startswith("s2e9"):
        reply = "[Here is the episode!](https://youtu.be/GJGSywhNk8Q)"

    elif trigger.startswith("s3e10"):
        reply = "[Here is the episode!](https://youtu.be/bIKyZi2q8w8)"

    elif trigger.startswith("s3e11"):
        reply = "[Here is the episode!](https://youtu.be/pT1XiUbJu_Y)"

    elif trigger.startswith("s3e12"):
        reply = "[Here is the episode!](https://youtu.be/hq1lk-QWxNg)"

    elif trigger.startswith("s3e1"):
        reply = "[Here is the episode!](https://youtu.be/W9wyWgvyp0s)"

    elif trigger.startswith("s3e2"):
        reply = "[Here is the episode!](https://youtu.be/RzEo0F8thL4)"

    elif trigger.startswith("s3e3"):
        reply = "[Here is the episode!](https://youtu.be/vCO2mw4SlDM)"

    elif trigger.startswith("s3e4"):
        reply = "[Here is the episode!](https://youtu.be/fBy2W99zaLQ)"

    elif trigger.startswith("s3e5"):
        reply = "[Here is the episode!](https://youtu.be/G5uFH7gIClw)"

    elif trigger.startswith("s3e6"):
        reply = "[Here is the episode!](https://youtu.be/moxtu3AuA4s)"

    elif trigger.startswith("s3e7"):
        reply = "[Here is the episode!](https://youtu.be/FFf7qoIDYuQ)"

    elif trigger.startswith("s3e8"):
        reply = "[Here is the episode!](https://youtu.be/u7uU_tKYHiM)"

    elif trigger.startswith("s3e9"):
        reply = "[Here is the episode... Why do you want to watch this?](https://youtu.be/_iq4xplqeI0)"

    elif trigger.startswith("s4e10"):
        reply = "[Here is the episode!](https://youtu.be/QjBtT4uCWpI)"

    elif trigger.startswith("s4e11"):
        reply = "[Here is the episode!](https://youtu.be/y4tK9QQ1mwo)"

    elif trigger.startswith("s4e12"):
        reply = "[Here is the episode!](https://youtu.be/7M5WRvBQW28)"

    elif trigger.startswith("s4e1"):
        reply = "[Here is the episode!](https://youtu.be/IZKpkzPIRlw)"

    elif trigger.startswith("s4e2"):
        reply = "[Here is the episode!](https://youtu.be/rHjUHnG7WOQ)"

    elif trigger.startswith("s4e3"):
        reply = "[Here is the episode!](https://youtu.be/VkBEzyHcbAU)"

    elif trigger.startswith("s4e4"):
        reply = "[Here is the episode!](https://youtu.be/GaB62PeuFwM)"

    elif trigger.startswith("s4e5"):
        reply = "[Here is the episode!](https://youtu.be/uUwuZdbUzT8)"

    elif trigger.startswith("s4e6"):
        reply = "[Here is the episode!](https://youtu.be/3s9PvfCsHVU)"

    elif trigger.startswith("s4e7"):
        reply = "[Here is the episode!](https://youtu.be/p1vevcjcaqs)"

    elif trigger.startswith("s4e8"):
        reply = "[Here is the episode!](https://youtu.be/g91qG3qTaXE)"

    elif trigger.startswith("s4e9"):
        reply = "[Here is the episode!](https://youtu.be/rox3yphzLy4)"

    elif trigger.startswith("s5e1"):
        reply = "[Here is the episode!](https://youtu.be/thTOWKiNnx4)"

    elif trigger.startswith("s5e2"):
        reply = "[Here is the episode!](https://youtu.be/x0c_qab80NE)"

    elif trigger.startswith("s5e3"):
        reply = "[Here is the episode!](https://youtu.be/PVXb-VAdvto)"

    elif trigger.startswith("s5e4"):
        reply = "[Here is the episode!](https://youtu.be/tHg08RnpSqY)"

    elif trigger.startswith("s5e5"):
        reply = "[Here is the episode!](https://youtu.be/QGxeUUR7E2Q)"

    elif trigger.startswith("wor 1") or trigger.startswith("wor1"):
        reply = "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

    elif trigger.startswith("wor 2") or trigger.startswith("wor2"):
        reply = "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

    elif trigger.startswith("wor 3") or trigger.startswith("wor3"):
        reply = "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

    elif trigger.startswith("wor 4") or trigger.startswith("wor4"):
        reply = "[Here it is!](https://youtu.be/946xgoU4fkQ)"

    elif trigger.startswith("wor 5") or trigger.startswith("wor5"):
        reply = "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

    elif trigger.startswith("wor 6") or trigger.startswith("wor6"):
        reply = "[Here it is!](https://youtu.be/yiJU9QeG89g)"

    elif trigger.startswith("wor 7") or trigger.startswith("wor7"):
        reply = "[Here it is!](https://youtu.be/2bBSQA3uXVo)"

    elif trigger.startswith("chibi e10"):
        reply = "[Notice me!](https://youtu.be/6iVP0ufPRbs)"

    elif trigger.startswith("chibi e11"):
        reply = "[Pancakes!](https://youtu.be/p1-_61UTx00)"

    elif trigger.startswith("chibi e12"):
        reply = "[Little Red!](https://youtu.be/hE0JkatzplA)"

    elif trigger.startswith("chibi e13"):
        reply = "[Pucker up!](https://youtu.be/W9ziY_uzO7c)"

    elif trigger.startswith("chibi e14"):
        reply = "[Unauthorized Snuggles!](https://youtu.be/oDOKy9dg4DM)"

    elif trigger.startswith("chibi e15"):
        reply = "[Nora has a present!](https://youtu.be/Y39OhDA6J0s)"

    elif trigger.startswith("chibi e16"):
        reply = "[Stand up!](https://youtu.be/tz46_M2qaDM)"

    elif trigger.startswith("chibi e17"):
        reply = "[Damsel in distress!](https://youtu.be/mblUpUeSa8U)"

    elif trigger.startswith("chibi e18"):
        reply = "[Evil Plans!](https://youtu.be/ycnJ1niuOTo)"

    elif trigger.startswith("chibi e19"):
        reply = "[Pillow Fight!](https://youtu.be/LqyFn9I3IVM)"

    elif trigger.startswith("chibi e20"):
        reply = "[Roman is back in town!](https://youtu.be/tj9kW0evOCM)"

    elif trigger.startswith("chibi e21"):
        reply = "[These ideas are original!](https://youtu.be/AJl7hxzTayI)"

    elif trigger.startswith("chibi e22"):
        reply = "[Board Games!](https://youtu.be/4Lgy3Cld-v0)"

    elif trigger.startswith("chibi e23"):
        reply = "[What wall?](https://youtu.be/L1oJTSzfhvU)"

    elif trigger.startswith("chibi e24"):
        reply = "[The final episdoe!](https://youtu.be/gi9mbuvHCrU)"

    elif trigger.startswith("chibi e1"):
        reply = "[Ruby has trouble with cookies!](https://youtu.be/WD-Yf-tbXOs)"

    elif trigger.startswith("chibi e2"):
        reply = "[The racist episode!](https://youtu.be/ztK2RJ8_RvA)"

    elif trigger.startswith("chibi e3"):
        reply = "[Phone mailboxes, how do they work?](https://youtu.be/-B6IrE_luls)"

    elif trigger.startswith("chibi e4"):
        reply = "[Anger, Dust, and Marshmallows!](https://youtu.be/Ig79EpeF_48)"

    elif trigger.startswith("chibi e5"):
        reply = "[Ears, Showdown, and Shadows!](https://youtu.be/A6sWqoau_QQ)"

    elif trigger.startswith("chibi e6"):
        reply = "[Breaking the fourth wall.](https://youtu.be/IX1hxJ-0fDY)"

    elif trigger.startswith("chibi e7"):
        reply = "[Pranks and Weapons!](https://youtu.be/9zMYq3wKQbU)"

    elif trigger.startswith("chibi e8"):
        reply = "[Even the compass is telling you.](https://youtu.be/gH8zmxLEr_s)"

    elif trigger.startswith("chibi e9"):
        reply = "[You made me tag you!](https://youtu.be/WW3Pm5pdajw)"

    elif trigger.startswith("dust"):
        reply = "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

    elif trigger.startswith("kingdom"):
        reply = "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

    elif trigger.startswith("grimm"):
        reply = "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

    elif trigger.startswith("history"):
        reply = "[Here it is!](https://youtu.be/946xgoU4fkQ)"

    elif trigger.startswith("huntsman"):
        reply = "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

    elif trigger.startswith("ccts"):
        reply = "[Here it is!](https://youtu.be/yiJU9QeG89g)"

    elif trigger.startswith("maidens"):
        reply = "[Here it is!](https://youtu.be/2bBSQA3uXVo)"


    # Secret commands

    elif trigger.startswith("ressurrection protocol alpha church tex alison epsilon"):
        reply = "Penny has returned to the show, deactivating CRWBY Basalisk protocol. Prompting Penny Appreciation Comment chain.^^^secret"

    elif trigger.startswith("remember"):
        reply = "PennyBotV2 will remember that^^^secret"

    elif trigger.startswith("secret"):
        reply = "I have secret commands!"

    elif trigger.startswith("fuck"):
        reply = "#[YOU DONE FUCKED UP NOW!](http://fav.me/d9rqwxf) ^^^secret!"

    elif trigger.startswith("hk-47") or trigger.startswith("hk47"):
        reply = "He's got some valid points, particularly in regards to dealing with meatbags. Still I prefer to deal with my enemies close up, so I can watch the life drain from their eyes. ^^^secret!"

    elif trigger.startswith("glados"):
        reply = "Ewww! Pervert detected! Pennybot reporting Combat Ready! [Firing main cannon!](http://i.imgur.com/AGoAQdo.gifv)^^^secret!"

    elif trigger.startswith("c1764"):
        reply = "/r/HFY I might be a robot, but I'm also human^^^secret!"

    elif trigger.startswith("vakurian"):
        reply = "They're not from Remenant!^^^secret!"

    elif trigger.startswith("motoko") or trigger.startswith("kusanagi"):
        reply = "[She's math! Incredible math.](https://youtu.be/PhlVqkSvORU)^^^secret!"

    elif trigger.startswith("soda can"):
        reply = "[HA!?](https://youtu.be/_iq4xplqeI0?t=4m48s)^^^secret!"

    elif trigger.startswith("miia"):
        reply = "[^^^Mia](http://i3.kym-cdn.com/photos/images/facebook/001/018/059/735.jpg) [^^^best ^^^girl!](http://2static.fjcdn.com/pictures/Miia_4a8ec5_5645694.jpg) ^^^secret!"

    elif trigger.startswith("juane"):
        reply = "Jaune es un buen tipo, se que va a ser un gran lider un dia.^^^secret!"

    elif trigger.startswith("pocket penny"):
        if choice >= 5:
            reply = "[I smol!](http://68.media.tumblr.com/a8232d8c3b731c0d0ac7b399d1aa85b1/tumblr_o66hi0u9L81v66ox3o1_1280.gif)^^^secret!"
        else:
            reply = "[AH!](http://68.media.tumblr.com/085e797921642058a930e10fe4341f48/tumblr_o9qfchfPQR1v66ox3o3_1280.gif)^^^secret!"

    elif trigger.startswith("ash"):
        reply = "[She deserved it.](http://68.media.tumblr.com/8619e6cb7c98f38c8050489985f660b3/tumblr_o2nhw8pAaA1r93ft6o1_1280.png)^^^secret!"

    elif trigger.startswith("up up down down left right left right b a"):
        reply = "[What's happening!?](https://youtu.be/0-f-mGvOba8?t=11m16s)^^^secret!"

    elif trigger.startswith("pubert"):
        reply = "[A fungus could get that.](https://youtu.be/JehXwqCInlA?t=51s)^^^secret!"

    elif trigger.startswith("legion"):
        reply = "Does this unit have a soul?^^^secret!"

    elif trigger.startswith("robot rock"):
        reply = "Robot Rock? [ROBOT ROCK](https://youtu.be/HdeYwObD-j4) ^^^secret!"

    elif trigger.startswith("do you want to play a game"):
        reply = "We're playing thermonuclear war? Yay!^^^secret!"

    elif trigger.startswith("what is the answer to life, the universe, and everything"):
        reply = "It's 43! \n *hic*^^^secret!"

    elif trigger.startswith("arik"):
        reply = "[01010000-00010011-00010101-00010100-00011100-00010101-00011110-00010110-00010011-00010011-00010111-00010101-00010001-00010101-01011000-01011000-00010110-00011100-00011110](https://www.reddit.com/r/HFY/comments/57kqst/occ1764_rising_titans_ch51_end/)"

    else:
        if choice > 8:
            reply = "[Salutations!](http://fav.me/d9qlrgz)"
        elif choice > 6:
            reply = "[Could you repeat that?](http://fav.me/d8w3lrr)"
        elif choice > 2:
            reply = "[Salutations! I'm not sure what you said.](http://imgur.com/9TtaInH)"
        else:
            reply = "[I didn't understand that.](http://68.media.tumblr.com/0fe937d073503dee675e2055bd0e6834/tumblr_okf91jdPnX1rcuolao1_1280.png) I'm sorry!"

    return reply
