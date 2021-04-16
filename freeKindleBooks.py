# PRAW (Python Reddit API Wrapper) can be installed using the console command 'pip install praw'
import praw
import webbrowser

browser_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
browser = webbrowser.get(browser_path)

# myInfo.txt contains the private key for the API to work along with my Reddit username and password, each on its own line
# If you are planning on using the script, you can grab your own API key from https://reddit.com/prefs/apps and scrolling to the bottom
# where you can register for a free key.
with open('myInfo.txt', 'r') as f:
    lines = f.read().splitlines()
    secret_id = lines[0]
    un = lines[1]
    pw = lines[2]

# Rather than putting your key, username, and password in a separate text document like I did, you can instead, directly enter the info
# in the parameters bellow, replacing the client_id if yours differs
reddit = praw.Reddit(
    client_id = 'qDduOWV0mkXzmQ',
    client_secret = secret_id,
    user_agent = 'FreeKindleBooks',
    username = un,
    password = pw
)

# specifies the r/KindleFreebies subreddit that we will be looking through
subreddit = reddit.subreddit("kindlefreebies")

availableLinks = list()

# limits the number of results to 10 and filters to the hot posts
for submission in subreddit.hot(limit = 10):
    
    # Filters out self-posts (text-only posts)
    if not submission.is_self:
        kindleLink = submission.url
        
        # Checks if url is an Amazon link
        if 'www.amazon.com' in kindleLink:
            availableLinks.append(kindleLink)
    
open_in_browser = input('Would you like to open the links in your default browser (Y/N)?  ')

if open_in_browser.upper() == 'Y':
    for link in availableLinks:
        browser.open_new_tab(link)
else:
    for link in availableLinks:
        print(link)