from slackbot.bot import respond_to  # @botname：で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダー




#@respond_to()
@respond_to('てんき')
@respond_to('天気')
def weather(message):
    # 天気情報を取得して返信する
    import urllib
    import json

    # データ取得
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '016010'とすると道央の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '016010'

    html = urllib.request.urlopen(url + city_id)  # urlと都市のコードを組み合わせてurlを作る

    jsonfile = json.loads(html.read().decode('utf-8'))  # 上記のurlを読み込んだjsonfileをロードし、デコード変換して変数に代入

    title = jsonfile['title']

    telop = jsonfile['forecasts'][0]['telop']  # jsonfile内の配列forecastsの0番目（今日の天気）のtelop項目
    day = jsonfile['forecasts'][0]['dateLabel']

    telop1 = jsonfile['forecasts'][1]['telop']  # 配列forecastsの1番目（明日の天気）のtelop項目
    day1 = jsonfile['forecasts'][1]['dateLabel']

    telop2 = jsonfile['forecasts'][2]['telop']  # 配列forecastsの2番目（明後日の天気）のtelop項目
    day2 = jsonfile['forecasts'][2]['dateLabel']

    # telopが晴れだったら晴れのスラックのアイコンとか場合分け
    telop_icon = ''
    if telop.find('雪') > -1:
        telop_icon = ':showman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thinder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'

    telop1_icon = ''
    if telop1.find('雪') > -1:
        telop1_icon = ':showman:'
    elif telop1.find('雷') > -1:
        telop1_icon = ':thinder_cloud_and_rain:'
    elif telop1.find('晴') > -1:
        if telop1.find('曇') > -1:
            telop1_icon = ':partly_sunny:'
        elif telop1.find('雨') > -1:
            telop1_icon = ':partly_sunny_rain:'
        else:
            telop1_icon = ':sunny:'
    elif telop1.find('雨') > -1:
        telop1_icon = ':umbrella:'
    elif telop1.find('曇') > -1:
        telop1_icon = ':cloud:'
    else:
        telop1_icon = ':fire:'

    telop2_icon = ''
    if telop2.find('雪') > -1:
        telop2_icon = ':showman:'
    elif telop2.find('雷') > -1:
        telop2_icon = ':thinder_cloud_and_rain:'
    elif telop2.find('晴') > -1:
        if telop2.find('曇') > -1:
            telop2_icon = ':partly_sunny:'
        elif telop2.find('雨') > -1:
            telop2_icon = ':partly_sunny_rain:'
        else:
            telop2_icon = ':sunny:'
    elif telop2.find('雨') > -1:
        telop2_icon = ':umbrella:'
    elif telop2.find('曇') > -1:
        telop2_icon = ':cloud:'
    else:
        telop2_icon = ':fire:'

    text = title + '\n' + day + 'は' + telop + telop_icon + '\n' + day1 + 'は' + telop1 + telop1_icon + '\n' + day2 + 'は' + telop2 + telop2_icon+"だにゃ"

    message.send(text)



























    # @respond_to('string')     bot宛のメッセージ
    #                           stringは正規表現が可能 「r'string'」
    # @listen_to('string')      チャンネル内のbot宛以外の投稿
    #                           @botname: では反応しないことに注意
    #                           他の人へのメンションでは反応する
    #                           正規表現可能
    # @default_reply()          DEFAULT_REPLY と同じ働き
    #                           正規表現を指定すると、他のデコーダにヒットせず、
    #                           正規表現にマッチするときに反応
    #                           ・・・なのだが、正規表現を指定するとエラーになる？

    # message.reply('string')   @発言者名: string でメッセージを送信
    # message.send('string')    string を送信
    # message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
    #                               文字列中に':'はいらない
