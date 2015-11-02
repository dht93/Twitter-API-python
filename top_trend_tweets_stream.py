from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy
from geoloc import coordinates


ckey='your consumer key'
csecret='your consumer secret'
atoken='your access token'
asecret='your access secret'

address=raw_input("Enter the location whose top trend you want to know.\n")

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

first_trend=trendslist[0]                       #top trend

if first_trend[0]=='#':
    first_trend=first_trend[1:]

file_name=str(address)+" "+str(first_trend)+".txt"

print "Top trending in "+str(address)+" is: "+str(first_trend)
print ''

print "Current tweets about "+str(first_trend)+" :\n"
print''

class listener(StreamListener):
    def on_data(self,data):
        try:
            user_name=data.split('"screen_name":"')[1].split('","location"')[0]
            text=data.split(',"text":"')[1].split('","source')[0]
            print '@'+str(user_name)+' tweeted: '+str(text)
            print '\n'
            #file_name=str(first_trend)+".txt"
            savefile=open(file_name,'a')
            savefile.write('@'+str(user_name)+' tweeted: '+str(text))
            savefile.write('\n')
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException,e:
            print 'failed '+ str(e)
            time.sleep(5)
    def on_error(self,status):
        print status

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=[first_trend])
