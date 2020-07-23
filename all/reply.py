import tweepy
import logging
import json

auth = tweepy.OAuthHandler("consumer id","consumer secret key")

auth.set_access_token("api key","api secret key")

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()  

def check(api,keywords,since_id):
	logger.info("fetching mentions:")
	new_since_id = since_id
	for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
		new = max(tweet.id,new)
		if tweet.in_reply_to_status_id is not None:
                continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info("answering to {}".format(tweet.user.name))
            if not tweet.user.following():
            	tweet.user.follow()

    		api.update_status(status="please contact us through direct message",in_reply_to_status_id=tweet.id,)

	return new_since_id

def main():
	since_id = 1
	while 1:
		since_id = check(api,["world","time"],since_id)
		logger.info("fetching..")
		time.sleep(900)


if __name__=="__main__":
	main()

#stop the bot by pressing "ctrl-c"