import YoutubeChannelFinder
import TopReddit

UrlLists = TopReddit.GetTopSubmissions("videos", 100)
counter = 1

for items in UrlLists:
    if counter<len(UrlLists):
        try:
            YoutubeUser = YoutubeChannelFinder.get_user_from_id(UrlLists[counter])
        except IndexError:
            YoutubeUser = 'null'
        counter +=1
        print counter, len(UrlLists), YoutubeUser
    else:
        None
