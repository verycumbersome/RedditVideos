from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import urllib2
import json

youtube = build("youtube", "v3",
    developerKey="AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA")

def GetUserFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["channelTitle"]

def GetPlaylistIdFromId(VidId):
    search_response = youtube.videos().list(id=VidId, part="snippet").execute()

    try:
        return search_response["items"][0]["snippet"]["channelId"]
    except IndexError:
        return ""

def GetMostRecentVideo(ChannelId):
    search_response = youtube.channels().list(id=ChannelId, part="contentDetails").execute()

    try:
        playlistId = search_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    except:
        playlistId = ChannelId
    return playlistId #GetRecentVideos["items"][0]["contentDetails"]["videoId"], GetRecentNames["items"][0]["snippet"]["title"]
# def GetMostRecentVideo(ChannelId):
#     GetRecentVideos = youtube.playlistItems().list(playlistId=playlistId, part="contentDetails").execute()
#     GetRecentNames = youtube.playlistItems().list(playlistId=playlistId, part="snippet").execute()
GetMostRecentVideo("UCiY1u58pSv0RH0HYYAJlrBg")
