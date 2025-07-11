#!/usr/bin/env micropython
# krs id and baud rate scanner
# 2025.7.8
# by T.Nishimura of AiRRC
#

from krs_driver_for_scaner import *
print('Start KRS Scan')
krs=KRSdriver()
baud=[115200,625000,1250000]
#
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
  print('Start KRS mode change')
  sid,baud_r=read_baud()
  read_buf=krs.read_memory(sid)
  print("a=",sid,baud_r,read_buf[16])
#
  print("Change Mode")
  write_buf=bytearray(read_buf)
  if read_buf[16]==1:
      print("Change to Wheel Mode")
      write_buf[16]=0x0 # Angle mode
  else:
      print("Change to Angle Mode")
      write_buf[16]=0x1 # Wheel mode
#  
  print(krs.write_memory(sid,write_buf))
#
  read_buf=krs.read_memory(sid)
  print("mode= to ",read_buf[15])
#
if __name__ == '__main__':
    main()
#