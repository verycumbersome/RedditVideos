import YoutubeChannelFinder
import TopReddit
import argparse
import threading
import json

from itertools import chain
from collections import Counter, OrderedDict
from datetime import datetime
from threading import Timer

parser = argparse.ArgumentParser(description='argparser for Python code')
parser.add_argument('-l', '--limit', help='sets subreddit top get limit', type=int, default=1000)
parser.add_argument('-s', '--subreddit', help='sets subreddit from which to get top youtube users', default="videos")
parser.add_argument('-p', '--postnumber', help='sets the number of videos to post to subreddit', type=int, default=8)
parser.add_argument('-y', '--karmalimit', help='sets the minimum subscriber value for Youtube in order for it to be posted to subreddit', type=int)
args = parser.parse_args()

currentdate=datetime.today()
timedifference=currentdate.replace(year=currentdate.year, month=currentdate.month, day=currentdate.day, hour=20, minute=0, second=0, microsecond=0)
delta_t=timedifference-currentdate


secs=delta_t.seconds+1

def GetTopYoutuberList():

    UrlLists, Klist, PostUrl = TopReddit.GetTopSubmissions(args.subreddit, args.limit)
    counter = 1
    usercounter = 0
    additionalRequests = 0

    userList = []
    OrderedDictionary = {}
    MostRecentYoutubePost = []
    MostRecentYoutubeName = []
    YoutubeUsername = []


    for items in UrlLists:
        if counter<len(UrlLists):
            try:
                YoutubeUser = {YoutubeChannelFinder.GetUserNameFromId(UrlLists[counter]):Klist[counter]}

                userList.append(YoutubeUser)

            except IndexError:
                YoutubeUser = 'null'
            print counter, "/", len(UrlLists), YoutubeUser
            counter +=1
        else:
            None

    #Appends all karma scores in dictionary to one key per user
    for dictionary in userList:
        for key, value in dictionary.items():
            if OrderedDictionary.has_key(key):
                OrderedDictionary[key] = value + OrderedDictionary[key]

            else:
                OrderedDictionary[key] = value

    postFreq = Counter(OrderedDictionary.items())

    #Sorts the dictionary of all Youtube channel IDs by the associated karma value
    x = Counter(OrderedDictionary)
    y = OrderedDict(x.most_common())

    while (usercounter <= (args.postnumber + additionalRequests)):
        try:
            #Finds the uploads playlist for the userList
            YoutubeChannel = YoutubeChannelFinder.GetMostRecentVideo(y.keys()[usercounter])

            #Finds the most recent video from the uploads playlist
            recentId = YoutubeChannelFinder.GetMostRecentPlaylistVideo(YoutubeChannel)

            #Finds the subscriber count on Youtube of the channel
            subCount = int(YoutubeChannelFinder.GetSubCountFromId(y.keys()[usercounter]))

            #VideoId for recent posts from playlist 'uploads'
            MostRecentYoutubePost.append(recentId[0])

            #Video names for recent posts in playlist 'uploads'
            MostRecentYoutubeName.append(recentId[1])

            category = YoutubeChannelFinder.GetCategoryId(MostRecentYoutubePost[usercounter])

            print usercounter, recentId[1], y.values()[usercounter], YoutubeChannelFinder.GetUserFromId(MostRecentYoutubePost[usercounter]), subCount, YoutubeChannelFinder.GetCategoryId(MostRecentYoutubePost[usercounter])

            #filter for channel making it to approved submitters
            if subCount>30000 and category not in ["Entertainment", "Howto & Style", "News & Politics"] and y.values()[usercounter]>10000:
                YoutubeUsername.append({YoutubeChannelFinder.GetUserFromId(MostRecentYoutubePost[usercounter]): "https://www.youtube.com/watch?v=" + MostRecentYoutubePost[usercounter]})

                with open('data/youtubers.json', 'w') as outfile:
                    json.dump(YoutubeUsername, outfile, sort_keys = True, indent = 4)

                print "valid", usercounter
            else:
                additionalRequests+=1
                print "invalid"

            usercounter += 1

        except IndexError:
            break

GetTopYoutuberList()

# t = Timer(secs, GetTopYoutuberList)
# t.start()
