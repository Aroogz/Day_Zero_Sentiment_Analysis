# Twitter App access keys for @user
import tweepy


# Consume:
CONSUMER_KEY    = '1m6d5DLHkGO9gwmPnENrAUcTt'
CONSUMER_SECRET = '13523Tr36vpVQqGcjAO0eaEcnXbd3EU99wNv5mKjcDITiJm8Nz'

# Access:
ACCESS_TOKEN  = '141239888-SWgYb06yxEbkyaBae9aIJ5Ri0ueFrm0U00xolyhe'
ACCESS_SECRET = 'tFuRQo781MD9VPV15ieH0QbvRjOTgE2McSTa7FWrgLXiC'


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
