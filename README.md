# RedditVideos_YoutubeUser
First you need to make a Youtube API key. To do this go to https://console.developers.google.com. Login to your Google accont before creating a project.
Once created, go to the Library tab to the left side of the page and find the Youtube Data API. Click on it and then click enable for it to work.
Next, go into the Credentials tab. Create a new API key and name it whatever you prefer. Then create a new service account and make it a Compute Engine default service account.
After both have been created, go to manage service accounts and then under options for your service account, click create key and select json.
Save the key to your local directory. Next you need to add the environment variable GOOGLE_APPLICATION_CREDENTIALS. To do this you can either type export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/key.json'
or to save it like this for when your computer reboots so you dont have to enter it every time, you can add this line of code to your ~/.bash_profile or ~/.bashrc.
Next replace line 10 in YoutubeChannelFinder.py where it says 'put API key here' with the 'key' part from the API key you generated from the google console. 

Now you'll need to create a Reddit oath2 authorization by going to https://www.reddit.com/prefs/apps and selecting 'create app'. For redirect uri put 'http://localhost'.
In line 10 of TopReddit.py replace 'client_secret' with the client secret from the Reddit app you just created. Replace the 'client_id' with the id for your app(should be right under the name.)
the user_agent can pretty much be whatever you want.

Now everything should be ready to run!
