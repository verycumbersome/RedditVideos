from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import urllib2
import json

def youtube_search(item):

  youtube = build("youtube", "v3",
    developerKey="AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA")

  search_response = youtube.search().list(q=item, part="id,snippet", maxResults=6).execute()

  #print search_response

  videoCount = 0;
  title = ""
  channelId = ""
  channelName = ""


  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videoCount += 1
      if videoCount == 1:
         snippet = search_result["snippet"]
         title = snippet["title"]
         videoId = search_result["id"]["videoId"]
         channelId = snippet["channelId"]
         channelTitle = snippet["channelTitle"]
         print channelTitle

  # urlBase = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA&part=snippet&id="
  # if videoCount > 0:
  #    url = urlBase + videoId + ""
  #    r = urllib2.urlopen(url)
  #    metadata = json.load(r)['return']
  #    channelName = metadata["entry"]["author"][0]["name"]["$t"]
  #
  #    print( title, channelId, channelName )

def get_user_from_id(vidId):

  youtube = build("youtube", "v3",
    developerKey="AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA")

  search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

  #print search_response

  videoCount = 0;
  title = ""
  channelId = ""
  channelName = ""

  print search_response["items"][0]["snippet"]["channelTitle"]

youtube_search("h3h3")
get_user_from_id("u_xy1sjKyZc")
