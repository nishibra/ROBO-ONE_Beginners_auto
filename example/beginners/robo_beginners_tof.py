#!/usr/bin/env micropython
# ROBO-ONE-beginners program with BLE
# with ToF
# 2026.02.18
# by T.Nishimura @AiRRC
#
from ble_simple_peripheral import *
import bluetooth
from machine import Pin  # 入出力モジュール
import utime  # タイマーモジュール
from krs_driver import *
from psd_read import *
from gpio import *
from lider import LIDAR
#
LIDAR_ADDRESS = 0x10
i2c_1 = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15)) 
utime.sleep_ms(10)
#
slaves = i2c_1.scan()
if LIDAR_ADDRESS not in slaves:
    print('Bus error')
    sys.exit()
#
lidar = LIDAR(i2c_1, LIDAR_ADDRESS)
print(lidar.version())
lidar.set_min_max(5, 300)
lidar.set_frequency(250)
#
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
autoF=0 #auto mode:1
tofF=0 #Tof使用:1
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
    global autoF,tofF
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
    elif v==b'Ac':
        print("Upch")
        arm(0,-1700)
    elif v==b'Acr':
        print("Up_ch_r")
        arm(800,-1700)
    elif v==b'Acl':
        print("Up_ch_l")
        arm(-800,-1700)        
    elif v==b'Ad':
        print("Down")
        arm(0,-1950)
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
    elif v==b'On':
        print("Tof on")
        tofF=1
        arm(0,0)
        drive(0,0)  
    elif v==b'Off':
        print("Tof off")
        tofF=0
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
        arm(5500,-1000)
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
    global autoF,tofF
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
    Dist_th=0.26  #AC=0.25  AI=0.26 リングアウトチェック
    Dist_th2=0.14 #AC=0.40  AI=0.12 相手チェック
    #
    Dist_tof=0.3 #001=0.35 相手チェック
    while True:
        dist_t=lidar.distance()/100.00
        if dist_t==0:
            dist_t=3.00
        dist0,dist1,dist2=psd.read_adc_all()
        print(dist0,dist1,dist2,dist_t)
        #print('Tof=',dist_t)
        
        if p.is_connected():
            gpio.led1on()      # LEDを点灯
            i += 1
            if (i%30)==0:
                gpio.led1off()
            #
            if autoF==1:#auto mode
              
              if dist0>Dist_th and dist1>Dist_th:#リングアウトチェック
                print ("U-turn")
                drive(4000,-4000)
              elif dist0>Dist_th and dist1<Dist_th:#リングアウトチェック
                print ("L-turn")
                drive(4000,-0)
              elif dist0<Dist_th and dist1>Dist_th:#リングアウトチェック
                print ("R-turn")
                drive(-0,4000)            
              else: #相手チェック
                if dist0<Dist_th2 and dist1<Dist_th2:#相手チェック
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
                elif dist0<Dist_th2:
                    print ("R-turn")
                    drive(-100,2000)   
                elif dist1<Dist_th2:
                    print ("L-turn")
                    drive(2000,-100)
                else:
                    print ("no-turn")
                    #
                    if tofF==1: # ToFで相手チェック　いなければターン
                    
                        if dist_t<Dist_tof:
                            print ("Foward")
                            drive(4000,4000)
                        else:
                            if (i%300)>150: 
                                print("Fw-right")
                                drive(30,4000)
                            else:
                                print("Fw-left")
                                drive(4000,30)
                        
                    else:
                        drive(4000,4000)
                #後ろチェック
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
#
if __name__ == "__main__":
    main()
#