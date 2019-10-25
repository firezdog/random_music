import csv
from os.path import exists
from random import randint
import webbrowser
from get_music_list import get_music_list


def get_random_song(music_list):
    random_index = randint(0, len(music_list))
    piece = music_list[random_index]
    return piece[0]


def get_pieces():
    if not exists('music.csv'):
        get_music_list()
    with open('music.csv', encoding='utf-16') as music_file:
        pieces = []
        csv_reader = csv.reader(music_file)
        for row in csv_reader:
            pieces.append(row)
        return pieces


if __name__ == "__main__":
    song = get_random_song(get_pieces()).encode('ascii', 'ignore').decode('ascii')
    webbrowser.register('google-chrome', webbrowser.Chrome('google-chrome'))
    try:
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query={}'.format(song))
    except Exception as search_exception:
        print('Error while trying to search for song {}'.format(song))
        print(search_exception)
