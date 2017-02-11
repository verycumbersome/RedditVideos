import re
try:
    import praw
except:
    lib = "PRAW"
    print "ImportError: %s is not found on your system" % (lib)
    print "You must install %s to operate this program" % (lib)
    sys.exit()

r = praw.Reddit(user_agent="Popular_Creators_Bot",client_secret="-XFcJKpyFCrrkib_OU_ylL5bLkM",client_id="RxtcAmhbH9sWCA",username="Popular_Channels_Bot",password="Vh3-89G-Pv9-aoy")

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
