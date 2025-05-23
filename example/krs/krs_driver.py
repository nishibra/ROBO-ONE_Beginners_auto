#!/usr/bin/env micropython
# Kondo KRS servo control program
# 2025.4.6
# by T.Nishimura of AiRRC
#
from machine import Pin, I2C, UART
import time
#-------------------------
class KRSdriver():
  def __init__(self):
   #set serial
    self.con = UART(1, baudrate=1250000, tx=Pin(8), rx=Pin(9))
    self.con.init(bits=8, parity=0, stop=1,timeout=50)
#
    self.buf2=bytearray(2)
    self.buf3=bytearray(3)
    time.sleep(0.2)
#
  def current_set(self,sid,curr):
    self.buf3[0]=0xC0+sid #cmd+id
    self.buf3[1]=0x03
    self.buf3[2]=curr&0x1F
    self.con.write(self.buf3)
#
    buf_read=self.con.read(2)
    if buf_read is not None:
      if (len(buf_read)==2):
        val=buf_read[1]
        return(val)
      else:
        print ("ID="+str(sid)+"read few")
        return (9998)
    else:
      print ("ID="+str(sid)+"read none")
      return(9999)
#----------------------------
# set angle
  def set_position_ret(self,sid,t_pos):
    if(t_pos==0): #set free
      t_pos=0
    elif(t_pos>11500):
      t_pos=11500
    elif(t_pos<3500 ):
      t_pos=3500
  #
    self.buf3[0]=0x80+sid #cmd+id
    self.buf3[1]=(t_pos>>7)&0x7f
    self.buf3[2]=t_pos&0x7f
    self.con.write(self.buf3)
    
    buf_read=self.con.read(3)
    if buf_read is not None:
      #print(len(buf_read))
      if (len(buf_read)==3):
        val=buf_read[2]+(buf_read[1]<<7)
        return(val)
      else:
        print ("ID="+str(sid)+" read few="+str(len(buf_read)))
        return (9998)
    else:
      print ("ID="+str(sid)+" read none")
      return(9999)
#-----------------------------
# set angle by slave mode
  def set_position(self,sid,t_pos):
# 
    if(t_pos==0): #set free
      t_pos=0
    elif(t_pos>11500):
      t_pos=11500
    elif(t_pos<3500 ) :
      t_pos=3500
  #
    self.buf3[0]=0x80+sid #cmd+id
    self.buf3[1]=(t_pos>>7)&0x7f
    self.buf3[2]=t_pos&0x7f
  # write
    self.con.write(self.buf3)
#------------------------
# read angle at free condition
  def read_position_set_free(self,sid):
    position=self.set_position_ret(sid,0)
    return position
#--------------------------
# read any condition
  def read_position(self,sid):  #from ics3.6
    self.buf2[0]=0xA0+sid #cmd+id
    self.buf2[1]=0x05 #angle
    self.con.write(self.buf2)
    #time.sleep(0.001)
    buf_read=self.con.read(4)
    if buf_read is not None:
      if (len(buf_read)==4):
        val=buf_read[3]|(buf_read[2]<<7)
        return(val)
      else:
        print ("ID="+str(sid)+" read few")
        #print ("ID="+str(sid)+" set few="+str(len(buf_read)))
        return (9998)
    else:
      print ("ID="+str(sid)+" read none")
      return (9999)

def get_position_all():
  sid=1 # right motor
  print(sid,"=",krs.read_position(sid))
  sid=2 # left motor
  print(sid,"=",krs.read_position(sid))
  sid=3 # pan motor
  print(sid,"=",krs.read_position(sid))
  sid=4 # tilt motor
  print(sid,"=",krs.read_position(sid))

def arm_set():
#Arm
  krs.set_position_ret(3,6000)
  krs.set_position_ret(4,8200)
  time.sleep(0.3)
  krs.read_position_set_free(1)
  krs.read_position_set_free(2)
  
def drive_set():
  #直進
  krs.set_position_ret(1,7500+100)
  krs.set_position_ret(2,7500-100)
  time.sleep(0.3)
  #回転
  krs.set_position_ret(1,7600)
  krs.set_position_ret(2,7600)
  time.sleep(0.4)
  #stop
  krs.set_position_ret(1,7500)
  krs.set_position_ret(2,7500)
  time.sleep(0.3)
  #free
  krs.read_position_set_free(3)
  krs.read_position_set_free(4)  

#------------------------
if __name__ == '__main__':
  print('Start KRS Test')
  krs=KRSdriver()
#
  get_position_all() # すべての軸のポジションを取得
 # arm_set()# アームのセットポジションへ移動
 # drive_set()# モーターを直進後転回
