from pymessenger2 import QuickReply

quickreplies1 = []
quickreplies1.append(QuickReply(content_type = 'text', title = '🆕Kích hoạt tài khoản'))
quickreplies1.append(QuickReply(content_type = 'text', title = '⭕️ Không có dữ liệu'))
quickreplies1.append(QuickReply(content_type = 'text', title = '✘ Lỗi khác'))
quickreplies1.append(QuickReply(content_type = 'text', title = '🏠 Home'))

quick_replies2 = []
quick_replies2.append(QuickReply(content_type = 'text', title = 'Case Study tham khảo'))
quick_replies2.append(QuickReply(content_type = 'text', title = 'Thông tin về dữ liệu'))
quick_replies2.append(QuickReply(content_type = 'text', title = 'Tạo bộ từ khóa'))
quick_replies2.append(QuickReply(content_type = 'text', title = '🏠 Home'))

quickreplies2 = []
quickreplies2.append(QuickReply(content_type = 'text', title = 'Mình nhận được rồi!'))
quickreplies2.append(QuickReply(content_type = 'text', title = 'Vẫn chưa thấy email!'))
quickreplies2.append(QuickReply(content_type = 'text', title = '🏠 Home'))

quickReply = []
quickReply.append(QuickReply(content_type = 'text', title = '📓 Hướng dẫn sử dụng'))
quickReply.append(QuickReply(content_type = 'text', title = '🏠 Home'))

home = []
home.append(QuickReply(content_type = 'text', title = '🏠 Home'))




def BaoLoi(Bot, recipient_id, user_memory, mess_content):
    if (user_memory.get('state_1') == mess_content):
        reponse = 'SMCC rất xin lỗi vì bạn đã gặp phải bất tiện này. Vui lòng cho chúng tôi biết sự cố bạn đã gặp phải nhé!'
        Bot.send_quick_reply(recipient_id, reponse, quickreplies1)
        return
    if (user_memory.get('state_1') != mess_content):
        if (mess_content == '📓 Hướng dẫn sử dụng'):
            response = 'SMCC xin gửi bạn bộ tài liệu hướng dẫn sử dụng công cụ: http://bit.ly/tailieuhuongdansmcc'
            Bot.send_text_message(recipient_id, response)
            response1 = 'Hãy cùng tìm hiểu rõ hơn về cách dùng SMCC nhé!'
            Bot.send_quick_reply(recipient_id, response1, quick_replies2)
            user_memory['state_1'] = '💻 Giới thiệu về SMCC'
            user_memory['state_2'] = '📓 Hướng dẫn sử dụng'
            user_memory['state_3'] = None
            user_memory['state_4'] = None
            return
        if (user_memory.get('state_2') not in ['🆕Kích hoạt tài khoản', '⭕️ Không có dữ liệu', "✘ Lỗi khác"]):
            user_memory['state_2'] = mess_content
            if(mess_content == '🆕Kích hoạt tài khoản'):
                response = 'Vui lòng kiểm tra kỹ email, kể cả Spam để đảm bảo rằng đã nhận được email kích hoạt của SMCC nhé!'
                Bot.send_quick_reply(recipient_id, response, quickreplies2)
                return
            if (mess_content == '⭕️ Không có dữ liệu'):
                response = 'Dữ liệu không trả về đôi lúc là do bộ từ khóa và thời gian lựa chọn của bạn chưa thật chính xác. Hãy tham khảo thêm hướng dẫn của SMCC để giải quyết nhé!'
                Bot.send_quick_reply(recipient_id, response, quickReply)
                return
            if (mess_content == "✘ Lỗi khác"):
                response = 'Vui lòng cho chúng tôi biết sự cố bạn đã gặp phải nhé!'
                response1 = 'https://goo.gl/forms/PkUndkbHfExGK3ME3'
                Bot.send_text_message(recipient_id, response)
                Bot.send_quick_reply(recipient_id, response1, home)
                return
        if (user_memory.get('state_2') == '🆕Kích hoạt tài khoản'):
            print(user_memory['state_2'])
            if (mess_content == 'Mình nhận được rồi!'):
                response = 'Cảm ơn bạn đã đăng ký sử dụng SMCC! Hãy cùng tìm hiểu thêm về cách sử dụng SMCC nhé!'
                Bot.send_quick_reply(recipient_id, response, quickReply)
                return
            if (mess_content == 'Vẫn chưa thấy email!'):
                response = 'Hãy cho chúng tôi email bạn đăng ký để SMCC kiểm tra lại nhé!'
                Bot.send_text_message(recipient_id, response)
                return

# curl -X POST -H "Content-Type: application/json" -d '{
#   "recipient":{
#     "id":"1853291161414120"
#   },
#   "message":{
#     "attachment":{
#       "type":"template",
#       "payload":{
#         "template_type":"button",
#         "text":"Try the postback button!",
#         "buttons":[
#           {
#             "type":"postback",
#             "title":"🏠 Home",
#             "payload":"home"
#           }
#         ]
#       }
#     }
#   }
# }' "https://graph.facebook.com/v2.6/me/messages?access_token=EAAgxBwLaxtkBAL1kMZAH044dcJOL6339ZBfwkpdWEZCZAO2tZBFi76BRabFjEkJJOvxSgVe8mM3eWGHCt69zXyjAZAwhFARMmOJmzFqqsOfY1wWpj66Qg4l8YKEXZAXZCMZC6WHsgLro7AlSkuNRzepraCaWTLiUquhCapbb4Cvd3i4EQ3ourqXeH"
