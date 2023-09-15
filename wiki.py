import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://lv.wikipedia.org'
lang = 'lv'
visited_links = set()
links_to_explore = [f'{base_url}/wiki/Latvija']
with open('latvian_paragraphs.txt', 'a', encoding='utf-8') as f, open('latvian_titles.txt', 'a', encoding='utf-8') as t, open('latvian_sentences.txt', 'a', encoding='utf-8') as s:
    while links_to_explore:
        url = links_to_explore.pop(0)
        if url in visited_links or url.startswith("https://lv.wikipedia.org/wiki/Diskusija") or url.startswith("https://lv.wikipedia.org/wiki/Special") or url.startswith("https://lv.wikipedia.org/wiki/Vikip%C4%93dija") or url.startswith("https://lv.wikipedia.org/wiki/Att%C4%93ls"):
            continue
        visited_links.add(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            title = soup.find(class_='mw-page-title-main').text.strip()
        except:
            title = soup.find(class_='firstHeading mw-first-heading').text.strip()
        text = ' '.join([p.text for p in soup.find_all('p') if not p.find_parent('tr')]).strip()
        text = re.sub(r'\[\d+\]', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\[\d+\]', '', text)
        sentences = re.split(r"(?<=[a-zāčēģīķļņšūž\"']\.)\s*(?=[A-ZĀČĒĢĪĶĻŅŠŪŽ0-9])", text)
        if not sentences or len(sentences)== 1 or len(sentences)== 2 or len(sentences)== 3:
            continue
        words = len(title.split())
        if(words>=2):
            t.write(f'{title}\n')
            f.write(f'{" ".join(sentences[1:6])}\n')
        for sentence in sentences:
            s.write(f'{sentence.strip()}\n')
        new_links = soup.find_all('a', href=True)
        links_to_explore.extend([f'{base_url}{link["href"]}' for link in new_links if link['href'].startswith(f'/wiki/') and not link['href'].startswith('/wiki/Diskusija') and not link['href'].startswith('/wiki/Special') and not link['href'].startswith('/wiki/Vikip%C4%93dija') and not link['href'].startswith('/wiki/Att%C4%93ls')])
