import os
import json
import tweepy as tw
from datetime import datetime, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
path = r'{}'.format(os.path.normpath(dir_path + '/env.json'))

with open(path,'r',encoding='utf8') as file:
    auth = json.load(file)


class getTweets:


    start_at = (datetime.now() + timedelta(hours=-3) ).strftime("%Y-%m-%dT%H:00:00Z")
    end_at   = (datetime.now() + timedelta(hours=-3) ).strftime("%Y-%m-%dT%H:59:59Z")

    

    client = tw.Client(bearer_token=auth['bearer_token'],
                    consumer_key=auth['consumer_key'],
                    consumer_secret=auth['consumer_secret'],
                    access_token=auth['access_token'],
                    access_token_secret=auth['access_token_secret'],
                    return_type=dict)

    def getTweet(self, start_at,end_at, next_token = None):

        return self.client.search_recent_tweets(query='"Lula" "Bolsonaro" -is:retweet',
                                            max_results=100,
                                            tweet_fields = ['author_id','created_at','text','source','lang'],
                                            user_fields = ['name','username','location','verified'],
                                            expansions = ['author_id',],
                                            start_time  = [start_at],
                                            end_time    = [end_at],
                                            place_fields = ['country','country_code'],
                                            next_token = next_token
                                            )



    def pagination(self):         
        tweets = []
        response = self.getTweet(self.start_at,self.end_at)
        tweets.append(response['data'])
        next_token = response['meta']['next_token']

        while 'next_token' in response['meta'].keys():
           response = self.getTweet(self.start_at,self.end_at,next_token)
           tweets.append(response['data'])
	    
        return tweets 



if __name__ == "__main__":

    print(getTweets().pagination())    
