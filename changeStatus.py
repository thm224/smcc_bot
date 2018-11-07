from flask import Flask, request
import requests

PAGE_ACCESS_TOKEN = open('access_token.dat', 'r').readline()

def send_typing_on(recipient_id):
    payload = {
        'sender_action': 'typing_on'
        ,'recipient': {
            'id': recipient_id
        }
    }
    call_send_api(payload)

def send_typing_off(recipient_id):
    payload = {
        'sender_action': 'typing_off'
        ,'recipient': {
            'id': recipient_id
        }
    }
    call_send_api(payload)

def call_send_api(messageData):
    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }
    response = requests.post(
        FB_API_URL,
        params=auth,
        json=messageData
    )
    return response.json()


