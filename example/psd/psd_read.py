#!/usr/bin/env micropython
# PSD ADC Test program
# 2025.5.18
# by T.Nishimura of AiRRC
#
import machine
import utime
#-------------------------
class PSDread():
  def __init__(self):
    self.sensor_psd0 = machine.ADC(0) #右センサー
    self.sensor_psd1 = machine.ADC(1) #左センサー
    self.sensor_psd2 = machine.ADC(2) #後ろセンサー
    self.denatsu_factor = 3.3 / (65535) #電圧に変換係数
    self.kyori_factor=0.3 #電圧に変換係数
#
  def read_adc0(self):
    read_psd0 = self.sensor_psd0.read_u16()*self.denatsu_factor
    if read_psd0!=0:
      dist0 = (1/read_psd0)*self.kyori_factor
    return dist0
#
  def read_adc1(self):
    read_psd1 = self.sensor_psd1.read_u16()*self.denatsu_factor
    if read_psd1!=0:
      dist1 = (1/read_psd1)*self.kyori_factor
    return dist1
#
  def read_adc2(self):
    read_psd2 = self.sensor_psd2.read_u16()*self.denatsu_factor
    if read_psd2!=0:
      dist2 = (1/read_psd2)*self.kyori_factor
    return dist2
#
  def read_adc_all(self):
    read_psd0 = self.sensor_psd0.read_u16()*self.denatsu_factor
    read_psd1 = self.sensor_psd1.read_u16()*self.denatsu_factor
    read_psd2 = self.sensor_psd2.read_u16()*self.denatsu_factor
    if read_psd0!=0:
      dist0 = (1/read_psd0)*self.kyori_factor
    if read_psd1!=0:
      dist1 = (1/read_psd1)*self.kyori_factor
    if read_psd2!=0:
      dist2 = (1/read_psd2)*self.kyori_factor
    return dist0,dist1,dist2
#  
#------------------------
if __name__ == '__main__':
  print('Start PSD Test')
  psd=PSDread()  
  #
  while True:
    dist0,dist1,dist2=psd.read_adc_all()
    print(dist0,dist1,dist2)
    utime.sleep_ms(100)
#------------------------------------------------