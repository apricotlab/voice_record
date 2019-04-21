from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pyaudio  #録音機能を使うためのライブラリ
import wave     #wavファイルを扱うためのライブラリ
import os 
import pydub
from pydub import AudioSegment    #wavからmp3
from pydub.playback import play
import asyncio

SOUNDFILE_ROOT = './sound/'
RECORD_SECONDS = 10 #録音する時間の長さ（秒）
iDeviceIndex = 0 #録音デバイスのインデックス番号
 
#基本情報の設定
FORMAT = pyaudio.paInt16 #音声のフォーマット
CHANNELS = 1             #モノラル
RATE = 44100             #サンプルレート
CHUNK = 2**11            #データ点数
FLAG_RECORDING = 0       #録画中フラグ
#audio = pyaudio.PyAudio() #pyaudio.PyAudio()

def button_click_exit():
    sys.exit()


def play_sound(sound):
#    wf = wave.open(sound, "r")
#    # ストリームを開く
#    p = pyaudio.PyAudio()
#    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                    channels=wf.getnchannels(),
#                    rate=wf.getframerate(),
#                    output=True)
#
#    # チャンク単位でストリームに出力し音声を再生
#    chunk = 1024
#    data = wf.readframes(chunk)
#    while data != b'':
#        stream.write(data)
#        data = wf.readframes(chunk)
#    stream.close()
    audio_data = AudioSegment.from_mp3(sound)
    play(audio_data)
    

def show_selection():
    i = 0 
    for i in lb.curselection():
        print(lb.get(i))
    return i


def button_click_play():
#    sound = AudioSegment.from_file("./sound/topic_1.wav", "wav")
    soundfile =SOUNDFILE_ROOT +  filelist[show_selection()] + '.mp3'
    if(os.path.exists(soundfile)):
       print(soundfile)
       play_sound(soundfile) 
    else:
       messagebox.showinfo("Message","録音ファイルがありません")       

def button_click_start():
    global selected_id
    selected_id = show_selection()
    global file_to_create
    file_to_create = SOUNDFILE_ROOT + filelist[selected_id]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(recording_start(file_to_create))
#     recording_start(file_to_create)    


def button_click_stop():
    recording_stop()
    

#def show_selection():
#    for i in lb.curselection():
#        print(lb.get(i))
#    return i

async def recording_start(filename):
    global audio
    audio = pyaudio.PyAudio() #pyaudio.PyAudio()
    global stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index = iDeviceIndex, #録音デバイスのインデックス番号
        frames_per_buffer=CHUNK)
    FLAG_RECORDING = 1
    print ("recording...")
    global frames
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
       data = stream.read(CHUNK)
       frames.append(data)
#       await asyncio.sleep(1)
       if FLAG_RECORDING==0:
            break
    print ("finished recording")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    full_filename = filename + '.wav'
    waveFile = wave.open( full_filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    mp3_filename = filename + '.mp3'
    if(os.path.exists(full_filename)):
      sound = pydub.AudioSegment.from_wav(full_filename)
#       sound.export(mp3_filename,format="mp3")
      sound.export(mp3_filename,codec="libmp3lame")
    if(os.path.exists(mp3_filename)):
      complete_status[selected_id] = '完了'
      lb3.delete(selected_id,selected_id) 
      lb3.insert(selected_id,complete_status[selected_id]) 

async def recording_stop():
      FLAG_RECORDING = 0 


#def refresh_list():
#    for i, name in enumerate(currencies):
#       name = 'topic_' + str(i) + '.wav'
#       if(os.path.exists(SOUNDFILE_ROOT + name)):
#         complete_status[i] = '完了'
#         lb3.delete(i,i) 
#         lb3.insert(i,complete_status[i]) 


if __name__ == '__main__':
    root = Tk()
    root.title('台詞レコーダー')
#    root.geometry("1200x900")


    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()    
#    frame1.grid(column=0, row=0, sticky=(Tk.W + Tk.E))
    root.columnconfigure(0,weight=3,uniform='group1')
    root.columnconfigure(1,weight=1,uniform='group1')
    path = './scenario_sentence.txt'
    with open(path) as f:
#      l = f.readlines()
      currencies = f.readlines()
    
    # Listbox
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=20)
    lb.grid(row=0, column=0)

 # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=1,sticky=(N,S))
 
    filelist = []
    
    for i, name in enumerate(currencies):
       name = 'topic_' + str(i)
       filelist.append(name)

    v2 = StringVar(value=filelist)
    lb2 = Listbox(frame1, listvariable=v2,height=20)
    lb2.grid(row=0, column=2)

 # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb2.yview)
    lb2['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=3,sticky=(N,S))


    complete_status = []
    for i, name in enumerate(currencies):
       if(os.path.exists(SOUNDFILE_ROOT + filelist[i] + '.mp3' )):
         name = '完了'
       else:
         name = '未完了'
       complete_status.append(name)

    v3 = StringVar(value=complete_status)
    lb3 = Listbox(frame1, listvariable=v3,height=20)
    lb3.grid(row=0, column=4)

 # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb3.yview)
    lb3['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=5,sticky=(N,S))

    #Button
    button1 = ttk.Button(frame1, text='録音開始', command=button_click_start)
    button1.grid(row=1, column=0, columnspan=3)
   

    #Button
    button2 = ttk.Button(frame1, text='録音ストップ', command=button_click_stop)
    button2.grid(row=2, column=0, columnspan=3)


    #Button
    button3 = ttk.Button(frame1, text='再生', command=button_click_play)
    button3.grid(row=3, column=0, columnspan=3)

    #Button
    button4 = ttk.Button(frame1, text='終了', command=button_click_exit)
    button4.grid(row=3, column=4, columnspan=3)
    
    
root.mainloop()
