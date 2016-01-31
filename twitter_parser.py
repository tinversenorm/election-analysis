"""
@author: Pranav Harathi
date: 01-30-16

Parses Twitter for recent mentions, retweets, etc. to evaluate online presence of presidential candidates.
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

	def get(url):
		"""
		Returns Requests object from a get request
		"""
		return requests.get(url, auth=auth)

	def search(query):
		"""
		Returns Requests object specifically for a search query
		"""
		return requests.get("https://api.twitter.com/1.1/search/tweets.json?q=" + query, auth=auth)








# usernames: realDonaldTrump, tedcruz, BernieSanders, HillaryClinton
