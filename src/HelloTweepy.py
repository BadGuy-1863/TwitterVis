import tweepy
c_key = "0iyK7MB6jiQ1KM4267bhOyNNk"
c_sec = "bynOPvxzK74YjJtbXknhkE26MO2EIIbm86tiPegidIODYNsbP0"

auth = tweepy.OAuthHandler(c_key, c_sec)
#auth.set_access_token("1106421196642492417-qOfYHTZOFhi3pmSeo3UsQWxyknKDcn", "GAS8iUymH0EL61WqhogBFyPeZuUKxvF1YHW1svAri3DkS")
#This lets me use MY twitter, not just public
api = tweepy.API(auth)
'''public_tweets = api.home_timeline()

user = api.get_user('twitter')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)'''

for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)