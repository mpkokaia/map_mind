from django.db import models
from TwitterAPI import TwitterAPI
import json
import urllib2
# Create your models here.
class Data():
    def __init__(self,lat,lng):
        self.lat=lat
        self.lng=lng

    def get_twitts(self):
        consumer_key='cAyuxu0b59RnFfZSBSmgQ'
        consumer_secret='aUIcVMwiyD4JUiZIPjzyJ4YBGNyyQZbN1pGLqzck2g'
        access_token_key='2207373091-0t8uHrdUMKOPVGhwIdIXSEaEgZe067wNVIm3CkE'
        access_token_secret='dffIVTmJ0hfzdZnwJjwch4r9Phjp86cwGe6jhRPwznud0'
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('search/tweets', {'geocode':str(self.lat)+','+str(self.lng)+','+'5km','result_type':'recent'})
        array=[]
        for item in r.get_iterator():
            array.append(item['text'])
        return (array)

    def get_photos(self):
        CLIENTID='1ba7375c89e04f17933528a0c104f544'
        url='https://api.instagram.com/v1/media/search?lat='+str(self.lat)+'&lng='+str(self.lng)+'&distance='+'5km'+'&client_id='+ CLIENTID
        req = urllib2.urlopen(url)
        obj = json.loads(req.read().decode('utf-8'))
        array=[]
        for i in range(len(obj['data'])):
            array.append(obj['data'][i]['images']['standard_resolution']['url'])
        return (array)
