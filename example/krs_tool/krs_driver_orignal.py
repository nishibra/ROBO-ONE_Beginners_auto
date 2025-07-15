#!/usr/bin/env python
# Kondo KRS servo control program
# 2020.03.24
# by T.Nishimura
#---------------------------------
import serial, time
# initialize
buf2=bytearray(2)
buf3=bytearray(3)
buf4=bytearray(4)
#buf66=bytearray(66)
temp_=bytearray(2)
# serial
con = serial.Serial()
con.port='/dev/ttyAMA0'  #for RasPi4
#con.port='/dev/ttyUSB0'  #for PC
#con.port='/dev/ttyS1'  #for Tinker
con.baudrate=115200  #1250000 / 625000 / 115200
con.bytesize=8
con.parity=serial.PARITY_EVEN
con.stopbits=1
con.timeout=0.5
# try:
con.open()
# except:
#    print "comm port erorr"
#---------------------------------
# set angle fo slave mode
def set_angle(sid,tangle):
  if tangle==0:
      tangle=0
  elif(tangle>11500):
      tangle=11500
  elif(tangle<3500 ):
      tangle=3500
  cmd1=sid&0x1f
  cmd=0x80+cmd1
  buf3[0]=cmd  #cmd+id
  buf3[1]=(tangle>>7)&0x7f
  buf3[2]=tangle&0x7f
  con.write(buf3)
  rcv = [ord(i) for i in con.read(6)]
  print rcv
#---------------------------------
# for ICS3.5
def set_read_angle(sid,tangle):
  if tangle==0:
      tangle=0
  elif(tangle>11500):
      tangle=11500
  elif(tangle<3500 ):
      tangle=3500
  cmd1=sid&0x1f
  cmd=0x80+cmd1
  buf3[0]=cmd #cmd+id
  buf3[1]=(tangle>>7)&0x7f
  buf3[2]=tangle&0x7f
  con.write(buf3)

  #rcv = [ord(i) for i in con.read(6)]
  #print "rrr=",rcv

  buf_read=con.read(6)
  if (len(buf_read)==6):
     temp_[0]=ord(buf_read[4])
     temp_[1]=ord(buf_read[5])
     val=temp_[1]|(temp_[0]<<7)
     #print "get %d" %(val)
     return(val)
  else:
    print ("angle read error")
    return(0)
#---------------------------------
# set current
def current_set(sid,curr):
  cmd1=sid&0x1f 
  cmd=0xC0+cmd1
  buf3[0]=cmd #cmd+id
  buf3[1]=0x03
  buf3[2]=curr&0xFF
  con.write(buf3)
  buf_read=con.read(6)
  if (len(buf_read)==6):
     val=ord(buf_read[5])
     return(val)
  else:
    print ("current read error")
    return(0)
#---------------------------------
# set speed 1-127
def speed_set(sid,spd):
  cmd1=sid&0x1f 
  cmd=0xC0+cmd1
  buf3[0]=cmd #cmd+id
  buf3[1]=0x02
  buf3[2]=spd&0xFF
  con.write(buf3)
  buf_read=con.read(6)
  if (len(buf_read)==6):
     val=ord(buf_read[5])
     return(val)
  else:
    print ("speed read error")
    return(0)
#---------------------------------
# set strech  1-127
def strech_set(sid,strc):
  cmd1=sid&0x1f 
  cmd=0xC0+cmd1
  buf3[0]=cmd #cmd+id
  buf3[1]=0x01
  buf3[2]=strc&0xFF
  con.write(buf3)
  buf_read=con.read(6)
  if (len(buf_read)==6):
     val=ord(buf_read[5])
     return(val)
  else:
    print ("speed read error")
    return(0)
#---------------------------------
# read temp
def temp_set(sid):
  cmd1=sid&0x1f 
  cmd=0xA0+cmd1
  buf2[0]=cmd #cmd+id
  buf2[1]=0x04

  con.write(buf2)
  buf_read=con.read(5)
  if (len(buf_read)==5):
     val=ord(buf_read[4])
     return(val)
  else:
    print ("Temp. read error")
    return(0)
#---------------------------------
def read_angle(sid):  #for ics3.6
  cmd1=sid&0x1f 
  cmd=0xA0+cmd1
  buf2[0]=cmd #cmd+id
  buf2[1]=0x05 #angle
  con.write(buf2)
