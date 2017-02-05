import YoutubeChannelFinder
import TopReddit
import argparse

from itertools import chain
from collections import Counter, OrderedDict

parser = argparse.ArgumentParser(description='argparser for Python code')
parser.add_argument('--limit', help='sets subreddit top get limit', type=int)
parser.add_argument('--subreddit', help='sets subreddit from which to get top youtube users')
args = parser.parse_args()

UrlLists = TopReddit.GetTopSubmissions(args.subreddit, args.limit)
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
x = Counter(userList)
y = OrderedDict(x.most_common())
print y
