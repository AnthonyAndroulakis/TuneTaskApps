#!/usr/bin/python

###MADE SPECIFICALLY FOR MELODICPERCEPTIONTASK. DO NOT USE ELSEWHERE.
##GREEN##RED##
import tkinter
import time
import os
import sys
import signal
import linecache
from PIL import ImageTk, Image

import screen
from screen import window
from screen import WaitForKey
from screen import WaitForTime
import subprocess
import pyautogui
import re
import sendkey

participant=open('..\\participant.txt').read()
open('..\\output\\'+participant+'_points.csv','w').close() # clear points.csv file
os.system('echo points, response time >> ..\\output\\'+participant+'_points.csv')

window_width = pyautogui.size().width
window_height = pyautogui.size().height

from utils import ReadFileAsLines

def ChangeLabelText(label, newText):
  label.config(text = newText)
  label.update()


pic = 0
imagePanel = tkinter.Label(window)

def ShowImage(path):
  global window
  global pic
  global imagePanel
  img = Image.open(path)
  img = img.resize((window_width, window_height), Image.ANTIALIAS)
  pic = ImageTk.PhotoImage(img)
  imagePanel.config(image = pic)
  imagePanel.pack(side="bottom", fill="both", expand="yes")
  imagePanel.update()
  pass

def Advance():
  global label
  global lines
  global currentLine
  global window

  ChangeLabelText(label, lines[currentLine])

  currentLine += 1
  if currentLine == len(lines):
    screen. window.destroy()
    return True
  
  return False

