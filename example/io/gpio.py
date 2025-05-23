#!/usr/bin/env micropython
# GPIO program
# 2025.5.18
# by T.Nishimura of AiRRC
#
# LED gpio 16pin
# SW  gpio 17pin
#-----------------------------------------
#
from machine import Pin
import utime
#-------------------------
class GPIO():
  def __init__(self):
    self.switch = Pin(17, Pin.IN, Pin.PULL_UP)  # GP0のピンを入力ピンに定義。PULL_UPに設定
    self.led0 = Pin("LED", Pin.OUT, value=0) # on boardのLED
    self.led1 = Pin(16, Pin.OUT, value=0)
  def switch(self):
    sw=self.switch.value()
    return(sw)
  def led0on(self):
      self.led0.off()  # LEDを点灯
  def led0off(self):    
      self.led0.on()
  def led1on(self):
      self.led1.on()  # LEDを点灯
  def led1off(self):    
      self.led1.off() 
#------------------------
if __name__ == '__main__':
  print('Start GPIO Test')
  gpio=GPIO()  
  #
  while True:
    if gpio.switch()==0:
      gpio.led0on()
      gpio.led1on()
      print("on")
    else:
      gpio.led0off()
      gpio.led1off()    
      print("off")
    utime.sleep_ms(50)  # 50msec待つ
#-----------------------------------------