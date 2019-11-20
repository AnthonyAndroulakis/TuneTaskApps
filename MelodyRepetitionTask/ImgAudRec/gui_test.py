#!/usr/bin/python

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
import soundcard as sc

defaultRecDevice=str(sc.default_microphone())[12:-14]

participant=open('..\\participant.txt').read()

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

def switch(audiopath,index,roundType):
  ShowImage('audio_resized.jpg') # 1st image: audio_resized.jpg
  process = subprocess.Popen('py playaud.py '+audiopath, shell=True)
  process.wait()
  process.kill()
  ShowImage('green_resized.jpg') # 2nd image: green_resized.jpg
  if roundType == 'practice':
    cmd = 'ffmpeg -f dshow -i audio="'+defaultRecDevice+'" '+'..\\PracticeRecordings\\'+participant+'_'+audiopath[12:-4]+'.wav'
  if roundType == 'tune':
    cmd = 'ffmpeg -f dshow -i audio="'+defaultRecDevice+'" '+'..\\Recordings\\'+participant+'_'+audiopath[13:-4]+'.wav'
  os.system('start "mtapprecording" /min cmd /k '+cmd)
  WaitForKey('space')
  os.system('taskkill /F /FI "WINDOWTITLE eq mtapprecording*" /T')

#######MAIN#######  
listaudio=sys.argv[1:] # arguments for gui_test, ex: py gui_test.py practice1.wav practice2.wav practice3.wav
def allfunc(listaudio):
  if 'practice' in listaudio[0]:
    for i in range(len(listaudio)):
      switch(listaudio[i],i,'practice')
  if 'tune' in listaudio[0]:
    for i in range(len(listaudio)):
      switch(listaudio[i],i,'tune')

allfunc(listaudio)
