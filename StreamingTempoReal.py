# -*- coding: utf-8 -*-

#author: Allan Sesto

import tweepy
import json
from textblob import TextBlob
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'post_your_key_here'
consumer_secret = 'post_your_secret_here'
access_token = 'post_your_token_here'
access_secret = 'post_your_secretToken_here'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            txtblb = TextBlob(tweet).sentiment
            print(tweet, txtblb.polarity, txtblb.subjectivity)
            if (txtblb.subjectivity*100 >= 60):
                output = open("TwitterAnalisys_20180403.txt","a")
                output.write(str(txtblb.polarity))
                output.write('\n')
                output.close()
                return True           
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['', 'Temer', 'Ministro Barroso', 'Lula', 'Lula2018', 'Carmem Lucia','STF', 'Habeas Corpus', 'Dilma'])
