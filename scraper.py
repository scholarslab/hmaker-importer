from bs4 import BeautifulSoup
import requests
import json

URL_PREFIX = "https://www.thehistorymakers.org"

def getInfo(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("### ERR: request code not 200 for: ", url)
        return None
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    infodiv = soup.find("div","info")
    bio = {}
    for dl in infodiv.find_all("dl"):
        for dt in dl.find_all("dt"):
            bio[dt.text.strip(": ")] = dt.findNext("dd").text.strip()
    biography = soup.find("section","col-sm bio-detail__main-content").find("p")
    bio["Biography"] = biography.get_text()
    return bio

bios = {}
with open("PoliticalMakers.html", 'r') as page:
    html = page.read()
    soup = BeautifulSoup(html, 'html.parser')
    bio_cards = soup.find_all("div","bio-card--list")
    for bio_card in bio_cards:
        name = bio_card.find('a').get('title')
        url = URL_PREFIX+bio_card.find('a').get('href')
        bio = getInfo(url)
        bio["Name"] = name
        bios[url] = bio
        print(url)

with open("PoliticalBios.json", "w") as out:
    json.dump(bios,out)