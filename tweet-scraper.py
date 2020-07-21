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
	since_id = 0
	public_tweets = api.user_timeline(screen_name = handle)
	while True:		
		for tweet in public_tweets:
		    print(tweet.text)
		    tweets.append(tweet.text)
		    if(tweet.id > since_id):
		    	since_id = tweet.id
		time.sleep(10) #10 minutes
		public_tweets = api.user_timeline(screen_name = handle, since_id = since_id)

def authenticate():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

def runapp():
	app.run(host = '0.0.0.0', port = 5010)

if __name__ == '__main__':	

	tweets = []

	# based on a quick skim of the doco around authentication, I feel there may be a better way to do this. But at the moment I believe I'm limited by Tweepy.
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

		#while True: #keep the main thread awake so that I can exit using Ctrl-C until I have another solution
		#	time.sleep(0.5)

		thread1.join()
		thread2.join()

	except: #catching all exceptions here just so that the program exits cleanly
		print 'Something went wrong!!'
