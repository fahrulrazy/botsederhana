# tweep.py
import tweepy

#I prepared this class for simplicity. Fill in details and use it.
class Tweet:
    #My Twitter consumer key
    consumer_key='consumer key'
    #My consumer secret
    consumer_secret='consumer secret'
    #My access token
    access_token='access token'
    #My access token secret
    access_token_secret='access token secret'

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.handle = tweepy.API(self.auth)

    def hitme(self,str):
        self.handle.update_status(str)
        print 'sukses nge-twit :)'
