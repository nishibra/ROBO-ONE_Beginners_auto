#!/usr/bin/env micropython
# PSD Test program
# 2025.5.18
# by T.Nishimura of AiRRC
#
import machine
import utime
sensor_psd0 = machine.ADC(0) #右センサー
sensor_psd1 = machine.ADC(1) #左センサー
sensor_psd2 = machine.ADC(2) #後ろセンサー

denatsu_factor = 3.3/2**16 #電圧に変換係数
kyori_factor=0.3 #電圧に変換係数(センサーにより調整要)

while True:
    read_psd0 = sensor_psd0.read_u16()*denatsu_factor
    read_psd1 = sensor_psd1.read_u16()*denatsu_factor
    read_psd2 = sensor_psd2.read_u16()*denatsu_factor
    if read_psd0!=0:
      dist0 = (1/read_psd0)*kyori_factor
    if read_psd1!=0:
      dist1 = (1/read_psd1)*kyori_factor
    if read_psd1!=0:
      dist2 = (1/read_psd2)*kyori_factor
    print(dist0,dist1,dist2)
    utime.sleep_ms(20)
#------------------------------------------------