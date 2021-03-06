import json
#import pandas as pd

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import MysqlDemo
#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        name = (tweet['user']['name']).encode("utf-8")
        text = (tweet['text']).encode("utf-8")
        createdTime = (tweet['created_at']).encode("utf-8")
        #print (data)
        MysqlDemo.mysqlInsert(name, text, createdTime)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'http', 'https'
    stream.filter(track=['http:', 'https:'])
    