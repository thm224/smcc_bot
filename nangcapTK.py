from pymessenger2 import QuickReply
quickReply = []
quickReply.append(QuickReply(content_type = 'text', title = '☎️ Liên hệ'))

quickreplies1 = []
quickreplies1.append(QuickReply(content_type = 'text', title = '💳 Chuyển khoản'))
quickreplies1.append(QuickReply(content_type = 'text', title = '📄 Xuất hóa đơn'))
quickreplies1.append(QuickReply(content_type = 'text', title = '📑Dịch vụ làm báo cáo'))
quickreplies1.append(QuickReply(content_type = 'text', title = '🏠 Home'))
def nangcaptk(Bot, recipient_id, user_memory, mess_content):
    if (user_memory.get('state_1') == mess_content):
        re = open('nangcaptk.dat', 'r')
        for line in re:
            Bot.send_text_message(recipient_id, line)
        Bot.send_quick_reply(recipient_id, 'Tìm hiểu thêm:', quickreplies1)
        return
    if (user_memory.get('state_1') != mess_content):
        if (user_memory.get('state_2') not in ['💳 Chuyển khoản','📄 Xuất hóa đơn','📑Dịch vụ làm báo cáo']):
            user_memory['state_2'] = mess_content    
            if (mess_content == '💳 Chuyển khoản'):
                re = open('ttinchuyenkhoan.dat', 'r')
                for line in re:
                    Bot.send_text_message(recipient_id, line)
                Bot.send_quick_reply(recipient_id, 'Tìm hiểu thêm:', quickreplies1)
                user_memory['state_2'] = None
                return
            if (mess_content == '📄 Xuất hóa đơn'):
                re = open('xuathoadon.dat', 'r')
                for line in re:
                    Bot.send_text_message(recipient_id, line)
                Bot.send_quick_reply(recipient_id, 'Tìm hiểu thêm:', quickreplies1)
                user_memory['state_2'] = None
                return
            if (mess_content == '📑Dịch vụ làm báo cáo'):
                print(mess_content)
                response = 'Ngoài 2 gói Freemium và Premium, SMCC còn cung cấp dịch vụ data analysis by expert (chuyên gia kết hợp với dữ liệu của smcc để phân tích báo cáo).'
                Bot.send_quick_reply(recipient_id, response, quickReply)
                return
        if (user_memory.get('state_2') == '📑Dịch vụ làm báo cáo'):
            if mess_content == '☎️ Liên hệ':
                reponse = 'Thông tin liên hệ của SMCC:\nHotline: +84 973-999-804\nEmail: sale@smcc.vn'
                Bot.send_text_message(recipient_id, reponse)
                return
        