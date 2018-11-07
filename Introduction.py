from pymessenger2 import QuickReply
import requests
quick_replies1 = []
quick_replies1.append(QuickReply(content_type = 'text', title = '↪️ Truy cập ngay'))
quick_replies1.append(QuickReply(content_type = 'text', title = '📓 Hướng dẫn sử dụng'))
quick_replies1.append(QuickReply(content_type = 'text', title = '📂 Các gói dịch vụ'))
quick_replies1.append(QuickReply(content_type = 'text', title = '🏠 Home'))
quick_replies2 = []
quick_replies2.append(QuickReply(content_type = 'text', title = 'Case Study tham khảo'))
quick_replies2.append(QuickReply(content_type = 'text', title = 'Thông tin về dữ liệu'))
quick_replies2.append(QuickReply(content_type = 'text', title = 'Tạo bộ từ khóa'))
quick_replies2.append(QuickReply(content_type = 'text', title = '🔙 Quay lại'))
quick_replies2.append(QuickReply(content_type = 'text', title = '🏠 Home'))
quick_replies3 = []
quick_replies3.append(QuickReply(content_type = 'text', title = '⚙️ Các thông số'))
quick_replies3.append(QuickReply(content_type = 'text', title = '📦 Nguồn dữ liệu'))
quick_replies3.append(QuickReply(content_type = 'text', title = '🔰 Các loại dữ liệu'))
quick_replies3.append(QuickReply(content_type = 'text', title = '🔙 Quay lại'))
quick_replies3.append(QuickReply(content_type = 'text', title = '🏠 Home'))
quick_replies4 = []
quick_replies4.append(QuickReply(content_type = 'text', title = '🔑 Từ khóa chính'))
quick_replies4.append(QuickReply(content_type = 'text', title = '🔎 Từ khóa đi kèm'))
quick_replies4.append(QuickReply(content_type = 'text', title = '🔙 Quay lại'))
quick_replies4.append(QuickReply(content_type = 'text', title = '🏠 Home'))
def read_token():
    file = open('access_token.dat', 'r')
    token = file.readline()
    file.close()
    return token
ACCESS_TOKEN = read_token()

def send_button_home(recipient_id):
    payload = {
        "recipient":{
        "id":recipient_id
        },
        "message":{
        "attachment":{
        "type":"template",
        "payload":{
            "template_type":"button",
            "text":"",
            "buttons":[
            {
                "type":"postback",
                "title":"🏠 Home",
                "payload":"home"
            }
            ]
        }
        }
    } 
    }
    call_send_api(payload)

def call_send_api(messageData):
    response = requests.post(
        "https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": ACCESS_TOKEN},
        json=messageData
    )
    return response.json()
