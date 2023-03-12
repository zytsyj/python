import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"
}
for num in range(0,250,25):
    response = requests.get(f"https://movie.douban.com/top250?start={num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        stringtitle = title.string
        if "/" not in stringtitle:
            print(stringtitle)


