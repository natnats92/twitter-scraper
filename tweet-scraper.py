import tweepy	
import pdb
import sys
from flask import Flask
from flask import jsonify
import threading
import time

app = Flask(__name__)
@app.route('/tweets/', methods = ['GET'])
def print_tweets():
    return jsonify(tweets)

def fetchtweets():
	while True:
		public_tweets = api.user_timeline(handle)
		for tweet in public_tweets:
		    print(tweet.text)
		    tweets.append(tweet.text)
		time.sleep(10)

def authenticate():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

def runapp():
	app.run(host = '127.0.0.1', port = 5002)

if __name__ == '__main__':	

	tweets = []

	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''

	if len(sys.argv) == 1:
		print('Please provide a Twitter handle in the format python tweet-scraper.py <handle>')
		exit()

	handle = sys.argv[1]

	try:

		f = open('credentials.txt', 'r')
		if f.mode == 'r':
			lines = f.readlines()
			consumer_key = lines[0].split('=')[1].replace('\n','')
			consumer_secret = lines[1].split('=')[1].replace('\n','')
			access_token = lines[2].split('=')[1].replace('\n','')
			access_token_secret = lines[3].split('=')[1].replace('\n','')
		f.close()

		api = authenticate()

		thread1 = threading.Thread(target = fetchtweets)
		thread2 = threading.Thread(target = runapp)
		thread1.daemon = True
		thread2.daemon = True
		thread1.start()
		thread2.start()

		while True: #keep the main thread awake so that I can exit using Ctrl-C until I have another solution
			time.sleep(0.5)

		thread1.join()
		thread2.join()

	except:
		print 'Something went wrong!! To begin with, please check your API credentials.'
