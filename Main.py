import YoutubeChannelFinder
import TopReddit
import argparse
import threading

from itertools import chain
from collections import Counter, OrderedDict
from datetime import datetime
from threading import Timer

parser = argparse.ArgumentParser(description='argparser for Python code')
parser.add_argument('-l', '--limit', help='sets subreddit top get limit', type=int)
parser.add_argument('-s', '--subreddit', help='sets subreddit from which to get top youtube users')
parser.add_argument('-p', '--postnumber', help='sets the number of videos to post to subreddit')
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
                #YoutubeUser = {YoutubeChannelFinder.GetUserFromId(UrlLists[counter]):[Klist[counter], PostUrl[counter]]}
                YoutubeUser = {YoutubeChannelFinder.GetUserNameFromId(UrlLists[counter]):Klist[counter]}

                userList.append(YoutubeUser)


            except IndexError:
                YoutubeUser = 'null'
            print counter, "/", len(UrlLists), YoutubeUser
            counter +=1
        else:
            None
    #sum(item['gold'] for item in myLIst)
    for dictionary in userList:
        for key, value in dictionary.items():
            if OrderedDictionary.has_key(key):
                OrderedDictionary[key] = value + OrderedDictionary[key]
                print OrderedDictionary[key]
            else:
                OrderedDictionary[key] = value
    x = Counter(OrderedDictionary)
    y = OrderedDict(x.most_common())
    for i in range(args.postnumber):
        try:
            YoutubeChannel = YoutubeChannelFinder.GetMostRecentVideo(y.keys()[usercounter])
            recentId = YoutubeChannelFinder.GetMostRecentPlaylistVideo(YoutubeChannel)

            MostRecentYoutubePost.append(recentId[0])
            MostRecentYoutubeName.append(recentId[1])

            print usercounter, recentId[1], y.values()[usercounter]
            usercounter += 1
            TopReddit.PostTopSubmissions(MostRecentYoutubeName[i], "https://www.youtube.com/watch?v=" + MostRecentYoutubePost[i], i)
        except IndexError:
            None
GetTopYoutuberList()

# t = Timer(secs, GetTopYoutuberList)
# t.start()
