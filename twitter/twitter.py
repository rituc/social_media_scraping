from application_only_auth import Client
import urllib
import urllib2
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

TWITTER_INFO_BASE_URL = "https://api.twitter.com/1.1/users/show.json?screen_name="

def main():
	Twitter()

class Twitter():
	def __init__(self):
		self.client = Client(CONSUMER_KEY, CONSUMER_SECRET)

	def get_twitter_info(self, screen_name):
		info = {}
		if (len(screen_name) > 0):
			api_url = TWITTER_INFO_BASE_URL + screen_name
			try:
				data = self.client.request(api_url)
				info = {"twitter_handle": data["screen_name"],
								"description": data["description"],
								"favourites_count": data["favourites_count"],
								"followers_count": data["followers_count"],
								"friends_count": data["friends_count"],
								"statuses_count": data["statuses_count"]
								}
			except Exception as err:
				print err
			return info

		def get_tData(keyword):
			tweets = []
			url = 'http://search.twitter.com/search.json'
			data = {'q': keyword, 'lang': 'en', 'result_type': 'recent'}
			params = urllib.urlencode(data)
			try:
				req = urllib2.Request(url, params)
				response = urllib2.urlopen(req)
				jsonData = json.load(response)
				tweets = []
				for item in jsonData['results']:
					tweets.append(item['text'])
				return tweets
			except urllib2.URLError, e:
				print "error"
			return tweets

if __name__ == "__main__":
	main()
