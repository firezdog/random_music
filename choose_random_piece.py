from get_music_list import get_music_list
from random import randint


def get_random_song(music_list):
    random_index = randint(0, len(music_list))
    try:
        piece = music_list[random_index]
        return piece
    except Exception as get_random_song_exception:
        raise get_random_song_exception


if __name__ == "__main__":
    try:
        music_list = get_music_list()
        print(get_random_song(music_list))
    except Exception as get_music_exception:
        print(get_music_exception)
