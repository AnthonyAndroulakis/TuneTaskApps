#!/usr/bin/python

import tkinter
import time
import os

def ReadFileAsLines(path):
  with open(path) as f:
    lines = f.read().splitlines()
  return lines
