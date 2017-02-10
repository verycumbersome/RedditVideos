import YoutubeChannelFinder
import TopReddit
import argparse
import threading

from itertools import chain
from collections import Counter, OrderedDict
from datetime import datetime
from threading import Timer

parser = argparse.ArgumentParser(description='argparser for Python code')
parser.add_argument('--limit', help='sets subreddit top get limit', type=int)
parser.add_argument('--subreddit', help='sets subreddit from which to get top youtube users')
args = parser.parse_args()

currentdate=datetime.today()
timedifference=currentdate.replace(year=currentdate.year, month=currentdate.month, day=currentdate.day, hour=20, minute=0, second=0, microsecond=0)
delta_t=timedifference-currentdate


secs=delta_t.seconds+1

def GetTopYoutuberList():

    UrlLists, Klist, PostUrl = TopReddit.GetTopSubmissions(args.subreddit, args.limit)
    counter = 1
    usercounter = 0
    userList = []
    userUrl = []
    OrderedDictionary = {}
    MostRecentYoutubePost = []
    MostRecentYoutubeName = []


    for items in UrlLists:
        if counter<len(UrlLists):
            try:
                YoutubeUser = {YoutubeChannelFinder.GetUserFromId(UrlLists[counter]):[Klist[counter], PostUrl[counter]]}

                userList.append(YoutubeUser)


            except IndexError:
                YoutubeUser = 'null'
            print counter, "/", len(UrlLists), YoutubeUser
            counter +=1
        else:
            None

    for dictionary in userList:
        for key, value in dictionary.items():
            if OrderedDictionary.has_key(key):
                OrderedDictionary[key] = value + OrderedDictionary[key]
            else:
                OrderedDictionary[key] = value
    print "\n", OrderedDictionary
    x = Counter(OrderedDictionary)
    y = OrderedDict(x.most_common())
    print y.keys()[0]
    print "\n"
    for topUser in y:
        YoutubeChannel = YoutubeChannelFinder.GetPlaylistIdFromId(UrlLists[usercounter])
        print usercounter+1, topUser, y.values()[usercounter], YoutubeChannelFinder.GetMostRecentVideo(YoutubeChannelFinder.GetPlaylistIdFromId(UrlLists[usercounter]))
        usercounter += 1

    # for i in range(10):
    #     print y.keys()[0], "THIS IS KEYS "
    #     try:
    #         YoutuberId = YoutubeChannelFinder.GetIdFromUsername()
    #     except IndexError:
    #         YoutuberId = "ProZd"
    #     Playlist, VidName = YoutubeChannelFinder.GetMostRecentVideo(YoutuberId)
    #
    #     MostRecentYoutubePost.append(Playlist)
    #     MostRecentYoutubeName.append(VidName)
    #
    #     TopReddit.PostTopSubmissions(MostRecentYoutubeName[i], "https://www.youtube.com/watch?v=" + MostRecentYoutubePost[i])
GetTopYoutuberList()

# t = Timer(secs, GetTopYoutuberList)
# t.start()
