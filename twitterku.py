#twitterku.py

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
bot = telepot.Bot('token')

# Attach a function to notifyOnMessage call back
bot.notifyOnMessage(handle)

# Listen to the messages
while 1:
 time.sleep(10)
