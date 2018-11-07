from pymessenger2 import QuickReply

quickreplies = []
quickreplies.append(QuickReply(content_type = 'text', title = '🎉 Ưu đãi'))
quickreplies.append(QuickReply(content_type = 'text', title = '🙌 Hợp tác'))
quickreplies.append(QuickReply(content_type = 'text', title = '🖥 InfoRe'))

quickreplies_1 = []
quickreplies_1.append(QuickReply(content_type = 'text', title = '☎️ Liên hệ'))

def otherInformations(Bot, recipient_id, user_memory, mess_content):
    if (user_memory.get('state_1') == mess_content):
        Bot.send_quick_reply(recipient_id, 'Các thông tin khác:', quickreplies)
        return
    if (user_memory.get('state_1') != mess_content):
        if (user_memory.get('state_2') is None):
            user_memory['state_2'] = mess_content
            if (mess_content == '🎉 Ưu đãi'):
                re = open('uudai.dat', 'r')
                for line in re:
                    Bot.send_text_message(recipient_id, line)
                Bot.send_quick_reply(recipient_id, 'Các thông tin khác:', quickreplies)
                user_memory['state_2'] = None
                return
            if (mess_content == '🙌 Hợp tác'):
                re = open('hoptac.dat', 'r')
                for line in re:
                    Bot.send_text_message(recipient_id, line)
                reponse = 'Thông tin liên hệ của SMCC:\nHotline: +84 973-999-804\nEmail: sale@smcc.vn'
                Bot.send_text_message(recipient_id, reponse)
                Bot.send_quick_reply(recipient_id, 'Các thông tin khác:', quickreplies)
                user_memory['state_2'] = None
                return
            if (mess_content == '🖥 InfoRe'):
                re = open('infore.dat', 'r')
                for line in re:
                    Bot.send_text_message(recipient_id, line)
                Bot.send_quick_reply(recipient_id, 'Các thông tin khác:', quickreplies)
                user_memory['state_2'] = None    
                return
                
# curl -X POST -H "Content-Type: application/json" -d '{
#   "recipient":{
#     "id":"1853291161414120"
#   },
#   "sender_action":"typing_on"
# }' "https://graph.facebook.com/v2.6/me/messages?access_token=EAAgxBwLaxtkBAHMloficzdtHmMJDycC32OcZCqoWIIGZACvYomzEJMHSou07ByMZBT6W5uaKgUaT6qw383UFz3SiiHCMqpbU7oEuiRGVXE9Rm1TUYzQRJ04uP3wWLLUeRPfRlxnVQZA2TUqbza49O1ZAp39AYOYGCU0J9THXZB52HiPUmnqaN6"