#  rcv = [ord(i) for i in con.read(6)]
#  print "rrr=",rcv
  buf_read=con.read(6)
  if (len(buf_read)==6):
     temp_[0]=ord(buf_read[4])
     temp_[1]=ord(buf_read[5])
     val=temp_[1]|(temp_[0]<<7)
     return(val)
  else:
    print ("read position error")
    return(0)
#---------------------------------
# set ID
def id_read():
  buf4[0]=0xFF
  buf4[1]=0x00
  buf4[2]=0x00
  buf4[3]=0x00
  con.write(buf4)
 # time.sleep(1.5)
  #rcv = [ord(i) for i in con.read(5)]
  #print rcv
  buf_read=con.read(1)
 
  if (len(buf_read)==1):
     val=(ord(buf_read[0]))&0x1f
     return(val)
  else:
    print ("ID read error")
    return(0)
#---------------------------------
# set ID 0-31
def id_set(sid):
  cmd1=sid&0x1f 
  cmd=0xE0+cmd1
  buf4[0]=cmd    #cmd+id
  buf4[1]=0x01
  buf4[2]=0x01
  buf4[3]=0x01
  con.write(buf4)
  time.sleep(0.5)
  #rcv = [ord(i) for i in con.read(5)]
  #print rcv
  buf_read=con.read(5)
  if (len(buf_read)==5):
     val=(ord(buf_read[4]))&0x1f
     return(val)
  else:
    print ("IDS read error")
    return(0)
#---------------------------------
# read memory
def read_memory(sid):
  cmd1=sid&0x1f 
  cmd=0xA0+cmd1
  buf2[0]=cmd    #cmd+id
  buf2[1]=0x00
  con.write(buf2)
  time.sleep(0.5)
  #rcv = [ord(i) for i in con.read(68)]
  #print rcv
  buf_read=con.read(68)
  #print buf_read[8],buf_read[9]
  if (len(buf_read)==68):
     #val=ord(buf_read[18])
     #val=ord(buf_read[19])
     return(val)
  else:
    print ("memory read error")
    return(0)
#---------------------------------
# slave mode set / reset
def change_sleve(sid,sl): #sl=1 on sl1=0 off
  cmd1=sid&0x1f 
  cmd=0xA0+cmd1
  buf2[0]=cmd    #cmd+id
  buf2[1]=0x00
  con.write(buf2)
  time.sleep(0.5)
  #rcv = [ord(i) for i in con.read(68)]
  #print rcv
  buf_read=con.read(68)
  str_list = list(buf_read)
  if (sl==1):
     str_list[18]=chr(0x08)
  else:
     str_list[18]=chr(0x00)
  cmd1=sid&0x1f
  cmd=0xC0+cmd1
  str_list[2]=chr(cmd)
  str_list[3]=chr(0x00)
  #print("stst",str_list)
  for i in range(66):
      str_list[i]=str_list[2+i]
  #print "ssss",str_list
  str_changed = "".join(str_list)
  #print(str_changed)
  con.write(str_changed)
  rcv = [ord(i) for i in con.read(68)]
  print rcv
#---------------------------------
#angle control test
def test_angle_control(sid):
  print "start"
  i=5500
  while i<8000:
    i=i+250
    set_angle(sid,i)
    time.sleep(0.05)
#
#---------------------------------
if __name__ == '__main__':
  sid=2
  time.sleep(0.1)
  print "ID=",id_read() #read ID
  #print "IDS=",id_set(2) #set ID
  time.sleep(0.1)
  #rcv = [ord(i) for i in con.read(6)]
  #print "rrr=",rcv
  print "data=",set_angle(sid,7500)
  time.sleep(0.1)

  print "angle=",set_read_angle(sid,5000)
  time.sleep(0.1)
  print "data=",set_angle(sid,7500)
  time.sleep(0.1)
  print "current=",current_set(sid,63)
  print "speed=",speed_set(sid,100)
  print "strech=",strech_set(sid,60)
  print "temp.=",temp_set(sid)
  #print "memory=",read_memory(sid)
  #print "change=",change_sleve(sid,0)
  #print read_angle(sid)
  test_angle_control(sid)
  time.sleep(0.1)

  #rcv = [ord(i) for i in con.read(6)]
  #print "rrr=",rcv

  print "free and read position=",set_read_angle(sid,0)
  print "set free"
  #set_angle(sid,0)
  print "end"
  con.close()
#---------------------------------
