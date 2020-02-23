from json import JSONDecodeError
import tweepy
import random
import pandas as pd
from textblob import TextBlob
import requests
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os

c_key = "0iyK7MB6jiQ1KM4267bhOyNNk"
c_sec = "bynOPvxzK74YjJtbXknhkE26MO2EIIbm86tiPegidIODYNsbP0"

auth = tweepy.OAuthHandler(c_key, c_sec)
api = tweepy.API(auth)

def mapsize(n):
    return 5+20*abs(n)

def mapcolor(n):
    if n<0:
        return 'r'
    elif n == 0:
        return 'k'
    else:
        return 'b'

rootdir = 'C:/Users/there/PycharmProjects/Misc/TwitterXSports/arab_spring_csv'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
        fig = plt.figure(figsize=(8, 8))
        m = Basemap()
        m.drawcoastlines()
        n = sum(1 for line in open(os.path.join(subdir, file), 'rt', encoding='utf-8'))  # number of records in file (excludes header)
        s = 65  # desired sample size
        skip = sorted(
            random.sample(range(1, n + 1), n - s))  # the 0-indexed header will not be included in the skip list
        data = pd.read_csv(os.path.join(subdir, file), sep = ';',  encoding='utf-8', names = ['date', 'user', 'text'], skiprows = skip)
        for index, row in data.iterrows():
            print(index)
            tweet = row['text']
            tweet_data = TextBlob(tweet)
            sent = tweet_data.sentiment
            add = api.get_user(row[1]).location
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
        name = os.path.splitext(file)[0][11:]
        fig.suptitle(name.split('-')[1] + '-' + name.split('-')[0], fontsize=20)
        plt.savefig(name.split('-')[1] + '-' + name.split('-')[0]+'.png')
