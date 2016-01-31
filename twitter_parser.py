"""
@author: Pranav Harathi
date: 01-30-16

Parses Twitter for recent mentions, retweets, etc. to evaluate online presence of presidential candidates.

Example usage of parser:

1. Search query = "Adele"
from twitter_parser import *
wrapper = new TwitterWrapper(c_key, c_secret, a_token, a_token_secret)
search = wrapper.search("Adele")
# list of tweets
tweet_list = search.tweets


"""

import requests
import json
from requests_oauthlib import OAuth1

"""
Lightweight API wrapper
"""
class TwitterWrapper():

	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret
		self.auth_obj = OAuth1(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

	def get(self, url):
		"""
		Returns Requests object from a get request
		"""
		return requests.get(url, auth=self.auth_obj)

	def search(self, query):
		"""
		Returns Search object
		"""
		return Search(requests.get("https://api.twitter.com/1.1/search/tweets.json?q=" + query, auth=self.auth_obj))

class Search():

	def __init__(self, r_obj):
		self.r_obj = r_obj
		self.tweets = []
		for x in json.loads(self.r_obj.text)["statuses"]:
			tweet = Tweet()
			tweet.dict = x
			tweet.created_at = x["created_at"]
			tweet.id = x["id"]
			tweet.text = x["text"]
			tweet.source = x["source"]
			tweet.in_reply_to_status_id = x["in_reply_to_status_id"]
			tweet.in_reply_to_user_id = x["in_reply_to_user_id"]
			tweet.user = User()
			tweet.user.dict = x["user"]
			tweet.user.id = x["user"]["id"]
			tweet.user.name = x["user"]["name"]
			tweet.user.screen_name = x["user"]["screen_name"]
			tweet.user.location = x["user"]["location"]
			tweet.user.followers_count = x["user"]["followers_count"]
			self.tweets.append(tweet)

class Tweet():

	def __init__(self):
		self.created_at = ""
		self.id = ""
		self.text = ""
		self.source = ""
		self.in_reply_to_status_id = ""
		self.in_reply_to_user_id = ""
		self.user = None
		self.dict = None

	def __repr__(self):
		return unicode(self.text).encode('utf8')

class User():

	def __init__(self):
		self.id = ""
		self.name = ""
		self.screen_name = ""
		self.location = ""
		self.followers_count = 0
		self.dict = None
