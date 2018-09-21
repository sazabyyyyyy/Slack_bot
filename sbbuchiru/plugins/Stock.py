from slackbot.bot import respond_to
from slackbot.bot import listen_to

from bs4 import BeautifulSoup
import urllib.request as req

@listen_to("為替")
@respond_to('為替')
def mention_func1(message):

    #ヤフーファイナンスからスクレイピング
    #ドル円
    res = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy")
    soup = BeautifulSoup(res, "html.parser")
    usd = soup.select_one(".stoksPrice").string

    #ユロ円
    res1 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=EURJPY")
    soup1 = BeautifulSoup(res1, "html.parser")
    euroyen = soup1.select_one(".stoksPrice").string

    #ユロル
    res2 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=EURUSD")
    soup2 = BeautifulSoup(res2, "html.parser")
    euro = soup2.select_one(".stoksPrice").string

    # #オジエン
    # res3 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy")
    # soup3 = BeautifulSoup(res3, "html.parser")
    # aud = soup3.select_one(".stoksPrice").string

    # トルコ
    res4 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=TRYJPY")
    soup4 = BeautifulSoup(res4, "html.parser")
    trky = soup4.select_one(".stoksPrice").string

    # ポンド
    res5 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=GBPJPY")
    soup5 = BeautifulSoup(res5, "html.parser")
    pond = soup5.select_one(".stoksPrice").string

    # ランド
    res6 = req.urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=ZARJPY")
    soup6 = BeautifulSoup(res6, "html.parser")
    zar = soup6.select_one(".stoksPrice").string

    message.send("ドル円    "+usd)
    message.send("ユーロドル " + euro)
    message.send("ユーロ円  " + euroyen)
    message.send("ランド   " + zar)
    message.send("トルコ円  " + trky)
    message.send("ポンド円  " + pond)

