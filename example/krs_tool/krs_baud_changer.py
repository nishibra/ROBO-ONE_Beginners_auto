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
#
def b2b(by):
  if by==0:
      print("Baud=",baud[2])
      ba=2
  elif by==1:
      print("Baud=",baud[1])
      ba=1
  elif by==10:
      print("Baud=",baud[0])
      ba=0
  return baud[ba]

def read_baud():
  try:   
    krs.con = UART(1, baudrate=baud[0], tx=Pin(8), rx=Pin(9))
    sid=krs.id_read()
    print("baud rate=",baud[0]," id=",sid)
    baudr=baud[0]
  except:
    try:
      krs.con = UART(1, baudrate=baud[1], tx=Pin(8), rx=Pin(9))
      sid=krs.id_read()
      print("baud rate=",baud[1]," id=",sid)
      baudr=baud[1]
    except:
      try:
        krs.con = UART(1, baudrate=baud[2], tx=Pin(8), rx=Pin(9))
        sid=krs.id_read()
        print("baud rate=",baud[2]," id=",sid)
        baudr=baud[2]
      except:
        print("no servo")
        baudr=0
  return (sid,baudr)
#
def main():
  print('Start KRS baudrate change')
  sid,baud_r=read_baud()
  read_buf=krs.read_memory(sid)
  print("a=",sid,baud_r,read_buf)
#
  print("chg baud to 1250000")
  write_buf=bytearray(read_buf)
  write_buf[29]=0x0  #set 1250000
#  
  print(krs.write_memory(sid,write_buf))
  krs.con = UART(1, baudrate=1250000, tx=Pin(8), rx=Pin(9))
  read_buf=krs.read_memory(sid)
  print("baudrate=",baud_r," to ",b2b(read_buf[29]))
  
  time.sleep(1)
  print("id ",sid,"=",krs.read_position_set_free(sid))
#
if __name__ == '__main__':
    main()
#