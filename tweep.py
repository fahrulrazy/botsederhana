# tweep.py
import tweepy

#I prepared this class for simplicity. Fill in details and use it.
class Tweet:
    #My Twitter consumer key
    consumer_key='Jj6wgCvliZhHdpFbXxkl937Dn'
    #My consumer secret
    consumer_secret='W0N8IcQqrOYYPcJPJQlVLyVc3efcGRcoOs826MCApXH00y2hI3'
    #My access token
    access_token='108912006-YS9hYivbERIZzcNpugqXX7OFcPXr4DnFryLR0er3'
    #My access token secret
    access_token_secret='LRVFnGbZYGT4y0VISJ8Eza99GVoQA7ocqpFAfSTM4oimC'

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.handle = tweepy.API(self.auth)

    def hitme(self,str):
        self.handle.update_status(str)
        print 'sukses nge-twit :)'
