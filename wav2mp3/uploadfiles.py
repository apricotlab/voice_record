import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./ApricotlabCallCenter-e033714b3c24.json'
client = storage.Client()
bucket = client.get_bucket('ai-sound-apricotlab')

blob = bucket.blob('ApricotlabCallCenter/welcome01.wav')
blob.upload_from_filename(filename='./welcome01.wav')

#アップロードしたファイルをダウンロード
#blob2 = bucket.get_blob('取得ファイル名')
#print(blob2.download_as_string())

