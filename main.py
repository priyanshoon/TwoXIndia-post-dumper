import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv
from gtts import gTTS
import requests
import time


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_audio(text):
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save('audio.mp3')


username = os.environ.get("username")
password = os.environ.get("password")
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")

teleurl = os.environ.get("teleurl")

reddit_instance = praw.Reddit(
        username = username,
        password = password,
        client_id = client_id,
        client_secret = client_secret,
        user_agent = "test-bot"
        )

subreddit = reddit_instance.subreddit("TwoXIndia")
new = subreddit.new(limit=1)


def get_video():
    for submission in new:
        if submission.is_video or submission.is_reddit_media_domain:
            link = submission.shortlink
            data = {
                    'chat_id': 5234092740,
                    'text': str(link)
                    }
            print(link)
            print(teleurl+"/sendMessage")
            send_msg = requests.post(teleurl+"/sendMessage", data)
            print(send_msg.status_code)
        else:
            title = submission.title
            print(title)
            get_audio(submission.selftext)
            audio = str('audio.mp3')
            os.system('ffmpeg -loop 1 -i ./img/patani.jpg -i '+ audio +' -shortest out.mp4')
            data = {
                    'chat_id': 5234092740,
                    'caption': str(title)
                    }
            send_video = requests.post(teleurl+"/sendVideo", data, files={'video': open('./out.mp4', 'rb')})
            data = {
                    'chat_id': 1594462597,
                    'caption': str(title)
                    }
            send_video = requests.post(teleurl+"/sendVideo", data, files={'video': open('./out.mp4', 'rb')})
            print(send_video.status_code)


def main():
    get_video()
    os.remove('out.mp4')
    os.remove('audio.mp3')


if __name__ == "__main__":
    while True:
        main()
        time.sleep(7200)
