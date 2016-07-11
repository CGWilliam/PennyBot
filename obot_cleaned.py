__author__ = 'C.G.William / Weerdo5255' \

'I can be contacted at weerdo5255@gmail.com'
'Youre free to use the below code, on the stipulation that you give me credit and share with others!'
'My website is www.cgwilliam.com'

# The information here needs to be filled out for each application that wants to connect to reddit. For security reasons sections of the code have been ommited.

app_id = ''
app_secret = ''
app_uri = 'http://127.0.0.1:65010/authorize_callback'
app_ua = 'A comment response triggered by certain requests made in user comments. contact /u/weerdo5255 if she has gone rouge.'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = ''
app_refresh = ''

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r
