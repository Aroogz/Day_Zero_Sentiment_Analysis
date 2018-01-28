if __name__ == "__main__":
    import sqlite3
    import tweepy
    from src.credentials import twitter_setup
    from src.tweetStreamListener import TweetStreamListener
    # from .credentials import *
    # from .tweetStreamListener import TweetStreamListener

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # c.execute("DROP TABLE tweets")
    c.execute("""
            CREATE TABLE IF NOT EXISTS tweets (
            text TEXT,
            date TEXT,
            user INTEGER,
            location TEXT,
            follower_count INTEGER,
            verified NUMERIC,
            retweet_count INTEGER
            )""")
    print("table created")

    # Run the stream
    api = twitter_setup()
    print('api set up done')
    l = TweetStreamListener()
    stream = tweepy.Stream(api.auth, l)

    # Filter the stream for these keywords. Add whatever you want here!
    stream.filter(track=['day zero water', 'water crisis cape', 'rain cape day zero', 'cape town drought'])
