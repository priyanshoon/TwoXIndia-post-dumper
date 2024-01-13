# TwoXIndia Post Dumper

__The tool is still incomplete__

This tool will fetch the new post from r/TwoXIndia and convert that text form to
video and upload it to telegram.

Add your reddit username password

Get your client_id client_secret


```fish
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

```fish
python3 main.py
```

- [x] Reddit Scraper
- [x] Text to Audio
- [x] ffmpeg Implementation for merging img and audio
- [ ] Adding Subtitle to video
- [ ] Random img picker for video
- [x] Telegram Implementation
- [ ] Database Setup
