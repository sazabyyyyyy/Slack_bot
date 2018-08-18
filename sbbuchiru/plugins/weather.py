# from slackbot.bot import respond_to  # @botname：で反応するデコーダ
# from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダー
#
#
# @respond_to('今日の天気')
# def weather(message):
#     # 天気情報を取得して返信する
#     import urllib
#     import json
#
#     # データ取得
#     url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
#     # '016010'とすると道央の情報を取得してくれる
#     # ここを変えれば任意の地域の天気情報を取得できる
#     city_id = '016010'
#
#     html = urllib.request.urlopen(url + city_id)  # urlと都市のコードを組み合わせてurlを作る
#
#     jsonfile = json.loads(html.read().decode('utf-8'))  # 上記のurlを読み込んだjsonfileをロードし、デコード変換して変数に代入
#
#     text = jsonfile['description']['text']  # jsonfile内のdscription,text項目を変数textに代入
#
#     message.send(text)  # textをslackへ
#

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
