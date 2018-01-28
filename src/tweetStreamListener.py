from tweepy.streaming import StreamListener
import json
from src.tweet import Tweet
from src.credentials import twitter_setup


class TweetStreamListener(StreamListener):

    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:

            # make it json
            tweet = json.loads(data)
            print("tweet converted")

            # filter
            if not tweet['retweeted'] and 'RT @' not in tweet['text']:
                # get user via tweepy so we can get their no of followers
                api = twitter_setup()
                user_profile = api.get_user(tweet['user']['screen_name'])
                print("about to create tweet instance")
                # create tweet instance with data
                tweet_data = Tweet(
                    str(tweet['text'].encode('utf-8')),
                    tweet['created_at'],
                    tweet['user']['screen_name'],
                    tweet['user']['location'],
                    user_profile.followers_count,
                    tweet['user']['verified'],
                    tweet['retweet_count'])  # fill remaining parameter
                print("tweet instance created")
                tweet_data.insert_tweet('test.db')
                print("success")

        except Exception as e:
            print(e)
            print('after ex')
            pass

        return True

