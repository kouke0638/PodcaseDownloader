import feedparser
import requests
import os

# RSS Feed URL，請將 <YourPodcaseRSSFeedLink> 替換成你的 Podcast RSS Feed 連結
# 可以從 https://castos.com/tools/find-podcast-rss-feed/ 找到你的 Podcast RSS Feed 連結
rss_url = '<YourPodcaseRSSFeedLink>'

# 解析 RSS feed
feed = feedparser.parse(rss_url)

# 確保 'files' 資料夾存在
if not os.path.exists('files'):
    os.makedirs('files')

# 下載每一個集的 MP3
for entry in feed.entries:
    mp3_url = entry.enclosures[0]['href']  # 獲取 MP3 檔案的 URL
    response = requests.get(mp3_url, stream=True)
    filename = os.path.join('files', f"{entry.title}.mp3")

    # 將 MP3 保存到檔案
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"Downloaded '{entry.title}' to '{filename}'")
