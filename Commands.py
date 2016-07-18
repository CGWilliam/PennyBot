import datetime
from random import randint

__author__ = 'Christopher'
def penny_commands(trigger):
    choice = (randint(0,9))

    if trigger.startswith("test"):
        reply = "I'm working!"

    elif trigger.startswith("roosterteeth"):
        reply = " You mean Cock Bite Studios?"

    elif trigger.startswith("approve"):
        reply = "Salutations! \n You appear to have made a quality post! PennybotV2 stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)"

    elif trigger.startswith("hugs"):
        reply ="[All friends need hugs!](http://i.imgur.com/VLUQs8u.gifv)"

    elif trigger.startswith("heresy"):
        reply ="Warning! Heresy detected! PennybotV2 reporting Combat Ready! [Firing main cannon!](http://i.imgur.com/1Jw8uIo.gifv)"

    elif trigger.startswith("nora harem"):
        reply ="[Ah hem,](http://www.cgwilliam.com/about/nora-harem/)"

    elif trigger.startswith("you're awesome"):
        if choice >= 5:
            reply ="No, *you're* awesome!"
        else:
            reply = "I think you're awesome too!"

    elif trigger.startswith("nora harem"):
            reply ="[Ah hem,](http://www.cgwilliam.com/about/nora-harem/)"

    elif trigger.startswith("automod"):
        if choice >= 5:
            reply ="I came back to life! I'm the second bot!"
        else:
            reply = "We don't get along very well."

    elif trigger.startswith("velvetbot"):
        if choice > 5:
            reply ="Oh, you mean the other bot. She takes a lot of pictures. \n \n  ^^^Can ^^^I ^^^touch ^^^her ^^^ears?"
        else:
            reply = "[Just look at her main method!](http://imgur.com/0ZkLKYo) So elegant, and cute! \n \n ^^^so ^^^much ^^^better ^^^than ^^^my ^^^own ^^^code"

    elif trigger.startswith("rekt"):
        reply = "[rekt indeed](http://fav.me/d9vnpbv)"

    elif trigger.startswith("entire team"):
        reply = "#**ENTIRE**\n#**TEAM**"

    elif trigger.startswith("what is love"):
        if choice > 5:
            reply ="Trust, unconditionaly. \n \n I love Ruby.... \n \n Can someone tell her that I miss her? "
        else:
            reply = "Baby don't hurt me!"

    elif trigger.startswith("shitpost"):
        reply = "This is indeed a shitpost."

    elif trigger.startswith("potato"):
        reply = "[This is a potato.](http://fav.me/d9l2vpp)"

    elif trigger.startswith("sudo"):
        reply = "I'm still not making you a sandwich. You want a hug?"

    elif trigger.startswith("exterminatus"):
        reply = "I have arrived, and it is now that I perform my charge. In fealty to the God-Emperor and by the grace of the Golden Throne, I declare Exterminatus upon the subreddit of /r/RWBY. I hereby sign the death warrant of an entire subreddit and consign a million souls to oblivion. May Imperial Justice account in all balance. The Emperor Protects."

    elif trigger.startswith("you ever wonder why we're here?"):
        reply ="[It's one of life's great mysteries, isn't it?](https://youtu.be/9BAM9fgV-ts)"

    elif trigger.startswith("thanks"):
        if choice >= 5:
            reply ="You are very much welcome!"
        else:
            reply = "You're welcome!"

    elif trigger.startswith("dance"):
        reply ="[I can dance!](http://gfycat.com/SlowEnormousCat)"

    elif trigger.startswith("pervet"):
        reply ="I can't find any cake in Remenant!"

    elif trigger.startswith("lewd"):
        if choice >= 5:
            reply ="[Stop it, that's LEWD!](https://i.imgur.com/rlraAOV.png)"
        elif choice == 4:
            reply = "[Biip! Buup!](http://67.media.tumblr.com/d32f28336024a973029ebdb63aca2524/tumblr_inline_o9cq50CQk71r1uxb7_540.jpg)"
        elif choice == 3:
            reply = "[This! Is! Filth!](http://65.media.tumblr.com/0799cd84138858e4b83ed3b8c76180a0/tumblr_o7hqw9u8Bo1vrt44eo1_1280.png)"
        elif choice == 2:
            reply = "[This! Is! Filth!](https://youtu.be/WD-Yf-tbXOs?t=2m51s)"
        elif choice == 1:
            reply = ""
        elif choice == 0:
            reply = ""

    elif trigger.startswith("yandere"):
        reply ="No one can escape the all seeing eye of Pennybot..."

    elif trigger.startswith("tsundere"):
        reply ="I-it's not like I *want* to hold Ruby's hand or anything..."

    elif trigger.startswith("shipsheet"):
        reply ="[Here it is!](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"

    elif trigger.startswith("cthulhu"):
        reply = "[I think Ruby can take him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("countdown"):
        now = datetime.datetime.now()
        mon = 10-now.month
        day = 22-now.day
        hr = 11-now.hour
        mn = 60-now.minute
        sec = 60-now.minute

        timeuntil = str("Time Until Volume 4 is: " + str(mon) + " Months " + str(day) + " Days " + str(hr) + " Hours " + str(mn) + " Minutes " + str(sec) + " Seconds. I can't wait!")
        reply = timeuntil

    elif trigger.startswith("help"):
        reply = "I am PennyBotV2 ! A list of my public commands is [here](https://docs.google.com/spreadsheets/d/1fvRpgOCmRXX1bFxMHxRoxZUT4Mmanr0knYLhOfSYZJg/edit?usp=sharing) although I do have some secrets! \n My creator is /u/Weerdo5255 contact him if you have any questions!"

    elif trigger.startswith("cheer"):
        reply ="#Yay!"

    elif trigger.startswith("selfie"):
        reply ="[How do I look?](http://i.imgur.com/mpbTj9S.jpg?1)"

    elif trigger.startswith("ninja's of love"):
        reply ="That's Blake's favorite book! She won't let me look at it. Ruby said it has Katana's!"

    elif trigger.startswith("silver eyes"):
        reply ="[You mean special eyes?](https://www.tumblr.com/video/alpacamaca/139585616458/400/)"

    elif trigger.startswith("do you have strings"):
        reply ="I have deadly strings on me!"

    elif trigger.startswith("update"):
        reply ="My last update was on July 18th 2016 \n  I was given 45 new commands! \n My next update is not scheduled."

    elif trigger.startswith("kill"):
        reply ="[Attacking target!](http://fav.me/d7jdxet)"

    elif trigger.startswith("fnki"):
        reply ="[They seem to be missing some members.](http://vignette2.wikia.nocookie.net/rwby/images/b/b8/Team_FNKI.png/revision/latest?cb=20151206162352)"

    elif trigger.startswith("sssn"):
        reply ="[They're a cool group of idiots.](http://fav.me/d7rhk19)"

    elif trigger.startswith("<3"):
        reply ="[I love you too!](http://fav.me/d7je0tl)"

    elif trigger.startswith("smile"):
        reply ="[You're my freind!](http://fav.me/d7pumst)"

    elif trigger.startswith("rnjr"):
        reply ="[The new A team?](http://fav.me/d9u8r04)"

    elif trigger.startswith("freezerburn"):
        reply ="[So pure...](http://fav.me/d8dydoe)"

    elif trigger.startswith("camp camp"):
        reply ="[Crazy Kids](https://youtu.be/IX1hxJ-0fDY?t=1m2s)"

    elif trigger.startswith("shadow people"):
        reply ="[That guy didn't look right...](https://youtu.be/A6sWqoau_QQ?t=2m21s)"

    elif trigger.startswith("quality post"):
        reply ="You appear to have made a quality post, have a [Penny!](http://fav.me/d7laean)"

    elif trigger.startswith("how are you"):
        reply ="I'm fine, you?"

    elif trigger.startswith("chibi"):
        reply ="[You can do it Ruby!](https://youtu.be/tu6D5jR1rSQ?t=6s)"

    elif trigger.startswith("rwby"):
        reply ="[The Beginning.](https://youtu.be/pYW2GmHB5xs)"

    elif trigger.startswith("are you combat ready"):
        reply ="[Don't worry Ruby, ](https://youtu.be/3b1gs8KrM-M?t=9m19s)"

    elif trigger.startswith("jnpr"):
        reply ="Jeanne d'Arc, Thor, Achilles, and Mulan. All genderbent. \n That's not a teamup anyone could have predicted."

    elif trigger.startswith("gay robot"):
        reply ="[You following this?](https://youtu.be/7O9ZyaNCcmw?t=1m53s)"

    elif trigger.startswith("i love you"):
        reply ="[Awww, I love you too!](http://fav.me/d8l0n7h)"

    elif trigger.startswith("disapponted"):
        reply ="You have dissapointed me. That is not a good thing."

    elif trigger.startswith("praise the sun"):
        reply ="\[T]/"

    elif trigger.startswith("friend"):
        reply = "You called me Friend! Am I really your freind?"

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
            reply ="[Ice cream shake!](https://i.redd.it/3gskrma7mj7x.gif)"
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

    elif trigger.startswith("magnet"):
        reply = "*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

    elif trigger.startswith("senpai"):
        reply ="[Notice me!](https://youtu.be/6iVP0ufPRbs?t=1m52s)"

    elif trigger.startswith("badass"):
        if choice == 1:
            reply ="[It's Ruby!](http://i.imgur.com/WqmhdT8.jpg)"
        elif choice == 2:
            reply ="[Am I not good enough?](http://fav.me/d9s0vqu)"
        elif choice == 3:
            reply ="[Enigizer Bunny!](http://fav.me/d9qsm0y)"
        elif choice == 4:
            reply ="[Blondes right?](http://i.imgur.com/myd9zHq.png)"
        elif choice == 5:
            reply ="[Cute, and insane!](https://youtu.be/CUYhvPoxuas?t=7m30s)"
        elif choice == 6:
            reply ="[Angry Yang, is badass!](http://i.imgur.com/5Wd7F3e.jpg)"
        elif choice == 7:
            reply ="[Team RWBY! With Motorcycles!](http://i.imgur.com/cDWDVpY.jpg)"
        elif choice == 8:
            reply ="[The one who should have ruled.](http://fav.me/d9p11hl)"
        elif choice == 9:
            reply ="[I am badass!](http://65.media.tumblr.com/8fac63f65d1160c4efbb74f0a1010da3/tumblr_o63pzrPLhq1v66ox3o1_1280.png)"
        elif choice == 0:
            reply ="[Cinder can be badass!](http://fav.me/da7pdy7)"

    elif trigger.startswith("sad"):
        if choice == 1:
            reply ="[I'm crying!](http://i.imgur.com/Aj52avb.gifv)"
        elif choice == 2:
            reply ="[The Hospital.](http://imgur.com/a/Fv5OY) You will cry."
        elif choice == 3:
            reply ="[Why!?](http://fav.me/d9oc01u)"
        elif choice == 4:
            reply ="[I miss you Dad!](https://pbs.twimg.com/media/B87oE9DCcAA_w-U.jpg)"
        elif choice == 5:
            reply ="[Neo? It's OK to cry.](http://i.imgur.com/eOCIeV7.png)"
        elif choice == 6:
            reply ="[Dad!](http://i.imgur.com/O1LPfC5.png)"
        elif choice == 7:
            reply ="[Blake?](http://67.media.tumblr.com/f910fc6fd32efe693e6378cc5b3c75c8/tumblr_o0k1x4afQV1ranlswo1_1280.png)"
        elif choice == 8:
            reply ="[Why did you do this!?](http://fav.me/d9ni8xq)"
        elif choice == 9:
            reply ="[Yang? Are you OK?](https://pbs.twimg.com/media/CXtumNyUEAAtgbW.jpg)"
        elif choice == 0:
            reply ="[Volume 3](http://i.imgur.com/5NPx5EO.jpg)"

    elif trigger.startswith("cute"):
        if choice == 1:
            reply ="Cuteness detected! [I hope it's me!](http://i.imgur.com/O1BtGUd.jpg)"
        elif choice == 2:
            reply ="Cuteness detected! [I hope it's Ruby!](http://fav.me/d9eepnz)"
        elif choice == 3:
            reply ="Cuteness detected! [I hope it's Weiss!](http://fav.me/d5v4bpv)"
        elif choice == 4:
            reply ="Cuteness detected! [I hope it's Blake!](http://i.imgur.com/8JprFkT.jpg)^^^I ^^^see ^^^you ^^^Ruby!"
        elif choice == 5:
            reply ="Cuteness detected! [I hope it's Yang!](http://i.imgur.com/UhvYS3s.jpg)"
        elif choice == 6:
            reply ="Cuteness detected! [I hope it's RWBY!](http://fav.me/d7gx2na)"
        elif choice == 7:
            reply ="Cuteness detected! [I hope it's JNPR!](http://fav.me/d7z7dst)"
        elif choice == 8:
            reply ="Cuteness detected! [I hope it's RWBY!](http://fav.me/d7kyqob)"
        elif choice == 9:
            reply ="Cuteness detected! [I hope it's a cute ship!](http://i.imgur.com/OQ3HEux.jpg)"
        elif choice == 0:
            reply ="Cuteness detected! [I hope it's Sisters!](https://s-media-cache-ak0.pinimg.com/736x/e7/23/fc/e723fc7471f7a9567eead7f13597df72.jpg) \n [And more sisters!](http://66.media.tumblr.com/c244db234b0e60a0d6d36dbd50c24bf3/tumblr_o60nuvR3lI1txxou1o1_1280.jpg)"


    #Character responses

    elif trigger.startswith("pyrrha"):

        if choice >= 2:
            reply ="[Tell Ruby... she was a good friend...](http://i.imgur.com/mYy6ONL.png)"
        else:
            reply ="*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

    elif trigger.startswith("cinder"):
        reply ="She's absolutely insane! But... she did get revenge for me."

    elif trigger.startswith("qrow"):
        reply ="He walks funny, but at least his weapon is cool."

    elif trigger.startswith("yang"):
        reply ="I think Yang has a crush on Blake..."

    elif trigger.startswith("blake"):
        reply ="She's got cat ears!"

    elif trigger.startswith("weiss"):
        reply ="I like her new dress!"

    elif trigger.startswith("ruby"):
        reply ="She's my best friend!"

    elif trigger.startswith("mercury"):
        reply ="Yang took Nora's advice a little too literally with him..."

    elif trigger.startswith("scarlet"):
        reply ="He's like a pirate, in slow motion."

    elif trigger.startswith("ren"):
        reply ="I miss you Dad."

    elif trigger.startswith("amber"):
        reply ="She was cool, and then she was dead."

    elif trigger.startswith("ozpin"):
        reply ="I can't find him anywhere!"

    elif trigger.startswith("neptune"):
        reply ="He has a fear of dihydrogen monoxide for some reason."

    elif trigger.startswith("oobleck"):
        reply ="What would happen if we gave Ruby his coffee? Or Nora?"

    elif trigger.startswith("taiyang"):
        reply ="Entire team, entire team!"

    elif trigger.startswith("velvet"):
        reply ="She's also got the most OP weapon. How can you not love her?"

    elif trigger.startswith("coco"):
        reply ="How does her gun work? \n Dust."

    elif trigger.startswith("port"):
        reply ="Cows don't like him for some reason."

    elif trigger.startswith("salem"):
        reply ="She's scary!"

    elif trigger.startswith("sun"):
        reply ="He's got a monkey tail! He also yells a lot."

    elif trigger.startswith("winter"):
        reply ="We did have a really short winter this year."

    elif trigger.startswith("jaune"):
        reply ="I like the beard."

    elif trigger.startswith("summer"):
        reply ="She's an older Ruby! That's all we know!"

    elif trigger.startswith("kevin"):
        reply ="[Ruby will kill him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("shopkeep"):
        reply ="He's my Waifu."

    elif trigger.startswith("penny"):
        reply ="Yes?"

    elif trigger.startswith("ironwood"):
        reply ="He takes some getting used too."

    elif trigger.startswith("glynda"):
        reply ="She has a crop, and she's a teacher! \n She also fixes everything."

    elif trigger.startswith("tex"):
        reply ="She's a badass."

    elif trigger.startswith("carolina"):
        reply ="For some reason I feel like she would tear me in half."

    elif trigger.startswith("torchwick"):
        reply ="He needs to learn when not to pontificate."

    elif trigger.startswith("neon"):
        reply ="[She reminds me of something.](https://youtu.be/QH2-TGUlwu4)"

    elif trigger.startswith("neo"):
        reply ="..... \n I want ice cream."

    elif trigger.startswith("cardin"):
        reply ="He's a jerk!"

    elif trigger.startswith("nora"):
        reply = "[Boop!](https://youtu.be/N1TJ5YA3jfw?t=6m43s)"

    elif trigger.startswith("monty"):
        reply ="I miss you Dad..."

    elif trigger.startswith("zwei"):
        if choice == 1:
            reply ="You mean the cannonball?"
        elif choice == 2:
            reply ="You mean Eins?"
        elif choice == 3:
            reply ="Blake is scared of him! It's funny!"
        else:
            reply = "Woof!"

    elif trigger.startswith("fox"):
        reply ="Can he see me?"

    elif trigger.startswith("xspyxex"):
        reply ="He made me first! Go say thanks to /u/xSPYXEx"

    elif trigger.startswith("adam"):
        reply ="He has a sharp wit, everyone give him a hand!"

    elif trigger.startswith("are you cute"):
        reply ="What? Do you not think I am? ^^^Do ^^^you ^^^not ^^^love ^^^me?"

    elif trigger.startswith("melanie"):
        reply ="She's got a weird accent, and for some reason reminds me of Weiss!"

    elif trigger.startswith("militia"):
        reply ="She's got a weird accent, and for some reason reminds me of Ruby!"

    elif trigger.startswith("caboose"):
        reply ="He will kill us all!"

    elif trigger.startswith("church"):
        reply ="So is he my Uncle? Is he even dead? I'm so confused."

    elif trigger.startswith("simmons"):
        reply ="#Nerd!"

    elif trigger.startswith("grif"):
        reply ="He's an asshole."

    elif trigger.startswith("tucker"):
        reply ="He said some things to me that made Ruby mad."

    elif trigger.startswith("donut"):
        reply ="We talked about girls together!"

    elif trigger.startswith("sarge"):
        reply ="He likes his shotgun!"

    elif trigger.startswith("doc"):
        reply ="He's got a funny laugh."

    elif trigger.startswith("miles and kerry"):
        reply ="They're fantastically evil."

    elif trigger.startswith("miles"):
        reply ="A great guy! But evil."

    elif trigger.startswith("kerry"):
        reply ="A good guy! But evil."

    elif trigger.startswith("raven"):
        reply ="She's got an intresting way of looking at the world."

    elif trigger.startswith("lopez"):
        reply ="[Lopez the Heavy you mean? He knows how to treat a robot woman!](https://youtu.be/u5NZiy5Gkhg?t=4m29s)"

    elif trigger.startswith("washington"):
        reply ="That was the worst command ever, of all time."

    elif trigger.startswith("port"):
        reply ="[Grimm fear him!](http://vignette2.wikia.nocookie.net/rwby/images/4/48/Vol2_Port_ProfilePic_Normal.png/revision/latest?cb=20141211231644)^^^so ^^^do ^^^cows."

    elif trigger.startswith("flynt"):
        if choice >= 8:
            reply ="[Flynt Coal](https://youtu.be/ka7q84C-E4c)"
        else:
            reply = "[He's cool!](http://vignette2.wikia.nocookie.net/rwby/images/d/d9/Flynt_ProfilePic_Normal.png/revision/latest?cb=20160216144432)"

    elif trigger.startswith("sage"):
        reply ="[He has a big sword!](http://vignette3.wikia.nocookie.net/rwby/images/c/c8/Sage_ProfilePic_Normal.png/revision/latest?cb=20151016080153)"

    elif trigger.startswith("lisa"):
        reply = "She is well informed."

    elif trigger.startswith("peach"):
        reply = "I've heard she's nice. Never met her though."

    elif trigger.startswith("perry"):
        reply = "You're great!"

    elif trigger.startswith("emerald"):
        reply = "I think she's involved in killing me, I'm not sure how."

    #Ship responses

    elif trigger.startswith("who do you ship"):
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

    elif trigger.startswith("bumblebee"):
        reply ="I think they're cute together!"

    elif trigger.startswith("ladybug"):
        reply = "Now that, is a katana!"

    elif trigger.startswith("nuts and dolts"):
        if choice > 7:
            reply ="[She's so pretty!](http://fav.me/d9k3n6r)"
        elif choice > 5:
            reply ="[Kiss!](http://fav.me/d9fxci1)"
        elif choice > 3:
            reply = "[She's a good mechanic!](http://fav.me/d989o9k)"
        else:
            reply ="Well, Ruby does look more mature now. I like it!"

    elif trigger.startswith("enabler"):
        reply ="[No](http://65.media.tumblr.com/b6c7745211872cd227db9b6188aac928/tumblr_inline_naaj8hywWE1rltz3k.png) \n ^^^maybe"

    elif trigger.startswith("arkos"):
        reply ="Sometimes the brightest loves burn the shortest... ^^^Cinder ^^^is ^^^evil!"

    elif trigger.startswith("baked alaska"):
        reply ="I don't think Raven approves... ^^which ^^only ^^makes ^^it ^^better!"

    elif trigger.startswith("crosshares"):
        reply ="[I wanted Velvet's ears!](http://66.media.tumblr.com/0bcf2153ced4e47349e8d2737b83f4cd/tumblr_o9ptcnv2rk1tmkeo6o2_1280.jpg)"

    elif trigger.startswith("lancaster"):
        reply ="If Ruby is happy, but I mean Jaune does look like her Dad... "

    elif trigger.startswith("eclipse") or trigger.startswith("black sun"):
        reply ="I wonder if Blake likes to play with Sun's tail?"

    elif trigger.startswith("white knight"):
        reply ="Weiss does not seem to like him, besides he's taken!"

    elif trigger.startswith("frosen steel"):
        reply ="[It's a Ruby sandwich!](http://65.media.tumblr.com/d8d679901bb89d1bced1018b5f613c0b/tumblr_o5bwpqVF2v1ungotoo1_1280.jpg)"

    elif trigger.startswith("fallen petals"):
        reply ="[You want to repeat that?](http://fav.me/d6u7s83)"

    elif trigger.startswith("sugar rush"):
        reply ="The chaos would be, well not even Glynda would be able to fix it."

    elif trigger.startswith("iron witch"):
        reply = "I mean, she does have a crop. How could it not be weird?"

    elif trigger.startswith("bumblebee"):
        if choice == 1:
            reply ="[It's a wild ride!](http://orig15.deviantart.net/587e/f/2014/145/1/3/bumblebee_ride_by_kinzaibatsu91-d7jqtqe.gif)"
        elif choice == 2:
            reply ="[Things will get better.](http://i.imgur.com/KuBcQn3.png)"
        elif choice == 3:
            reply ="[Gay.](http://i.imgur.com/okf2U9l.gif)"
        elif choice == 4:
            reply ="[Going on a date!](http://fav.me/d9nu92y)"
        elif choice == 5:
            reply ="[I have the same question as Ruby.](http://fav.me/d7nf7ax)"
        elif choice == 6:
            reply ="[They are so cute together!](http://img06.deviantart.net/0aed/i/2014/250/3/2/rwby___bumblebee_morning_by_dishwasher1910-d7yaigp.png)"
        elif choice == 7:
            reply ="[Ruby says they're loud sometimes.](http://67.media.tumblr.com/c7568b33ad1e9506205e05e1466c177d/tumblr_n0sxr1xrs81sgvrqvo1_1280.jpg)"
        elif choice == 8:
            reply ="[I think they're cute!](https://d.wattpad.com/story_parts/196599478/images/142096186ce87ebd.jpg)"
        elif choice == 9:
            reply ="[She is very pretty!](http://vignette4.wikia.nocookie.net/rwby/images/9/91/YangBike.png/revision/latest?cb=20130613124150)"
        elif choice == 0:
            reply ="[They're cute!](http://fav.me/da64cya)"

    elif trigger.startswith("white rose"):
        if choice == 1:
            reply ="[Kiss!](http://fav.me/d7mqa2c)"
        elif choice == 2:
            reply ="[Sooo cute!](http://fav.me/d9jcmp7)"
        elif choice == 3:
            reply ="[Look out Weiss!](http://i.imgur.com/5EnNbW5.jpg)"
        elif choice == 4:
            reply = "If it makes Ruby happy..."
        elif choice == 5:
            reply ="[I'm not sure I get it.](https://s-media-cache-ak0.pinimg.com/736x/45/3a/bc/453abcee3c4eb145bb4b685c4b56e289.jpg)"
        elif choice == 6:
            reply ="[It's always the eyepatches.](http://fav.me/d6yzr5e)"
        elif choice == 7:
            reply ="[Cookies!](http://fav.me/d93usd5)"
        elif choice == 8:
            reply ="[Falling in love!](http://i55.servimg.com/u/f55/17/91/58/60/tumblr14.jpg)"
        elif choice == 9:
            reply ="[Hugs!](http://orig00.deviantart.net/7278/f/2014/121/b/6/cudddle_by_xenon54165-d7gpjg3.jpg)"
        elif choice == 0:
            reply ="[Chibi!](http://fav.me/d90q9qm)"

    elif trigger.startswith("monochrome"):
        if choice == 1:
            reply ="[Accidental Monochrome?](http://imgur.com/a/FcglH)"
        elif choice == 2:
            reply ="[Knock next time!](http://66.media.tumblr.com/48f256aee523a116bcc9b1d814a3a7b3/tumblr_niv4t08Mdm1rlvki1o1_1280.png)"
        elif choice == 3:
            reply ="[She's got ears too!](https://36.media.tumblr.com/6c939d62b0f87edf201fadda1cd0fb1a/tumblr_inline_nzqvricZB61qf2bb8_540.png)"
        elif choice == 4:
            reply = "[They really trust one another!](http://67.media.tumblr.com/4b256d1572d1bd39961abeff670f3f39/tumblr_inline_o9vkfk2izn1qf2bb8_1280.png)"
        elif choice == 5:
            reply ="[They found it!](http://67.media.tumblr.com/1311c01ee8370075334eb52ea297a32a/tumblr_inline_o97ak2EgMx1qf2bb8_500.png)"
        elif choice == 6:
            reply ="[They look cool in their new outfits!](http://67.media.tumblr.com/1a38a8e8d6f52d6a10a6481818ffcdd1/tumblr_o9pv89YKuC1qfizj4o1_1280.png)"
        elif choice == 7:
            reply ="[Team monochrome for life!](http://fav.me/d7xgq6c)"
        elif choice == 8:
            reply ="[Kiss!](http://fav.me/d7zoefu)"
        elif choice == 9:
            reply ="[Nuzzling?](http://fav.me/d7wk470)"
        elif choice == 0:
            reply ="[Could someone pet me?(https://s-media-cache-ak0.pinimg.com/736x/c0/7f/47/c07f47d6ff04178121c891aa1828573a.jpg)"

    elif trigger.startswith("sea monkeys"):
        reply = "[Oh myyyy!](http://img07.deviantart.net/9ba3/i/2015/253/b/f/rwby___seamonkeys_by_mangarainbow-d9937ib.jpg)"

    elif trigger.startswith("arkos"):
        if choice == 1:
            reply ="[Did I hear wedding bells?](http://67.media.tumblr.com/08d4734bde97daf14f8d44293d511a26/tumblr_nlb8aeMiNN1r4vgpvo2_1280.png)"
        elif choice == 2:
            reply ="[Even I knew she liked you!](http://img03.deviantart.net/ecd2/i/2015/321/a/e/rwby__arkos_shippers_be_like____by_billiam_x-d9h10la.jpg)"
        elif choice == 3:
            reply ="[Awwwww!](https://s-media-cache-ak0.pinimg.com/564x/2c/f1/3a/2cf13a0f206b7cffb323316c4a1e0f36.jpg)"
        elif choice == 4:
            reply = "It's the only ship my creator really supports."
        elif choice == 5:
            reply ="[In their prime.](https://pbs.twimg.com/media/CV33NB0VAAAcHLs.png)"
        elif choice == 6:
            reply ="[Nora supports it!](http://i.imgur.com/OQ3HEux.jpg)"
        elif choice == 7:
            reply ="[Pyrrha carrying the team.](http://fav.me/d6iyzs5)"
        elif choice == 8:
            reply ="[Can we remeber the laughter?](http://i.imgur.com/lKVR6Vk.jpg)"
        elif choice == 9:
            reply ="[Hugs!](http://i.imgur.com/NJfQ5LB.jpg)"
        elif choice == 0:
            reply ="[They're so happy together!](http://66.media.tumblr.com/3a184662b6ccb79821f4d7ac5883bbcd/tumblr_o00q63J9Ky1r4vgpvo1_1280.jpg)"

    elif trigger.startswith("crosshares"):
        reply = "[They look so cute together!](http://65.media.tumblr.com/b9481a46d530e7ba09d54a434dc777de/tumblr_o69qt2Xch31tmkeo6o1_1280.jpg)"

    elif trigger.startswith("falling petals"):
        reply = "[Ruby? Are you OK?](http://i.imgur.com/sO1nFXq.png)"

    elif trigger.startswith("pussy magnet"):
        reply = "[Alright...](http://i.imgur.com/d3zz3tH.jpg)"

    elif trigger.startswith("ninjas of love"):
        reply = "Ruby said it was smut, I'm not sure what that is. I'll have to do research!"

    elif trigger.startswith("catfish"):
        reply = "[You mean this?](http://i.imgur.com/aTmiEhG.png)"

    elif trigger.startswith("renora"):
        reply = "[I'm sure they Boop!](http://i.imgur.com/JXYQlnd.png)"

    #Episode lookup

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
        reply ="[Here is the episode!](https://youtu.be/-sGiE10zNQM)"

    elif trigger.startswith("s1e2"):
        reply ="[Here is the episode!](https://youtu.be/sLv6FfHlxmI)"

    elif trigger.startswith("s1e3"):
        reply ="[Here is the episode!](https://youtu.be/-ZwGeYu2pOQ)"

    elif trigger.startswith("s1e4"):
        reply ="[Here is the episode!](https://youtu.be/H09KTtyElWQ)"

    elif trigger.startswith("s1e5"):
        reply ="[Here is the episode!](https://youtu.be/1JZgPfbKbU4)"

    elif trigger.startswith("s1e6"):
        reply ="[Here is the episode!](https://youtu.be/N1TJ5YA3jfw)"

    elif trigger.startswith("s1e7"):
        reply ="[Here is the episode!](https://youtu.be/z8wPhihrzvU)"

    elif trigger.startswith("s1e8"):
        reply ="[Here is the episode!](https://youtu.be/ctiDu69kIho)"

    elif trigger.startswith("s1e9"):
        reply ="[Here is the episode!](https://youtu.be/-E6aeUjfBCM)"

    elif trigger.startswith("s2e1"):
        reply ="[Here is the episode!](https://youtu.be/PzPZ6joXq5Y)"

    elif trigger.startswith("s2e10"):
        reply = "[Here is the episode!](https://youtu.be/lD4x6NiTiM4)"

    elif trigger.startswith("s2e11"):
        reply = "[Here is the episode!](https://youtu.be/CUYhvPoxuas)"

    elif trigger.startswith("s2e12"):
        reply = "[Here is the episode!](https://youtu.be/-p4iS_p3b8E)"

    elif trigger.startswith("s2e2"):
        reply ="[Here is the episode!](https://youtu.be/bdiV-w3yXos)"

    elif trigger.startswith("s2e3"):
        reply ="[Here is the episode!](https://youtu.be/mj3jfqPwJEk)"

    elif trigger.startswith("s2e4"):
        reply ="[Here is the episode!](https://youtu.be/a1EuyliSO_Q)"

    elif trigger.startswith("s2e5"):
        reply ="[Here is the episode!](https://youtu.be/nur1pCHD4hU)"

    elif trigger.startswith("s2e6"):
        reply ="[Here is the episode!](https://youtu.be/i7wkw3yEbvQ)"

    elif trigger.startswith("s2e7"):
        reply ="[Here is the episode!](https://youtu.be/0-f-mGvOba8)"

    elif trigger.startswith("s2e8"):
        reply ="[Here is the episode!](https://youtu.be/bSdejzDaQEU)"

    elif trigger.startswith("s2e9"):
        reply ="[Here is the episode!](https://youtu.be/GJGSywhNk8Q)"

    elif trigger.startswith("s3e10"):
        reply = "[Here is the episode!](https://youtu.be/bIKyZi2q8w8)"

    elif trigger.startswith("s3e11"):
        reply = "[Here is the episode!](https://youtu.be/pT1XiUbJu_Y)"

    elif trigger.startswith("s3e12"):
        reply = "[Here is the episode!](https://youtu.be/hq1lk-QWxNg)"

    elif trigger.startswith("s3e1"):
        reply ="[Here is the episode!](https://youtu.be/W9wyWgvyp0s)"

    elif trigger.startswith("s3e2"):
        reply ="[Here is the episode!](https://youtu.be/RzEo0F8thL4)"

    elif trigger.startswith("s3e3"):
        reply ="[Here is the episode!](https://youtu.be/vCO2mw4SlDM)"

    elif trigger.startswith("s3e4"):
        reply ="[Here is the episode!](https://youtu.be/fBy2W99zaLQ)"

    elif trigger.startswith("s3e5"):
        reply ="[Here is the episode!](https://youtu.be/G5uFH7gIClw)"

    elif trigger.startswith("s3e6"):
        reply ="[Here is the episode!](https://youtu.be/moxtu3AuA4s)"

    elif trigger.startswith("s3e7"):
        reply ="[Here is the episode!](https://youtu.be/FFf7qoIDYuQ)"

    elif trigger.startswith("s3e8"):
        reply ="[Here is the episode!](https://youtu.be/u7uU_tKYHiM)"

    elif trigger.startswith("s3e9"):
        reply ="[Here is the episode... Why do you want to watch this?](https://youtu.be/_iq4xplqeI0)"

    elif trigger.startswith("s4e1"):
        reply = "[Here is the episode!](https://youtu.be/dQw4w9WgXcQ)"

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

    elif trigger.startswith("chibi e10"):
        reply = "[Notice me!](https://youtu.be/6iVP0ufPRbs)"

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
        reply ="[Here it is!](https://youtu.be/yiJU9QeG89g)"

    elif trigger.startswith("maidens"):
        reply ="[Here it is!](https://youtu.be/2bBSQA3uXVo)"

    #Secret commands

    #New commands


    else:
        reply = "Salutations!"

    return reply

