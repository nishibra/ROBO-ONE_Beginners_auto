#!/usr/bin/env micropython
# ROBO-ONE-beginners program with BLE
# 2025.05.06
# by T.Nishimura @AiRRC
#
from ble_simple_peripheral import *
import bluetooth
from machine import Pin  # 入出力モジュール
import utime  # タイマーモジュール
from krs_driver import *
from psd_read import *
from gpio import *
#servo id
id_r=1
id_l=2
id_pan=3
id_tilt=4
#
ct=7500
ct_pan=6200
ct_tilt=8000
#
krs=KRSdriver()
psd=PSDread()
gpio=GPIO()
#
krs.read_position_set_free(id_r)
krs.read_position_set_free(id_l)
krs.read_position_set_free(id_pan)
krs.read_position_set_free(id_tilt)
#
#led = Pin(16, Pin.OUT, value=0)
#
autoF=0
#
def arm(pan,tilt):
    krs.set_position_ret(id_pan,ct_pan+pan)
    krs.set_position_ret(id_tilt,ct_tilt+tilt)
#
def drive(r_sp,l_sp):
    krs.set_position_ret(id_r,ct+r_sp)
    krs.set_position_ret(id_l,ct-l_sp)
#
def on_rx(v):
    global autoF
    gpio.led1on()      # LEDを消灯
    v=v.rstrip()
    print(v)
    if v==b'O':
        print("Free")
        krs.read_position_set_free(id_r)
        krs.read_position_set_free(id_l)
    elif v==b'F':
        print("foward")
        drive(4000,4000)
    elif v==b'B':
        print("Back")
        drive(-4000,-4000)
    elif v==b'R':
        print("Right")
        drive(-4000,4000)
    elif v==b'L':
        print("Left")
        drive(4000,-4000)
    elif v==b'Fr':
        print("Fw-right")
        drive(0,4000)
    elif v==b'Fl':
        print("Fw-left")
        drive(4000,0)
    elif v==b'Br':
        print("Bc-right")
        drive(0,-4000)
    elif v==b'Bl':
        print("Bc-left")
        drive(-4000,0)
    elif v==b'X':
        print("Stop")
        drive(0,0)  
# arm
    elif v==b'Au':
        print("Up")
        arm(0,1600)
    elif v==b'Ad':
        print("Down")
        arm(0,-1800)
    elif v==b'Ar':
        print("Right")
        arm(2000,0)
    elif v==b'Al':
        print("Left")
        arm(-2000,0)
    elif v==b'At':
        print("Auto")
        autoF=1
        arm(0,0)
        drive(0,0)  
    elif v==b'Op':
        print("Op")
        autoF=0
        arm(0,0)
        drive(0,0)
    elif v==b'Uf':
        print("Up-from front")
        arm(0,1600)
        utime.sleep(1)
        arm(0,-1000)
        utime.sleep(1)        
    elif v==b'Ub':
        print("Up-from back")    
        arm(5500,1600)
        utime.sleep(1)
        arm(5500,-1600)
        utime.sleep(1)
    elif v==b'Ao':
        print("Origin")
        arm(0,0)
    elif v==b'Ax':
        print("free")
        krs.read_position_set_free(id_pan)
        krs.read_position_set_free(id_tilt)
    else:
        print("No motion ",v)
#
def main():
    global autoF
    ble = bluetooth.BLE()
    p = BLESimplePeripheral(ble)

    # Start
    for i in range(3):
        gpio.led1off()      # LEDを点灯
        utime.sleep(0.2)  # 0.2秒待つ
        gpio.led1on()      # LEDを点灯
        utime.sleep(0.2)  # 0.2秒待つ
    #
    p.on_write(on_rx)     #　受信割り込みON
    #
    i = 0
    dist_th=0.21
    dist_th2=0.14
    while True:
        if p.is_connected():
            gpio.led1on()      # LEDを点灯
            i += 1
            if (i%30)==0: 
                gpio.led1off()
            dist0,dist1,dist2=psd.read_adc_all()
            print(dist0,dist1,dist2)
            if autoF==1:
              if dist0>dist_th and dist1>dist_th:
                print ("U-turn")
                drive(4000,-4000)
              elif dist0>dist_th and dist1<dist_th:
                print ("L-turn")
                drive(-2000,2000)
              elif dist0<dist_th and dist1>dist_th:
                print ("R-turn")
                drive(2000,-2000)            
              else:
                if dist0<dist_th2 and dist1<dist_th2:
                    print ("Stop")
                    drive(0,0)
                    print("men")
                    arm(0,1800)
                    time.sleep_ms(200)
                    arm(0,-200)
                    time.sleep_ms(200)
                    arm(0,-1800)
                    drive(4000,4000)
                    time.sleep_ms(100)
                    arm(0,0)
                    drive(-4000,-4000)
                    time.sleep_ms(200)
                elif dist0<dist_th2:
                    print ("R-turn")
                    drive(2000,-2000)   
                elif dist1<dist_th2:
                    print ("L-turn")
                    drive(-2000,2000)
                else:
                    print ("Foward")
                    drive(4000,4000)
                #
                if dist2<0.14:
                    print("u-t")
                    drive(-4000,4000)
                    arm(0,1800)
                    time.sleep_ms(500)
                    arm(0,0)
        else:
            gpio.led1on()
            i += 1
            if (i%60)==0: 
               gpio.led1off()
        time.sleep_ms(30)

if __name__ == "__main__":
    main()
