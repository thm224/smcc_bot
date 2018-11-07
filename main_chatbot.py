# coding: utf-8

import random
from flask import Flask, request
from pymessenger2 import Bot
from pymessenger2 import QuickReply
from wit import Wit
import requests
from pymessenger2.utils import AttrsEncoder
import json



users = {}


def read_token():
    file = open('access_token.dat', 'r')
    token = file.readline()
    file.close()
    return token


app = Flask(__name__)
ACCESS_TOKEN = read_token()
VERIFY_TOKEN = 'hoangminh224'
bot = Bot(ACCESS_TOKEN)

# We will receive messages that Facebook sends our bot at this endpoint


@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                print(message)
                if message.get('postback'):
                    recipient_id = message['sender']['id']
                    if message['postback'].get('payload'):
                        received_message = message['postback'].get('payload')
                        print(receive_message)
                        send_typing_on(recipient_id)
                        process_message(received_message, recipient_id)
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('quick_reply'):
                        received_message = message['message']['quick_reply'].get('payload')
                        send_typing_on(recipient_id)
                        process_message(received_message, recipient_id)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        # response_sent_nontext = get_message()
                        send_message(recipient_id, "response_sent_nontext")
    return ''

def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def process_message(mess_content, recipient_id):    
    global users
    if recipient_id not in users:
        users[recipient_id] = {}
    user_memory = users[recipient_id]
    # intent = scan_content(mess_content)
    if (mess_content == 'start'):
        re = open('start.dat', 'r')
        for line in re:
            bot.send_text_message(recipient_id, line)
        return
    if (mess_content == '🏠 Home'):
        quick_replies1 = []
        quick_replies1.append(QuickReply(content_type = 'text', title = '💻 Giới thiệu về SMCC'))
        quick_replies1.append(QuickReply(content_type = 'text', title = '🎁 Tặng tài khoản'))
        quick_replies1.append(QuickReply(content_type = 'text', title = '⏫ Nâng cấp tài khoản'))
        quick_replies1.append(QuickReply(content_type = 'text', title = '❌ Báo lỗi'))
        quick_replies1.append(QuickReply(content_type = 'text', title = '☎️ Liên hệ'))
        bot.send_quick_reply(recipient_id, "SMCC Bot có thể giúp gì cho bạn  🤓 ☺", quick_replies1)
        return
    if (mess_content == '☎️ Liên hệ'):
        response = 'Thông tin liên hệ của SMCC:\nHotline: +84 973-999-804\nEmail: sale@smcc.vn'
        response1 = 'Với những câu hỏi không thể giải đáp qua chatbot, hãy ghi lại câu hỏi theo form dưới đây:'
        response2 = 'https://goo.gl/forms/JMMevegkovNOHUMz1'
        bot.send_text_message(recipient_id, response)
        bot.send_text_message(recipient_id, response1)
        quick_replies = []
        quick_replies.append(QuickReply(content_type = 'text', title = '🏠 Home'))
        bot.send_quick_reply(recipient_id, response2, quick_replies)
        return
    if (mess_content == '🎁 Tặng tài khoản'):
        response = 'Hiện SMCC đang tiến hành tặng gói Premium miễn phí trị giá 48 triệu đồng/năm cho các Social Influencers.'
        bot.send_text_message(recipient_id, response)
        response1 = 'Thông tin chi tiết vui lòng xem tại: https://www.facebook.com/smcc.vn/posts/1998741413574215'
        quick_replies = []
        quick_replies.append(QuickReply(content_type = 'text', title = '🏠 Home'))
        bot.send_quick_reply(recipient_id, response1, quick_replies)
        return 
    if (mess_content == '💻 Giới thiệu về SMCC' or mess_content == '⏫ Nâng cấp tài khoản' or mess_content == '❌ Báo lỗi' or mess_content == '👉 Thông tin khác'):
        user_memory['state_1'] = mess_content
        user_memory['state_2'] = None
        user_memory['state_3'] = None
        user_memory['state_4'] = None
        print(user_memory['state_1'])
    if (user_memory.get('state_1') == '💻 Giới thiệu về SMCC'):
        print(user_memory['state_1'])
        print(user_memory.get('state_2'))
        print(user_memory.get('state_3'))
        print(user_memory.get('state_4'))
        from Introduction import gioiThieuSMCC
        gioiThieuSMCC(bot, recipient_id, user_memory, mess_content)  
    if (user_memory.get('state_1') == '⏫ Nâng cấp tài khoản'):
        from nangcapTK import nangcaptk 
        nangcaptk(bot, recipient_id, user_memory, mess_content)
    if (user_memory.get('state_1') == '❌ Báo lỗi'):
        from baoloi import BaoLoi
        BaoLoi(bot, recipient_id, user_memory, mess_content)
    if (user_memory.get('state_1') == '👉 Thông tin khác'):
        from otherInfo import otherInformations
        otherInformations(bot, recipient_id, user_memory, mess_content)
            
