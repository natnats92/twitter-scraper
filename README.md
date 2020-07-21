# twitter-scraper

# Monitor a Twitter account and check for new tweets every 10 minutes. The Twitter handle is to be provided as a command line argument by the user starting the program in the format 'python twitter-scraper.py <handle>'. The text from the new tweets will be output to stdout.

# Add your developer credentials to credentials.txt and place it in the same folder as tweet-scraper.py. https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a

# Build docker - Run 'sudo docker build -t twitter_scraper:latest .'

# Run docker - Run 'sudo docker run -p 5010:5010 --rm -ti twitter_scraper:latest python tweet-scraper.py <handle>'

# Stop docker - Run 'sudo docker ps' and get the CONTAINER ID. Then run 'sudo docker stop <CONTAINER ID>'.

# View Tweet dump at http://0.0.0.0:5010/tweets/

