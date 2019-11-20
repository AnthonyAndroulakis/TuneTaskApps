#!/usr/bin/python

import tkinter
import time
import os
import pyautogui

# Globals
window_width = pyautogui.size().width
window_height = pyautogui.size().height
keysym = ""

def TimerFired():
  global waitForTime
  waitForTime.set(waitForTime.get() + 1)
  pass

def WaitForTime(milliseconds):
  global waitForTime
  global window
  window.after(milliseconds, TimerFired)
  window.wait_variable(waitForTime)
  pass

def WaitForKey(key):
  global waitForVar

  keysym = ""
  window.wait_variable(waitForVar)
  window.update_idletasks()
  if keysym == key:
    return

def MainWindowEventHandler(event):
  global label
  global window
  global waitForVar

  waitForVar.set(waitForVar.get() + 1)
  keysym = event.keysym
  print(keysym)

window = tkinter.Tk()
# tkinter
# window.attributes("-fullscreen", True)
# window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.geometry(str(window_width) + 'x' + str(window_height))
window.configure(background='black')
window.bind_all('<KeyRelease>', MainWindowEventHandler)

waitForTime = tkinter.IntVar()
waitForVar = tkinter.IntVar()
