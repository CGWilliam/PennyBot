# PennyBot V2 Reddit Comment Response System

_The Return of PennyBot._

PennyBot is a comment parsing and response bot that has been primarily developed to operate on the /r/rwby subreddit. 
The program utilizes PRAW to access reddit and allow for the easier parsing of reddit data. 

Currently, PennyBot has several response types: 

* Any subreddit post that included the keyword 'Penny' will initiate a comment. 
* Any new comment in the subreddit that includes the keyword PennyBot, (command) will prompt a response from the bot. 
* The Pennybot thoughts command will access the AI model that is contained and accessed through the Brain.py file. 

The Brain.py file is not set to run, due to the difficulties with the operation of theano based AI calculations. The requirements being extensive, and it being only a small portion of the program the AI behavior is mimicked by having the program on systems capapble of running the AI file generate 500 sentences which are then called on at random. This replicates the behavior without the system dependencies.

For testing purposes the .obot file needs to be modified with OAuth information for the login of whatever account will comment on reddit. 

Please ensure that you test on an appropriate subreddit! (I.E. /r/test) 

Credit to the creator of the original PennyBot https://www.reddit.com/user/xSPYXEx