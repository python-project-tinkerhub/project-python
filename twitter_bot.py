import tweepy
from secrets import *

twitterid = 'AchyuthMohan2'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

f = open(twitterid+'.txt', 'w')

for tweet in tweepy.Cursor(api.mentions_timeline).items():
    if tweet.user.screen_name == twitterid:
        f.write(tweet.text+'\n\n')

f.close()