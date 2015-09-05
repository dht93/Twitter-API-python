import tweepy
from geoloc import coordinates

ckey='your_twitter_consumer_key'
csecret='your_consumer_secret'
atoken='your_access_token'
asecret='your_access_secret'

address=raw_input("Enter the location whose trends you want to know.\n")

coo=coordinates(address)
lati=coo[0]
longi=coo[1]

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

trendslist=[]

loc=api.trends_closest(lat=lati,long=longi)      #Returns the locations closest to the specified location
place=loc[0]['name']
woeid=loc[0]['woeid']                            #extracting the woeid of the first location

trends=api.trends_place(id=woeid)                #Returns the top 10 trending topics

for item in trends[0]['trends']:                 #trends is a list whose first element is of type dict
    trendslist.append(item['name'])

print '\n\nTrends near '+str(address)+' are:'
print ''
for trend in trendslist:
    print trend
