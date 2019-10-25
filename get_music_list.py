import csv
import requests
from bs4 import BeautifulSoup


# () => list
def get_music_list():
    soup = BeautifulSoup(get_content(), 'html.parser')
    music_rows = soup.find_all('tr')
    music = []
    for mr in music_rows:
        music.append(mr.select('td')[1].get_text(strip=True))
    write_music_csv(music)
    return music


# () => request object
def get_content():
    return requests.get('https://www.classicfm.com/classical-100/full-list/').content


# () => void (write csv file)
def write_music_csv(music):
    with open('music.csv', encoding='utf-16', mode='w') as music_file:
        music_writer = csv.writer(music_file)
        for piece in music[1:]:
            music_writer.writerow([piece])
