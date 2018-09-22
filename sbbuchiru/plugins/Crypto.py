from slackbot.bot import listen_to
from slackbot.bot import respond_to
from zaifapi import ZaifPublicApi
import pybitflyer

#pybitflyerライブラリを使う。bitflyerライトニングの銘柄から取得
@listen_to("ビットコイン")
@listen_to("bitcoin")
def mention_func1(message):


 bit=pybitflyer.API()
 btc=bit.ticker(product_code="BTC_JPY")

 #mona&xemはzaifAPIから取得
 zaif=ZaifPublicApi()

 xem = zaif.ticker("xem_jpy")
 mona = zaif.ticker("mona_jpy")

 message.send("BTC: "+str(btc["ltp"])+"円")
 message.send("XEM:"+str(xem["last"])+"円")
 message.send("MONA"+str(mona["last"]) +"円")

