from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)

url = "https://api.janja.me/v0/messages/text"
url1 = "https://api.janja.me/v0/messages/sendimage"
url2 = "https://api.janja.me/v0/messages/texturl"
url3 = "https://api.janja.me/v0/messages/sendcontact"
url4 = "https://api.janja.me/v0/messages/sendlocation"
url5 = "https://api.janja.me/v0/messages/sendaudio"
url6 = "https://api.janja.me/v0/messages/sendvideo"


headers = {
  'Authorization': 'Basic Y2Vic2FkbWluOll1QDQyMjAwMjExeHJkdA==',
  'Content-Type': 'application/json'
}

@app.route("/", methods=["GET", "POST"])
def index():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "message": "Hello, there this is a my Test URL \n https://www.ajua.com"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    return response.text


@app.route("/image", methods=["GET", "POST"])
def image():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://images.unsplash.com/photo-1644870430811-59048c8540ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=375&q=80",
        "caption": "Very nice"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    # print(response.text)
    return response.text


@app.route("/contact", methods=["GET", "POST"])
def contact():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "phone": "+256704880439",
        "phonetype": "mobile"
    })
    response = requests.request("POST", url3, headers=headers, data=payload)
    # print(response.text)
    return response.text

@app.route("/location", methods=["GET", "POST"])
def location():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "longitude": "1.1727",
        "latitude": "36.8308",
        "name": "Paradise lost kenya",
        "address": "Paradise lost , kiambu road, Nairobi, Kenya."
    })
    response = requests.request("POST", url4, headers=headers, data=payload)
    # print(response.text)
    return response.text

@app.route("/audio", methods=["GET", "POST"])
def audio():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "audio_url": "https://drive.google.com/file/d/1aRLJwgnk4hT12-QLKgGUP7TGuytET8WZ/view?usp=sharing"
    })
    response = requests.request("POST", url5, headers=headers, data=payload)
    # print(response.text)
    return response.text


    


    