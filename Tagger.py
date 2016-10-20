import time
import sqlite3

__author__ = 'C.G.William / Weerdo5255'

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'
def replytag(trigger, posturl, title, time):

    trigger = trigger.replace("tag", "")
    trigger = trigger.replace(" ", "")

    print(trigger)

    db = sqlite3.connect("tag.db")
    db.text_factory = str
    cursor = db.cursor()
    cursor.execute('INSERT INTO Tags VALUES (?, ?, ?, ?)',
                   (trigger, posturl, title, int(time)))
    db.commit()

    reply = "This post is tagged with, " + trigger

    return reply

def internaltag(trigger, posturl, title, time):
    print(trigger)

    db = sqlite3.connect("tag.db")
    db.text_factory = str
    cursor = db.cursor()
    cursor.execute('INSERT INTO Tags VALUES (?, ?, ?, ?)',
                   (trigger, posturl, title, int(time)))
    db.commit()

def tagcollect():
    db = sqlite3.connect("tag.db")
    db.text_factory = str
    cursor = db.cursor()
    onedayback = int(time.time())
    oneweekback = (int(time.time())) - 604800

    try:
        cursor.execute('SELECT * FROM tags WHERE datetime between (?) and (?) ORDER BY trigger ASC', (oneweekback, onedayback))

        outstring = "|Tag|URL|\n|:--|:--|\n"

        for row in cursor:
            outstring = outstring + "|" + str(row[0]) + " | [" + str(row[2]) + "]" + "(" + str(row[1]) +")" + " |\n"

    except:
        print("ERROR!")

    db.close()
    return outstring

