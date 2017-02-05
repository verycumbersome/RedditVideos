import YoutubeChannelFinder
import TopReddit
import argparse

from itertools import chain
from collections import Counter, OrderedDict

parser = argparse.ArgumentParser(description='argparser for Python code')
parser.add_argument('--limit', help='sets subreddit top get limit', type=int)
parser.add_argument('--subreddit', help='sets subreddit from which to get top youtube users')
args = parser.parse_args()

UrlLists, Klist = TopReddit.GetTopSubmissions(args.subreddit, args.limit)
counter = 1
userList = []
new_dictionary = {}

for items in UrlLists:
    if counter<len(UrlLists):
        try:
            YoutubeUser = {YoutubeChannelFinder.get_user_from_id(UrlLists[counter]): Klist[counter]}
            userList.append(YoutubeUser)

        except IndexError:
            YoutubeUser = 'null'
        print counter, "/", len(UrlLists), YoutubeUser
        counter +=1
    else:
        None

for dictionary in userList:
    for key, value in dictionary.items():
        if new_dictionary.has_key(key):
            new_dictionary[key] = value + new_dictionary[key]
        else:
            new_dictionary[key] = value

x = Counter(new_dictionary)
y = OrderedDict(x.most_common())
print y
