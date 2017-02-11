from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import re

youtube = build("youtube", "v3",
    developerKey="AIzaSyCyQN74f1KDl5NsjG9OP48_9DVcuDVEOYA")

def GetUserFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["channelTitle"]

def GetUserNameFromId(vidId):
    search_response = youtube.videos().list(id=vidId, part="id,snippet").execute()

    return search_response["items"][0]["snippet"]["channelId"]

def GetUserFromUrl(url):
    match = re.search(r"(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})", url)

    if match:
        result = match.group(1)

    search_response = youtube.videos().list(id=result, part="id,snippet").execute()
    return search_response["items"][0]["snippet"]["channelId"]

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
        print "SOmething went wrong"
    return playlistId

def GetMostRecentPlaylistVideo(playlistId):
    try:
        GetRecentVideos = youtube.playlistItems().list(playlistId=playlistId, part="contentDetails").execute()
        GetRecentNames = youtube.playlistItems().list(playlistId=playlistId, part="snippet").execute()

        return GetRecentVideos["items"][0]["contentDetails"]["videoId"], GetRecentNames["items"][0]["snippet"]["title"]
    except IndexError:
        GetRecentVideos = playlistId
        return ""
