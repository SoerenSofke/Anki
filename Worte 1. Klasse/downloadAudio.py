import requests
from bs4 import BeautifulSoup

fname = 'worte.txt'

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'
}

with open(fname, encoding="utf-8") as f:
    phrases = f.read().splitlines()

for phrase in phrases:
    phrase = phrase.replace('/', ',')
    words = phrase.split(' ')

    matches = {"der", "die", "das"}
    if matches.intersection(set(words)):
        word = words[1]
    else:        
        word = words[0]

    print(word) 


    url = 'https://de.wiktionary.org/wiki/' + word
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all(title='De-' + word + '.ogg'):
        print(link.get('href'))

        url = 'http:' + link.get('href')
        r = requests.get(url, headers=headers)
        
        filename = 'audio/' + phrase + '.ogg'
        with open(filename, "wb") as o:
            o.write(r.content)
        
        break
