if __name__ == "__main__":
    from src.utils import *

    conn = create_db('twitter_data.db')  # change db name
    c = conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS tweets (
            text TEXT,
            date TEXT,
            tweet_language TEXT,
            retweet_count INTEGER,
            favorite_count INTEGER,
            tweet_id TEXT,
            followers_count INTEGER,
            friends_count INTEGER,
            location TEXT,
            user_id TEXT,
            user_lang TEXT,
            geo_enabled NUMERIC,
            verified NUMERIC,
            user_location TEXT
            )""")
    print("table created")

    api = twitter_setup()
    print('api setup done')
    listener = TweetStreamListener()
    stream = tweepy.Stream(api.auth, listener=listener)
    stream.filter(track=['day zero water', 'water crisis cape', 'rain cape day zero', 'cape town drought'])
