import YoutubeChannelFinder
import TopReddit

from itertools import chain
from collections import Counter

UrlLists = TopReddit.GetTopSubmissions("videos", 1000)
counter = 1
userList = []

for items in UrlLists:
    if counter<len(UrlLists):
        try:
            YoutubeUser = YoutubeChannelFinder.get_user_from_id(UrlLists[counter])
            userList.append(YoutubeUser)
        except IndexError:
            YoutubeUser = ''
        counter +=1
        print counter, len(UrlLists), YoutubeUser
    else:
        None
print Counter(userList)
