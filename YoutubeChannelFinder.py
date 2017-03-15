from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import re

youtube = build("youtube", "v3",
    developerKey="")

def GetUserFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["channelTitle"]

def GetUserNameFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["channelId"]

def GetVidNameFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["title"]

def GetCategoryId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()
    categoryId = search_response["items"][0]["snippet"]["categoryId"]

    return youtube.videoCategories().list(id=categoryId, part="snippet").execute()["items"][0]["snippet"]["title"]

def GetSubCountFromId(channelId):
    search_response = youtube.channels().list(id=channelId, part="statistics").execute()

    try:
        return search_response["items"][0]["statistics"]["subscriberCount"]
    except IndexError:
        print "FUCKED UP"
        return ""

def GetMostRecentVideo(ChannelId):
    search_response = youtube.channels().list(id=ChannelId, part="contentDetails").execute()

    try:
        playlistId = search_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    except:
        playlistId = ChannelId
        print "Something went wrong"
    return playlistId

def GetMostRecentPlaylistVideo(playlistId):
    try:
        GetRecentVideos = youtube.playlistItems().list(playlistId=playlistId, part="contentDetails").execute()
        GetRecentNames = youtube.playlistItems().list(playlistId=playlistId, part="snippet").execute()

        return GetRecentVideos["items"][0]["contentDetails"]["videoId"], GetRecentNames["items"][0]["snippet"]["title"]
    except IndexError:
        GetRecentVideos = playlistId
        return ""
