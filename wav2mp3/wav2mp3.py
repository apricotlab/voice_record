import pydub
import os


# Article https://qiita.com/hasepy/items/8e6a0757da1ce074ce87

ROOT_PATH = './data/'


def process(file_path):
   print('Converting wav to mp3: ' + file_path)
   mp3file_path = file_path.replace(".wav",".mp3")
   sound = pydub.AudioSegment.from_wav(file_path)
#   sound.export(mp3file_path, format="mp3")
   sound.export(mp3file_path, codec="libmp3lame")


def recursive_file_check(path):
    if os.path.isdir(path):
        # directoryだったら中のファイルに対して再帰的にこの関数を実行
        files = os.listdir(path)
        for file in files:
            recursive_file_check(path + file)
    else:
      if path[-4:] == '.wav':
         process(path)


recursive_file_check(ROOT_PATH)


