#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup 
import argparse
import pprint

# Try this https://stackoverflow.com/a/70026382

parser = argparse.ArgumentParser()
parser.add_argument("channel_id")
args = parser.parse_args()
channel_id = args.channel_id

browser = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)' \
          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.' \
          '0.2661.102 Safari/537.36'

headers = {'User-Agent': browser}

request_url = f"https://youtube.com/channel/{channel_id}/live"

response = requests.get(request_url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
if soup.find("title").text == "404 Not Found":
    print("Channel not found, check channel id")
    exit(0)

stream_url = soup.find("link", {"rel": "canonical"}).get("href")

if "watch" not in stream_url:
    print("Channel has no planned stream yet")
    exit(0)
else:
    print("Next stream found")

response = requests.get(stream_url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
stream_dict = {
        "url": stream_url,
        "title": soup.find("meta", {"name": "title"}).get("content"),
        "time": soup.find("meta", {"itemprop": "startDate"}).get("content"),
        }

pprint.pprint(stream_dict)


