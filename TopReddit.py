import re
import urllib2
import json
import ast

try:
    import praw
except:
    lib = "PRAW"
    print "ImportError: %s is not found on your system" % (lib)
    print "You must install %s to operate this program" % (lib)
    sys.exit()

r = praw.Reddit(user_agent="",client_secret="-",client_id="",username="",password="")

user = r.redditor("Popular_Channels_Bot")

def DeleteAllSubmissions(username):
    for p in username.submissions.top(limit=None):
        p.delete()
        print 'Post Deleted'

def GetTopSubmissions(subreddit, l):
    SubredditInstance = r.subreddit(subreddit)
    TopOfSub = SubredditInstance.top(limit = l, time_filter='month')

    UrlList = []
    KarmaList = []
    PostUrl = []
    counter = 0

    for item in TopOfSub:
        match = re.search(r"(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})", item.url)

        if match:
            result = match.group(1)
            UrlList.append(result)
            KarmaList.append(item.ups)
            PostUrl.append(item.url)
            counter+=1
        else:
            result = ""
    return UrlList, KarmaList, PostUrl

def PostTopSubmissions(user, name, url):
    popularCreators=r.subreddit('popularcreators')
    popularCreators.submit(user+" - "+name, url=url,selftext=None)

def SearchUserVids(query):
    #urllib2.urlopen(https://www.reddit.com/api/v1/authorize?client_id=RxtcAmhbH9sWCA&response_type=TYPE&state=RANDOM_STRING&redirect_uri=URI&duration=DURATION&scope=SCOPE_STRING).read()
    search_results = json.loads(urllib2.urlopen("https://www.reddit.com/search.json?sort=top&limit=10&q="+query).read())
    with open('search.json', 'a') as outfile:
        for i in range(10):
            json.dump(search_results["data"]["children"][i], outfile, sort_keys = True, indent = 4, separators=(',', ': '))

    with open('search.json') as data_file:
        data = json.load(data_file)
        print data
    return search_results

#print SearchUserVids("pewdiepie")
DeleteAllSubmissions(user)
