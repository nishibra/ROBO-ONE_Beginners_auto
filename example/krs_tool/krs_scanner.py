#!/usr/bin/env micropython
# krs id and baud rate scanner
# 2025.6.21
# by T.Nishimura of AiRRC
#
#import time
from krs_driver_for_scaner import *
print('Start KRS Scan')
krs=KRSdriver()
baud=[115200,625000,1250000]
def main():
  try:   
    krs.con = UART(1, baudrate=baud[0], tx=Pin(8), rx=Pin(9))
    print("baud rate=",baud[0]," id=",krs.id_read())
  except:
    try:
      krs.con = UART(1, baudrate=baud[1], tx=Pin(8), rx=Pin(9))
      print("baud rate=",baud[1]," id=",krs.id_read())
    except:
      try:
        krs.con = UART(1, baudrate=baud[2], tx=Pin(8), rx=Pin(9))
        print("baud rate=",baud[2]," id=",krs.id_read())
      except:
        print("no servo")
#
if __name__ == '__main__':
    main()
#