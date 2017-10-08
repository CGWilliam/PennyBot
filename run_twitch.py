import csv
import random
import socket
import sqlite3
import time
import re
import sys
import commands
from obot import twitch_host, twitch_port, twitch_password, twitch_channel, twitch_user


def openSocket():
    ts = socket.socket()
    ts.connect((twitch_host,twitch_port))
    ts.send("PASS {}\r\n".format(twitch_password).encode("utf-8"))
    ts.send("NICK {}\r\n".format(twitch_user).encode("utf-8"))
    ts.send("JOIN {}\r\n".format(twitch_channel).encode("utf-8"))
    return ts


def joinChannel(s):
    readbuffer = ""
    loadChat = True
    while loadChat:
        readbuffer = readbuffer + s.recv(1024).decode("utf-8")
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()
        for commentline in temp:
            print(commentline)
            loadChat = doneLoad(commentline)
    postMessage(s, "Pennybot has joined chat")


def doneLoad(comment):
    if ("End of /NAMES list" in comment):
        return False
    else:
        return True


def postMessage(s, message):
    mTemp = "PRIVMSG " + twitch_channel + " :" + message
    s.sendall((mTemp + "\r\n").encode('utf-8'))
    print("Sent: " + mTemp)


def load_ai_phrase():
    with open('thoughts.txt', 'r') as f:
        aiphrase = [line.strip() for line in f]
    return aiphrase


def load_random_phrase():
    with open('Commands.txt', 'r', encoding='utf8') as f:
        randomcmd = [line.strip() for line in f]
    return randomcmd


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


def proccess_comments(current):
    # Add to the suggestion text file
    if current.startswith("suggestion"):
        reply = "[You can make Suggestions here!](https://goo.gl/forms/NKGPxdJzxh87dsjv2) \n \n Pennybot has saved this comment as well! \n \n ^^^^^^^^/u/weerdo5255 "

    # Access the AI Function
    elif current.startswith("thoughts"):
        thoughtstring = " "
        randomnum = (random.randint(0, 3))
        try:
            x = 0
            phrases = commands.load_ai_phrase()
            while (x <= randomnum):
                thoughtstring = thoughtstring + random.choice(phrases) + "\n"
                x += 1
        except:
            thoughtstring = ("I don't have any thoughts at the moment.")

        reply = thoughtstring

    elif current.startswith("shutdown"):
        author = twitch_user()
        print(author)
        if author == "weerdo5255":
            print("Emergency Shutdown Initiated! At: " + time.asctime(time.localtime(
                time.time())))
            sys.exit()
        else:
            reply = "You are not Pyrrha!"

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
        reply = commands.penny_commands(current)

    return reply


s = openSocket()
joinChannel(s)
readBuffer = ""
while True:
    current = s.recv(1024).decode("utf-8")
    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    if current == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", current).group(0)  # return the entire match
        message = CHAT_MSG.sub("", current)
        print(username + ": " + message)
        response = []
        current = message
        if "pennybot," in current:
            lookingfor = "pennybot,"
            # Remove pennybot from the string start scanning for response
            indexcount = current.index(lookingfor) + 9
            current = current.lstrip(current[:indexcount])
            current = current.strip()
            replied = True
            txtreply = proccess_comments(current)
            response.append(txtreply)
        elif "pb," in current:
            lookingfor = "pb,"
            # Remove pb from the string start scanning for response
            indexcount = current.index(lookingfor) + 3
            current = current.lstrip(current[:indexcount])
            current = current.strip()
            replied = True
            txtreply = proccess_comments(current)
            response.append(txtreply)

        string = ""
        for x in response:
            string += x + " \n \n"
            string = string.replace("[", '')
            string = string.replace("]", ' ')
            string = string.replace(")", " ")
            string = string.replace("(", '')
            postMessage(s, string)
            print(
                "Found a Penny comment at: " + time.asctime(
                    time.localtime(time.time())) + " \nI responded with:" + "\n" + string)
            db = sqlite3.connect("Tdatabase.db")
            db.text_factory = str
            cursor = db.cursor()
            cursor.execute('INSERT INTO Tdatabase VALUES (?, ?, ?, ?, ?, ?)',
                           (str(twitch_channel), int(time.time()), str(username), str(message), str(current), str(string)))
            db.commit()
        time.sleep(1 / (20/30))