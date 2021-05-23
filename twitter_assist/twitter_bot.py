from time import sleep
import tweepy
from secret_keys import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
while True:
    f = open('media/since_id.txt', 'r')
    since_id = int(f.read())
    f.close()
    mentions = api.mentions_timeline(include_entities=False, since_id=since_id)
    print(len(mentions))
    for tweet in reversed(mentions):
        f = open('media/'+tweet.user.screen_name+'.txt', 'a')
        f.write(tweet.created_at.strftime("- %d/%m/%Y %I:%M %p -------------\n"))
        f.write(tweet.text+'\n\n')
        f.close()
    if len(mentions)>0:
        f = open('media/since_id.txt', 'w')
        f.write(mentions[0].id_str)
        f.close()
    sleep(20)