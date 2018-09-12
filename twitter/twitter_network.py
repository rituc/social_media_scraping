import tweepy
import pandas as pd

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

class TwitterNetwork():

	def  __init__(self):
		# OAuth process, using the keys and tokens
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		self.api = tweepy.API(auth)



	def twitter_following_list(self, current_set):
		friend_df = pd.DataFrame()
		for screen_name in list(current_set)[3:]:
			frnd_list = self.get_user_friends(screen_name)
			if bool(frnd_list):
				frnd_df = pd.DataFrame({"friend_twitter_handle": frnd_list})
				frnd_df["twitter_handle"] = screen_name
				friend_df = friend_df.append(frnd_df)
				i = i + 1
				print "Row no.", i



	def get_user_friends(self, screen_name):
		twitter_frnd_list = []
		for friend in tweepy.Cursor(self.api.friends, screen_name=screen_name, count=200).items():
			twitter_frnd_list.append(friend.screen_name)
		return twitter_frnd_list