def practiceSwitch(): # 0,1,2
  ## 1,2
  ShowImage('1sttune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process = subprocess.Popen('py playaud.py ..\\practicetunes\\tune1.wav', shell=True)
  process.wait()
  process.kill()
  ShowImage('2ndtune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process1 = subprocess.Popen('py playaud.py ..\\practicetunes\\tune2.wav', shell=True)
  process1.wait()
  process1.kill()
  ShowImage('yellow_resized.jpg') # 2nd image: green_resized.jpg
  i=0
  sendkey.sendkey() # sends the s key t  o clear last_key_released of values '1' or '2'
  while i<1000: #wait for 10 seconds, check for keypress every 0.1 second
    keypress=WaitForTime(10)
    print(keypress)
    if keypress=='1' or keypress=='2':
      break
    i=i+1
  
  ## 3,3
  ShowImage('1sttune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process = subprocess.Popen('py playaud.py ..\\practicetunes\\tune3.wav', shell=True)
  process.wait()
  process.kill()
  ShowImage('2ndtune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process1 = subprocess.Popen('py playaud.py ..\\practicetunes\\tune3.wav', shell=True)
  process1.wait()
  process1.kill()
  ShowImage('yellow_resized.jpg') # 2nd image: green_resized.jpg
  i=0
  sendkey.sendkey() # sends the s key t  o clear last_key_released of values '1' or '2'
  while i<1000: #wait for 10 seconds, check for keypress every 0.1 second
    keypress=WaitForTime(10)
    print(keypress)
    if keypress=='1' or keypress=='2':
      break
    i=i+1

  ## 4,5
  ShowImage('1sttune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process = subprocess.Popen('py playaud.py ..\\practicetunes\\tune4.wav', shell=True)
  process.wait()
  process.kill()
  ShowImage('2ndtune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process1 = subprocess.Popen('py playaud.py ..\\practicetunes\\tune5.wav', shell=True)
  process1.wait()
  process1.kill()
  ShowImage('yellow_resized.jpg') # 2nd image: green_resized.jpg
  i=0
  sendkey.sendkey() # sends the s key t  o clear last_key_released of values '1' or '2'
  while i<1000: #wait for 10 seconds, check for keypress every 0.1 second
    keypress=WaitForTime(10)
    print(keypress)
    if keypress=='1' or keypress=='2':
      break
    i=i+1
  
def switch(audiopathOne,index):
  if int(audiopathOne[13:-4]) >= 1 and int(audiopathOne[13:-4]) <= 18: #between 1 and 18
    audiopathTwo=audiopathOne #play the same file
  elif int(audiopathOne[13:-4]) >= 19 and int(audiopathOne[13:-4]) <= 54:
    audiopathTwo='..\\tunes\\tune'+str(int(audiopathOne[13:-4])+1)+'.wav' #play next file
  ShowImage('1sttune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process = subprocess.Popen('py playaud.py '+audiopathOne, shell=True)
  process.wait()
  process.kill()
  ShowImage('2ndtune_resized.jpg')
  WaitForTime(1000)
  ShowImage('audio_resized.jpg')
  process = subprocess.Popen('py playaud.py '+audiopathTwo, shell=True)
  process.wait()
  process.kill()
  ShowImage('yellow_resized.jpg') # 2nd image: green_resized.jpg ###
  before=time.time() #start time = right after yellow screen shows
  #if roundType == 'practice':
  #  cmd = 'ffmpeg -f dshow -i audio="Microphone (Realtek(R) Audio)" '+'..\\PracticeRecordings\\'+participant+'_'+audiopath[12:-4]+'.wav'
  #if roundType == 'tune':
  #  cmd = 'ffmpeg -f dshow -i audio="Microphone (Realtek(R) Audio)" '+'..\\Recordings\\'+participant+'_'+audiopath[13:-4]+letters[index]+'.wav'
  #p1 = subprocess.Popen('start "mtapprecording" /min cmd /C '+cmd, stdout=subprocess.PIPE, shell=True)
  #keypressed=WaitForKey(['1','2'])
  sendkey.sendkey() # sends the s key to clear last_key_released of values '1' or '2'
  i=0
  #while i<1000:
  while time.time()-before < 10: #wait for 10 seconds, check for keypress every 0.1 second
    keypressed=WaitForTime(10)
    print(keypressed)
    if keypressed=='1' or keypressed=='2':
      break
    i=i+1
  #keypressed=WaitForTime(10000) # participant must press key by 10 seconds
  #print(keypressed)
  if keypressed != '1' and keypressed != '2':
    print('no key pressed')
    os.system('echo 9, 10 >> ..\\output\\'+participant+'_points.csv')
  if keypressed=='1': #green pressed
    if int(audiopathOne[13:-4]) >= 1 and int(audiopathOne[13:-4]) <= 18: #correct, case one
      responseTime=time.time()-before #response time
      os.system('echo 1, '+str(responseTime)+' >> ..\\output\\'+participant+'_points.csv')
    elif int(audiopathOne[13:-4]) >= 19 and int(audiopathOne[13:-4]) <= 54: #incorrect, case two
      responseTime=time.time()-before #response time
      os.system('echo 0, '+str(responseTime)+' >> ..\\output\\'+participant+'_points.csv')
  elif keypressed=='2': #red pressed
    if int(audiopathOne[13:-4]) >= 1 and int(audiopathOne[13:-4]) <= 18: #incorrect, case three
      responseTime=time.time()-before #response time
      os.system('echo 0, '+str(responseTime)+' >> ..\\output\\'+participant+'_points.csv')
    elif int(audiopathOne[13:-4]) >= 19 and int(audiopathOne[13:-4]) <= 54: #correct, case four
      responseTime=time.time()-before #response time
      os.system('echo 1, '+str(responseTime)+' >> ..\\output\\'+participant+'_points.csv')

#######MAIN#######  
listaudio=sys.argv[1:] # arguments for gui_test, ex: py gui_test.py practice1.wav practice2.wav practice3.wav
def allfunc(listaudio):
  if 'practice' in listaudio[0]:
    for i in range(len(listaudio)):
      practiceSwitch()
  if 'tune' in listaudio[0]:
    for i in range(len(listaudio)):
      switch(listaudio[i],i)

allfunc(listaudio)
