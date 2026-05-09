#!/usr/bin/env micropython
# Kondo KRS servo control program
# 2026.03.29
# by T.Nishimura of AiRRC
#
# Airrc
# 倒立伸子テストprogram
#
from machine import Pin, PWM
import time
from krs_driver_v2_0 import *
#----------------
# BNO055設定
from bno055 import *
i2c = machine.I2C(0, sda=machine.Pin(20), scl=machine.Pin(21)) 
imu = BNO055(i2c)
time.sleep(0.02)
calibrated =True #False
while calibrated == False:     
    calibrated = imu.calibrated()
    print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
    time.sleep(0.02)
#PushボタンSW設定
switch = Pin(17, Pin.IN, Pin.PULL_DOWN)   
#サーボモーターの設定
#servo id
id_r=1
id_l=2
id_pan=3
id_tilt=4
#
ct=7500#3500--11500
ct_pan=6200#panのセンター
ct_tilt=8000#Tiltのセンター
#インスタンス化
krs=KRSdriver()
# サーボフリー
krs.read_position_set_free(id_r)
krs.read_position_set_free(id_l)
krs.read_position_set_free(id_pan)
krs.read_position_set_free(id_tilt)
# 車輪のコントロール(足回りのみ使用)
def drive(r_sp,l_sp):
    if r_sp>4000:
        r_sp=4000
    elif r_sp<-4000:
        r_sp=-4000
    if l_sp>4000:
        l_sp=4000
    elif l_sp<-4000:
        l_sp=-4000                    
    krs.set_position_ret(id_r,ct-r_sp)
    krs.set_position_ret(id_l,ct+l_sp)
# PIDコントローラーClass
class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.previous_error = 0
        self.integral = 0
    # updateメソッド
    def update(self, current_value, dt):
        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output
    # resetメソッド
    def reset(self):
        self.integral = 0
        self.previous_error = 0
#------------------------------------
# PushボタンSWが押されるのを待つ。バランス点でSWを押す。
while(switch.value()==1):
    eu=imu.euler()
    pitch = eu[1]
    time.sleep(0.02)
    print(pitch)
#
last_time = time.ticks_ms()        
kp = 1.0  # 比例ゲイン (調整が必要)
ki = 10.0   # 積分ゲイン (調整が必要)
kd = 0.05 # 微分ゲイン (調整が必要)
target_angle =pitch #目標をセット
target_angle =-8 #固定する場合
# PIDコントローラのインスタンス化
pid_controller = PIDController(kp, ki, kd, target_angle)
#------------------------------------
# メインループ
if __name__ == "__main__":
    calibrated = imu.calibrated()
    while True:
        current_time = time.ticks_ms()
        dt = (current_time - last_time) / 1000.0
        last_time = current_time
        eu=imu.euler() # Eulea角を取得
        pitch = eu[1] # ピッチ角
        #        
        if pitch is not None:
            ##位置決めの場合
            pos=krs.read_position(id_r)
            pos_factor=0.001
            #右サーボ位置目標ct=7500で位置決めを行う
            #positionとの差分をピッチ角に加えてpid制御を行う
            d_pos=((pos-ct)*pos_factor)
            ##
            if dt==0:dt=1
            control_output = pid_controller.update(pitch+d_pos,dt)
            #print(dt,pitch,pos)
            factor = 10
            left_speed =int(control_output * factor)
            right_speed =int(control_output * factor)
            drive(right_speed,left_speed)
            time.sleep(0.005)
#