def gioiThieuSMCC(Bot, recipient_id, user_memory, mess_content):
    if (user_memory.get('state_1') == mess_content):
        # if (user_memory.get('state_2') is None)
        re = open("gioiThieuSmcc.dat","r")
        for line in re:
            Bot.send_text_message(recipient_id, line)
        Bot.send_quick_reply(recipient_id, "Tìm hiểu thêm về SMCC:", quick_replies1)
        return
        # if (user_memory.get('state_2') == mess_content):
    if (user_memory.get('state_1') != mess_content):
        if (user_memory.get('state_2') not in ['↪️ Truy cập ngay', '📓 Hướng dẫn sử dụng', '📂 Các gói dịch vụ']):
            user_memory['state_2'] = mess_content
            print(user_memory['state_2'])
            if (mess_content == '↪️ Truy cập ngay'):
                button1 = [
                 {
                    "type": "web_url",
                    "url": "https://smcc.vn/",
                    "title": "SMCC.VN"
                 }
                ]
                user_memory['state_2'] = None
                Bot.send_button_message(recipient_id, "truy cập tại địa chỉ:", button1)
                Bot.send_quick_reply(recipient_id, "Tìm hiểu thêm về SMCC:", quick_replies1)
                return
            if (mess_content == '📓 Hướng dẫn sử dụng'):
                response = 'SMCC xin gửi bạn bộ tài liệu hướng dẫn sử dụng công cụ: http://bit.ly/tailieuhuongdansmcc'
                Bot.send_text_message(recipient_id, response)
                response1 = 'Hãy cùng tìm hiểu rõ hơn về cách dùng SMCC nhé!'
                Bot.send_quick_reply(recipient_id, response1, quick_replies2)
                print(user_memory['state_2'])
                return
            if (mess_content == '📂 Các gói dịch vụ'):
                response = open('cacgoidv.dat', 'r')
                print(response)
                for line in response:
                    Bot.send_text_message(recipient_id, line)
                Bot.send_quick_reply(recipient_id, "Tìm hiểu thêm về SMCC:", quick_replies1)
                user_memory['state_2'] = None
                return
        if (user_memory['state_2'] == '📓 Hướng dẫn sử dụng'):
            print(user_memory.get('state_3'))
            if (user_memory.get('state_3') not in ['Case Study tham khảo', 'Thông tin về dữ liệu', 'Tạo bộ từ khóa']):
                user_memory['state_3'] = mess_content
                if (mess_content == 'Case Study tham khảo'):
                    response = open('caseStudy.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, 'Tìm hiểu về cách dùng SMCC:', quick_replies2)
                    user_memory['state_3'] = None
                    return
                if (mess_content == 'Thông tin về dữ liệu'):
                    response = 'Dữ liệu của SMCC là reality data được tổng hợp lại từ các bài viết trên Facebook, các trang báo, forums, blogs.'
                    Bot.send_text_message(recipient_id, response)
                    Bot.send_quick_reply(recipient_id, "Tìm hiểu về dữ liệu:", quick_replies3)
                    return
                if (mess_content == 'Tạo bộ từ khóa'):
                    response = open('taotukhoa.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, 'Tìm hiểu về các loại từ khóa:', quick_replies4)
                    return
                if (mess_content == '🔙 Quay lại'):
                    user_memory['state_3'] = None
                    user_memory['state_2'] = None
                    Bot.send_quick_reply(recipient_id, "Tìm hiểu thêm về SMCC:", quick_replies1)
                    return
            if (user_memory['state_3'] == 'Thông tin về dữ liệu'):
                user_memory['state_4'] = mess_content
                response1 = 'Tìm hiểu về dữ liệu:'
                if (mess_content == '⚙️ Các thông số'):
                    response = open('thongtindl.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, response1, quick_replies3)
                    user_memory['state_4'] = None
                    return
                if (mess_content == '📦 Nguồn dữ liệu'):
                    response = open('nguondl.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, response1, quick_replies3)
                    user_memory['state_4'] = None
                    return
                if (mess_content == '🔰 Các loại dữ liệu'):
                    response = open('loaidl.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, response1, quick_replies3)
                    user_memory['state_4'] = None
                    return
                if (mess_content == '🔙 Quay lại'):
                    response = 'Tìm hiểu về cách dùng SMCC'
                    Bot.send_quick_reply(recipient_id, response, quick_replies2)
                    user_memory['state_4'] = None
                    user_memory['state_3'] = None
                    return
            if (user_memory['state_3'] == 'Tạo bộ từ khóa'):
                user_memory['state_4'] = mess_content
                response1 = 'Tìm hiểu về các loại từ khóa:'
                if (mess_content == '🔑 Từ khóa chính'):
                    response = open('tukhoachinh.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, response1, quick_replies4)
                    user_memory['state_4'] = None
                    return
                if (mess_content == '🔎 Từ khóa đi kèm'):
                    response = open('tukhoadikem.dat', 'r')
                    for line in response:
                        Bot.send_text_message(recipient_id, line)
                    Bot.send_quick_reply(recipient_id, response1, quick_replies4)
                    user_memory['state_4'] = None
                    return
                if (mess_content == '🔙 Quay lại'):
                    response = 'Tìm hiểu về cách dùng SMCC'
                    Bot.send_quick_reply(recipient_id, response, quick_replies2)
                    user_memory['state_4'] = None
                    user_memory['state_3'] = None
                    return

