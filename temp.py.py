#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(5JnnjGNghoeSqldjULv+ZQC2koPy57QV6e4vcqbthf5W1/2WQPblUyKrvm0im6p/sF0aPQG8JJwfpt5fn69EWwYPpDymklJsU2TFmRoOppHJqUfppBPBZdrRauCBP543eeqMmDRgqbojgNRgE9iO+AdB04t89/1O/w1cDnyilFU=)
# 必須放上自己的Channel Secret
handler = WebhookHandler(
13fcc1266a5de0844503f15f0b245055

)

line_bot_api.push_message(
U5ec25188a66aa9714d14011c0c7a2b65, TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

