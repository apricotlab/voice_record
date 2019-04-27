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
