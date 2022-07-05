import json
import tweepy as tw

token = 'AAAAAAAAAAAAAAAAAAAAAJoeeQEAAAAA7iNH8YSfVBzqVuiAYDgdla61Dgc%3DeemZaPy4BaJ10f06RYlZQGlTGOH1tLnU6w8OmXQvYsMFwJ7tAP'
con_key= 'hvgGbkA9kV7kfRSuoHxznZt62'
con_secret = 'PsJrx5S8mqFuhqsZId7LIr8r8x2O8C6SttjQL43IL5cA09KYyE'
acess_tk = '913219474995675136-bMcQwEGxAOaNBcWzngPT3ZbNLbwU4ZY'
acess_tk_secret = 'chREgGVv4rd0OeLSa5ovuKJC2dflo93QX7skqtvzA2kDJ'

client = tw.Client(bearer_token=token,
                    consumer_key=con_key,
                    consumer_secret=con_secret,
                    access_token=acess_tk,
                    access_token_secret=acess_tk_secret,
                    return_type=dict)


resposta = client.search_recent_tweets(query='"Lula" -is:retweet',
                                      max_results=10,
                                      tweet_fields = ['author_id','created_at','text','source','lang','geo'],
                                      user_fields = ['name','username','location','verified'],
                                      expansions = ['geo.place_id', 'author_id'],
                                      place_fields = ['country','country_code']
                                      )            

print(json.dumps(resposta['data'],ensure_ascii=False))                                           