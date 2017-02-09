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
print currentdate.day, currentdate.year, currentdate.month
timedifference=currentdate.replace(year=currentdate.year, month=currentdate.month, day=currentdate.day, hour=20, minute=0, second=0, microsecond=0)
delta_t=timedifference-currentdate


secs=delta_t.seconds+1

def GetTopYoutuberList():

    UrlLists, Klist, PostUrl = TopReddit.GetTopSubmissions(args.subreddit, args.limit)
    counter = 1
    usercounter = 1
    userList = []
    new_dictionary = {}

    for items in UrlLists:
        if counter<len(UrlLists):
            try:
                YoutubeUser = {YoutubeChannelFinder.get_user_from_id(UrlLists[counter]):[Klist[counter], PostUrl[counter]]}
                userList.append(YoutubeUser)

            except IndexError:
                YoutubeUser = 'null'
            print counter, "/", len(UrlLists), userList
            counter +=1
        else:
            None

    TopReddit.PostTopSubmissions(PostUrl[1])

    for dictionary in userList:
        for key, value in dictionary.items():
            if new_dictionary.has_key(key):
                new_dictionary[key] = value + new_dictionary[key]
            else:
                new_dictionary[key] = value

    x = Counter(new_dictionary)
    y = OrderedDict(x.most_common())
    print "\n"
    for topUser in y:
        print usercounter, topUser, y.values()[usercounter-1][0]
        usercounter += 1

GetTopYoutuberList()

# t = Timer(secs, GetTopYoutuberList)
# t.start()
