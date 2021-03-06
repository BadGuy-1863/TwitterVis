from json import JSONDecodeError

import tweepy
from textblob import TextBlob
import requests
import json

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

c_key = "0iyK7MB6jiQ1KM4267bhOyNNk"
c_sec = "bynOPvxzK74YjJtbXknhkE26MO2EIIbm86tiPegidIODYNsbP0"

auth = tweepy.OAuthHandler(c_key, c_sec)
api = tweepy.API(auth)

#hashtag to generate a map of
hashtag = '#bernie2020'

#maps polarity to usable data
def mapsize(n):
    return 5+20*abs(n)

def mapcolor(n):
    if n<0:
        return 'r'
    elif n == 0:
        return 'k'
    else:
        return 'b'

#initialize map
fig = plt.figure(figsize=(8, 8))
m = Basemap()
m.drawcoastlines()

#iterate through search results for the hashtag
for tweet in tweepy.Cursor(api.search, q = hashtag).items(75):
    data = TextBlob(tweet.text)
    sent = data.sentiment
    add =  tweet.user.location
    loc = requests.get(
        "http://www.mapquestapi.com/geocoding/v1/address?key=VYYvg1ALBxbHr9ePwBS3BnWkLxHMtOyk&location=" + add)
    try:
        j_dict = json.loads(loc.text)
        coords = j_dict['results'][0]['locations'][0]['latLng']
        x, y = m(coords['lng'], coords['lat'])
        m.plot(x, y, marker='o', color=mapcolor(sent.polarity), ms=mapsize(sent.polarity))
    except IndexError:
        continue
    except JSONDecodeError:
        continue
#saves the map with some whitespace trimmed
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
plt.savefig(hashtag + '.png')
plt.show()
