
import praw
import boto3


def reddit_login():
    r = praw.Reddit(client_id='',
                    client_secret='',
                    redirect_uri='http://localhost:8080',
                    refresh_token='',
                    user_agent='Contact /u/weerdo5255 if it has gone rouge.')
    return r


def amazon_login():
    a = boto3.resource('s3', aws_access_key_id='',
                     aws_secret_access_key='')
    return a

