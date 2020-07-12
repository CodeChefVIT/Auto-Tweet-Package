import tweepy

auth = tweepy.OAuthHandler("consumer id","consumer secret key")

auth.set_access_token("api key","api secret key")

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (api.verify_credentials()):
	print('ok')
else:
	print('not ok')

timeline = api.home_timeline()

for tweet in timeline:
	print(f"{tweet.user.name} said {tweet.text}")
	break

s =  input("enter the text to tweet: ")

api.update_status(s)

# user = api.get_user("NASA")

# print(user.description)

# for x in user.followers():
# 	print(x.name)
# 	break

follow = input("enter the account to follow: ")
api.create_friendship(follow)

# api.update_profile(description="Second Year Computer Science Student") # for updating the profile description of personal account

to_like_tweets = api.home_timeline(count=1)
to_like_tweet = to_like_tweets[0]
print(f"{to_like_tweet.author.name} last tweet {to_like_tweet.id} is liked")
api.create_favorite(tweet.id) # for liking a recent tweet

user_id = input("enter the twitter name to block: ")
if (api.create_block(user_id)):
	print(user_id + " succesfully blocked")
else:
	mood =1
	for x in api.blocks():
		if (x==user_id):
			print(user_id+" already blocked")
			mood=2
			break
	if (mood==2):
		print(user_id+" does not exist")

#now for finding the trending topics worldwide or location 

trending = api.trends_place(1)
for trend in trending[0]["trends"]:
	print(trend["name"])




