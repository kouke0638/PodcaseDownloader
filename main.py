import feedparser
import requests
import os

# RSS Feed URL, replace <YourPodcaseRSSFeedLink> with your own Podcast RSS Feed link
# You can find your Podcast RSS Feed link at https://castos.com/tools/find-podcast-rss-feed/
rss_url = '<YourPodcaseRSSFeedLink>'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Ensure the 'files' directory exists
if not os.path.exists('files'):
    os.makedirs('files')

# Download the MP3 for each episode
for entry in feed.entries:
    mp3_url = entry.enclosures[0]['href']  # Get the URL of the MP3 file
    response = requests.get(mp3_url, stream=True)
    filename = os.path.join('files', f"{entry.title}.mp3")

    # Save the MP3 to a file
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"Downloaded '{entry.title}' to '{filename}'")
