import sqlite3
import json
import tweepy
from tweepy.streaming import StreamListener
from src.credentials import *


# API setup
def twitter_setup():
    """
    Utility function to setup the Twitter's API

    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # Return API with authentication:
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    return api


def insert_tweet(tweet, db, table):
    """ inserts tweet object in the table "table" in the database "db".

    keyword arguments:
    tweet -- tweet object
    db    -- the database
    table -- table in database "db"
    """
    print('in insert method')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    with conn:
        c.execute("""INSERT INTO """ + table + """ VALUES (:text, :date, :tweet_language, :retweet_count, 
                                                    :favorite_count, :tweet_id, :followers_count, :friends_count, 
                                                    :location, :user_id, :user_language, :geo_enabled, 
                                                    :verified, :user_location)""",
                  {'text': tweet['text'], 'date': tweet['created_at'], 'tweet_language': tweet['lang'],
                   'retweet_count': tweet['retweet_count'], 'favorite_count': tweet['favorite_count'],
                   'tweet_id': tweet['id_str'], 'followers_count': tweet['user']['followers_count'],
                   'friends_count': tweet['user']['friends_count'], 'location': tweet['user']['location'],
                   'user_id': tweet['user']['id_str'], 'user_language': tweet['user']['lang'],
                   'geo_enabled': tweet['user']['geo_enabled'], 'verified': tweet['user']['verified'],
                   'user_location': tweet['user']['location']})


def create_db(db):
    """ create a database connection to a SQLite database """

    try:
        conn = sqlite3.connect(db)
        return conn
    except Exception as e:
        print(e)


def create_table():
    pass


class TweetStreamListener(StreamListener):

    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        try:
            # process and insert tweet in database

            # convert to python dictionary
            tweet = json.loads(data)

            # filter retweets and insert into table in database
            if not tweet['retweeted'] and 'RT @' not in tweet['text']:
                print("inserting tweet to data base")
                insert_tweet(tweet, 'twitter_data.db', 'tweets')
                print("success inserting tweet")

        except Exception as e:
            print(e)
            print('in exception')
            pass

        return True

