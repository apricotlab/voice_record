# voice_record
Utility to record phrase

mac OS High Sierra  version  10.13.2
<br>
Amaconda

The following is ncessary to run ffmpeg part (to convert WAV to mp3) properly.

$brew install ffmpeg

$export PATH=/usr/local/bin:$PATH


How to run

python voice_record.py

<h1> Voice Record Web </h1>

<h2>How to set up</h2>

NOTE:Use firefox when you run this application from brower.<br>

Download<br>
https://github.com/cwilso/AudioRecorder

<h2>Preparation</h2>

Under the downloaded directory do the following

<PRE>
$ npm init -y
$ npm i http-server -D
$ vi package.json
{
  "name": "exp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "http-server -o"           <===== modifiy this line like this
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "http-server": "^0.7.4"
  }
}

$ npm start
</PRE>

From Firefox Browser <br>

http://127.0.0.1:8080



Reference
https://qiita.com/okunokentaro/items/0658f4a6c75270da726a


<h1>wav2mp3</h1>

Batch conversion from WAV to mp3

<b>How to prepare</b>
export PATH=/usr/local/bin:$PATH<br>
python -m pip install pydub<br>

<b>How to run</b>
Place wav2mp3.py in the directory where the .wav files exist.<br>
Then run the following:<br>
python3 wav2mp3.py
 
 


<h1>Dialogflow and Webhook to invoke IFTTT</h1>

Define:  IF this (Webhook), then that (LINE Message)

IFTTT<br>
https://ifttt.com/discover



<h2>Twilio Integration</h2>

Referance<br>

https://senyoltw.hatenablog.jp/entry/2018/11/18/183843


<h1>Google Cloud Storage file transfer</h1>

Reference:https://sleepless-se.net/2018/05/22/googlecloudstorage%E3%81%A7python%E3%81%8B%E3%82%89%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E3%82%84%E3%82%8A%E3%81%A8%E3%82%8A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/ <br>

If You encoutner:  ImportError: No module named 'google'  Error, follow the last comment of this article<br>
https://stackoverflow.com/questions/36183486/importerror-no-module-named-google

pip install google.cloud.bigquery
pip install google.cloud.storage


<h1>Creating intent thru API</h1>

On Google Cloud Platform Console<br>
Provide the Administrator role to the following member in IAM.<br>
dialogflow-utyfrq@apricotlabcallcenter.iam.gserviceaccount.com

From terminal<BR>
Specify the key file thru environment value:<br>
export GOOGLE_APPLICATION_CREDENTIALS=./ApricotlabCallCenter-XXXXXXXXXXXXXXX.json
