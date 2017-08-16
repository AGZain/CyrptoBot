
import urllib
import urllib2
import json

def poloniex_data(type):
    #if(type == 'returnOrderBook'):
    data_return = urllib2.urlopen('https://poloniex.com/public?command=returnTicker')
    return json.loads(data_return.read())

print("Fetching data..\n")
out = poloniex_data('returnOrderBook')
dat = out["BTC_BCN"]["last"]
print(dat)
