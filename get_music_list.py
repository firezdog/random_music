import csv
import requests
from bs4 import BeautifulSoup

# () => list
def get_music_list():
    soup = BeautifulSoup(get_content(), 'html.parser')
    music_rows = soup.find_all('tr')
    music = []
    for mr in music_rows:
        try:
            music.append(mr.select('td')[1].get_text(strip=True))
        except Exception as parsed_format_exception:
            raise parsed_format_exception
    write_music_csv(music)
    return music


# () => request object
def get_content():
    try:
        return requests.get('https://www.classicfm.com/classical-100/full-list/').content
    except Exception as get_content_exception:
        raise get_content_exception


# () => void (write csv file)
def write_music_csv(music):
    try:
        with open('music.csv', encoding='utf-16', mode='w') as music_file:
            music_writer = csv.writer(music_file)
            [music_writer.writerow([piece]) for piece in music]
    except Exception as write_music_exception:
        raise write_music_exception