def scan_content(mess_content):
    client = Wit("7PMLK4MWS5T2XRWGAK4GRCZTFUDXHPVY")
    resp = client.message(str(mess_content))
    if 'intent' in resp['entities']:
        for y in resp['entities']['intent']:
            return str(y['value'])
    else:
        return None
def send_typing_on(recipient_id):
    payload = {
        'sender_action': 'typing_on'
        ,'recipient': {
            'id': recipient_id
        }
    }
    call_send_api(payload)

def send_request_thread_control(recipient_id):
    print('ad')
    payload = {
        "recipient": {
            "id": recipient_id
        },
        "target_app_id": "263902037430900"
    }
    call_send_api1(payload)

def call_send_api(messageData):
    response = requests.post(
        "https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": ACCESS_TOKEN},
        json=messageData
    )
    return response.json()
def call_send_api1(messageData):
    response = requests.post(
        "https://graph.facebook.com/v2.6/me/pass_thread_control",
        params={"access_token": ACCESS_TOKEN},
        json=messageData
    )
    return response.json()

if __name__ == "__main__":
    app.run()
# curl -X POST -H "Content-Type: application/json" -d '{ 
#         "get_started":{
#                      "payload":"start"
#                 }
# }' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAgxBwLaxtkBAJyJJWlMOv7x0SjtB7UPyAdCr2wgnA3gUeVMN9FPwKgJvgkLuZA58LagRGZA0GZCtdzutD5wCsb9wepyPH7ctd6wbbRkYHv2Gg0ra7VwaxsAeAGfDXx1nRHsxMiPgMZCKILpoW4qS5Mmb3dae1o7z5VQycYN9wZDZD"
# }' "https://graph.facebook.com/v2.6/me/messages?access_token=EAAgxBwLaxtkBAL1kMZAH044dcJOL6339ZBfwkpdWEZCZAO2tZBFi76BRabFjEkJJOvxSgVe8mM3eWGHCt69zXyjAZAwhFARMmOJmzFqqsOfY1wWpj66Qg4l8YKEXZAXZCMZC6WHsgLro7AlSkuNRzepraCaWTLiUquhCapbb4Cvd3i4EQ3ourqXeH"
# curl -X POST -H "Content-Type: application/json" -d '{
#         "persistent_menu":[
#             {
#                 "locale":"default",
#                 "composer_input_disabled":true,
#                 "call_to_actions":[
#                     {
#                         "title":"🏠 Home",
#                         "type":"postback",
#                         "payload":"🏠 Home"
#                     },
#                     {
#                         "title":"📳 Hỗ trợ",
#                         "type":"nested",
#                         "call_to_actions":[
#                             {
#                                 "title":"⏫ Nâng cấp tài khoản",
#                                 "type":"postback",
#                                 "payload":"⏫ Nâng cấp tài khoản"
#                             },
#                             {
#                                 "title":"❌ Báo lỗi",
#                                 "type":"postback",
#                                 "payload":"❌ Báo lỗi"
#                             },
#                             {
#                                 "title":"☎️ Liên hệ",
#                                 "type":"postback",
#                                 "payload":"☎️ Liên hệ"
#                             }
#                         ]
#                     },
#                     {
#                         "title":"👉 Thông tin khác",
#                         "type":"postback",
#                         "payload":"👉 Thông tin khác"
#                     }
#                 ]
#             }
#         ]
# }' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAgxBwLaxtkBAJyJJWlMOv7x0SjtB7UPyAdCr2wgnA3gUeVMN9FPwKgJvgkLuZA58LagRGZA0GZCtdzutD5wCsb9wepyPH7ctd6wbbRkYHv2Gg0ra7VwaxsAeAGfDXx1nRHsxMiPgMZCKILpoW4qS5Mmb3dae1o7z5VQycYN9wZDZD"
