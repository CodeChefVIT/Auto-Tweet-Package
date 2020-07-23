import tweepy
import logging
import time
import json

auth = tweepy.OAuthHandler("consumer id","consumer secret key")

auth.set_access_token("api key","api secret key")

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()    

def following(api):
    logger.info("checking followers list:")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following():
            logger.info("following {}".format(follower.name))
            follower.follow()

def main():
    while 1:
        following(api)
        logger.info("procedding:")
        time.sleep(900)

if __name__=="__main__":
    main()

# stop the bot by pressing "ctrl-c"

