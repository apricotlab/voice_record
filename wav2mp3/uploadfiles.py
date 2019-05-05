import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./keys/ApricotlabCallCenter-e033714b3c24.json'
client = storage.Client()
bucket = client.get_bucket('ai-sound-apricotlab')

ROOT_PATH = './data/'


def process(file_path):
  print("Uploading the file:" + file_path)
  destination = 'ApricotlabCallCenter/' +  os.path.basename(file_path)
  blob = bucket.blob(destination)
  blob.upload_from_filename(filename=file_path)

def recursive_file_check(path):
    if os.path.isdir(path):
        # directoryだったら中のファイルに対して再帰的にこの関数を実行
        files = os.listdir(path)
        for file in files:
            recursive_file_check(path + file)
    else:
        # mp3だったら処理
      if path[-4:] == '.mp3':
         process(path)


recursive_file_check(ROOT_PATH)
