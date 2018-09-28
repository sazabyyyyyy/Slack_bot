import pybitflyer
from zaifapi import ZaifPublicApi

from bs4 import BeautifulSoup
import urllib.request as req

from slackbot.bot import listen_to
from slackbot.bot import respond_to

@listen_to("ビットコイン")
@listen_to("bitcoin")
@respond_to('bitcoin')
@respond_to('ビットコイン')

def mention_func1(message):

 bit=pybitflyer.API()
 btc=bit.ticker(product_code="BTC_JPY")

 zaif=ZaifPublicApi()
 xem=zaif.ticker("xem_jpy")
 mona=zaif.ticker("mona_jpy")


 message.send("BTC: "+str(btc["ltp"])+"円")
 message.send("XEM:"+str(xem["last"])+"円")
 message.send("MONA"+str(mona["last"]) +"円")
