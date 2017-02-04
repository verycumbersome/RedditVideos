from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import urllib2
import json

def get_user_from_id(vidId):

  youtube = build("youtube", "v3",
    developerKey="AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA")

  search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

  return search_response["items"][0]["snippet"]["channelTitle"]

#get_user_from_id("u_xy1sjKyZc")
