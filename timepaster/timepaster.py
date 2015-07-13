#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import sys
import pyperclip

def gettime():
  """Prompt for input, return minutes since midnight"""
  user_input = raw_input('Enter Start-End (hh:mm-hh:mm): ')
  return user_input

while True:
    timeValues = gettime()
    if timeValues == 'quit':
        print("Goodbye") 
        sys.exit()
        #break
    if timeValues != 'quit':
        try:
            timeStart, timeEnd = timeValues.split('-')
            timeStartH, timeStartM = timeStart.split('.')
            timeEndH, timeEndM = timeEnd.split('.') 
            time1 = int(timeStartM) + 60 * int(timeStartH)
            time2 = int(timeEndM) + 60 * int(timeEndH)
            diff = time2 - time1
            decimal_diff = "%d.%d" % (diff//60, diff%60/6)
            print """
               Duration: %d hrs and %d min
               Decimal difference: %d.%d
               ______________________________
               """ % (diff//60, diff%60, diff//60, diff%60/6)
            pyperclip.copy(decimal_diff)      
        except:
          print("\n               sorry, please use hh:mm-hh:mm, hh.mm-hh.mm or quit\n") 
