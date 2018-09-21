from slackbot.bot import listen_to
from slackbot.bot import respond_to
import pybitflyer

@listen_to("ビットコイン")
@listen_to("bitcoin")
@listen_to("")
def mention_func1(message):


 bit=pybitflyer.API()
 btc=bit.ticker(product_code="BTC_JPY")





 message.send("BTC: "+str(btc["ltp"])+"円")


