import sqlite3
from src.credentials import twitter_setup


class Tweet:

    """ A simple tweet class for a start"""

    def __init__(self, text, date, user, location, follower_count, verified, retweet_count):
        # todo
        # attributes: text, user, followers, created_at, location(user)
        self.text = text
        self.date = date
        self.user = user
        self.location = location
        self.follower_count = follower_count
        self.verified = verified
        self.retweet_count = retweet_count

    def insert_tweet(self, db):
        conn = sqlite3.connect(db)
        c = conn.cursor()
        print('in insert method')
        with conn:
            c.execute("""INSERT INTO tweets VALUES (:text, :date, :user, :location, 
        :follower_count, :verified, :retweet_count)""",
                      {'text': self.text, 'date': self.date, 'user': self.user,
                       'location': self.location, 'follower_count': self.follower_count,
                       'verified': self.verified, 'retweet_count': self.retweet_count})

            c.execute("SELECT * FROM tweets")
            return c.fetchall()

    def get_count(self):
        api = twitter_setup()
        user = api.get_user(self.user.screen_name)  # self.user is a user object
        return user.followers_count  # I don't know why I have to do this if I can get it from tweet
