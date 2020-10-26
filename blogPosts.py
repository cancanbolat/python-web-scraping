import requests
from bs4 import BeautifulSoup as bs4

headers_p = {"User-Agent":"{your-user-agent}"}

site_content = requests.get('https://pythonwebscraping.blogspot.com/', headers=headers_p)

site = site_content.content
soup = bs4(site, "html.parser")

# post title
titles = soup.find_all("h3", {"class":"post-title entry-title"})
for data in titles:
    print(data.text.strip()) 

# post image url
image_urls = soup.find_all("div", {"class":"separator"})
for data in image_urls:
    print(data.a['href']) 

# post date
dates = soup.find_all("a", {"class":"timestamp-link"})
for data in dates:
    print(data.abbr.text)

# post comment
comments = soup.find_all("a", {"class":"comment-link"})
for data in comments:
    print(data.text.strip()+" "+data['href']) 


