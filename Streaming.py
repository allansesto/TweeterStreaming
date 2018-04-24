
## Autor: Allan Sesto - 02/04/18

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

### Tokens e Chaves de autenticação

consumer_key = 'post_your_key_here'
consumer_secret = 'post_your_secret_here'
access_token = 'post_your_token_here'
access_secret = 'post_your_secretToken_here'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

### Declere da API com as palavras chaves

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('Analysis_hoje.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


## Hashs de Buscas

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(
    track=['Terça', 'Terça-Feira', 'Lula', 'Aecio Neves', 'Politica', 'Lava-Jato', 'Policia Federal', 'O Mecanismo'])
