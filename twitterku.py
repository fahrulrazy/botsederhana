#twitterku.py

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

import telepot, time
from nltk.chat.eliza import eliza_chatbot
from tweep import Tweet

# create tweet client
tweet_client = Tweet()
is_chatting = False

def handle(pesan):
    global is_chatting
    global tweet_client
    chat_id = pesan['chat']['id']
    command = pesan['text']
    print 'Got command: %s' % command

    if command == '/timeline' and not is_chatting:
        bot.sendMessage(chat_id, '\n'.join([message.text for message in tweet_client.handle.home_timeline()]))
    elif command.split('=')[0] == '/tweet' and not is_chatting:
        try:
            tweet_client.hitme(command.split('=')[1] + ' #clara')
            bot.sendMessage(chat_id, 'twit anda sukses dikirim')
        except:
            bot.sendMessage(chat_id, 'ada kesalahan')
    elif command == '/chat':
        is_chatting = True

        bot.sendMessage(chat_id, 'Hi I\'m Clara. Fachrul Razy\'s Personal Assistant. How can I help you?')
    elif command == '/stopchat':
        is_chatting = False
        bot.sendMessage(chat_id, 'See you! long kiss')
    elif not command.startswith('/') and is_chatting:
        bot.sendMessage(chat_id, eliza_chatbot.respond(command))
    else:
        pass


# Create a bot object with API key
bot = telepot.Bot('184876475:AAFKsZ6A9e-naIqJnvAXARLJ8Xuv27ODLHQ')

# Attach a function to notifyOnMessage call back
bot.notifyOnMessage(handle)

# Listen to the messages
while 1:
 time.sleep(10)
