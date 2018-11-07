curl -X POST -H "Content-Type: application/json" -d '{
"persistent_menu"😞
    {
    
    "locale":"default",
    "composer_input_disabled":"false",
    "call_to_actions"😞
        {
        "title":"📰 Tin nóng",
        "type":"postback",
        "payload":"tinnong"
        },
        {
        "title":"📚 Tin thú vị",
        "type":"postback",
        "payload":"tinthuvi"
        },
        
        {
        "title":"📱 Thêm...",
        "type":"nested",
        "call_to_actions"😞
             {
                "title":"⛅️ Thời tiết",
                "type":"postback",
                "payload":"thoitiet"
            },
            {
                "title":"📢 Nhận thông báo",
                "type":"postback",
                "payload":"nhanthongbao"
            },
            {
                "title":"🔒 Hủy nhận thông báo",
                "type":"postback",
                "payload":"huynhanthongbao"
            }
        ]
        }
    ]
    }
  ]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=