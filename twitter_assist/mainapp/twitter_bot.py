import tweepy
from .secret_keys import *

def download_file(twitterid , filepath):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    f = open(filepath, 'w')
    mentions = api.mentions_timeline(include_entities=False, count=200)
    for tweet in reversed(mentions):
        if tweet.user.screen_name == twitterid:
            f.write(tweet.created_at.strftime("- %d/%m/%Y %I:%M %p -------------\n"))
            f.write(tweet.text+'\n\n')
    f.close()
    