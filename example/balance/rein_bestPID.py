#
from machine import Pin, I2C, PWM
import time
import random
from krs_driver_v2_0 import *
import json
#from oled64_class import *
#oled=OLEDdriver()
#oled.logo()

# BNO055のI2Cアドレス
from bno055 import *
i2c = machine.I2C(0, sda=machine.Pin(20), scl=machine.Pin(21)) 
imu = BNO055(i2c)
time.sleep(0.02)
calibrated =True# False #      
while calibrated == False:     
    calibrated = imu.calibrated()
    print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
    time.sleep(0.02)
#------------------------------
# サーボモーターの設定
#servo id
id_r=1
id_l=2
id_pan=3
id_tilt=4
#
ctr=7500#3500--11500
ctl=7500#3500--11500
ct_pan=6200
ct_tilt=8000
#
krs=KRSdriver()
#
def free():
    krs.read_position_set_free(id_r)
    krs.read_position_set_free(id_l)
    krs.read_position_set_free(id_pan)
    krs.read_position_set_free(id_tilt)
#
def drive(r_sp,l_sp):
    if r_sp>4000:
        r_sp=4000
    elif r_sp<-4000:
        r_sp=-4000
    if l_sp>4000:
        l_sp=4000
    elif l_sp<-4000:
        l_sp=-4000                    
    krs.set_position_ret(id_r,ctr-r_sp)
    krs.set_position_ret(id_l,ctl+l_sp)
#
def arm(pan,tilt):
    krs.set_position_ret(id_pan,ct_pan+pan)
    krs.set_position_ret(id_tilt,ct_tilt+tilt)
#
# PID制御クラス (ゲインは外部から設定できるように変更)
class PIDController:
    def __init__(self, kp, ki, kd, setpoint=-8.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.previous_error = 0
        self.integral = 0
#
    def update(self, current_value, dt):
        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output
#
    def reset(self):
        self.integral = 0
        self.previous_error = 0
#
# PIDゲインの候補 (非常に少ない数で試す)
KP_CANDIDATES = [1,2]
KI_CANDIDATES = [5,10,15]
KD_CANDIDATES = [0.3,0.5]
ALL_ACTIONS = [(kp, ki, kd) for kp in KP_CANDIDATES for ki in KI_CANDIDATES for kd in KD_CANDIDATES]
NUM_ACTIONS = len(ALL_ACTIONS)

# 状態の離散化 (非常に粗い)
def discretize_state(pitch, angular_velocity):
    if pitch < -10:
        pitch_state = 0
    elif pitch < -2:
        pitch_state = 1
    elif pitch < 2:
        pitch_state = 2
    elif pitch < 10:
        pitch_state = 3
    else:
        pitch_state = 4
#
    if angular_velocity < -5:
        vel_state = 0
    elif angular_velocity < 5:
        vel_state = 1
    else:
        vel_state = 2
#
    return (pitch_state, vel_state)
#
# Qテーブルの初期化 (状態数 x 行動数)
NUM_PITCH_STATES = 5
NUM_VEL_STATES = 3
Q_TABLE = [[0.0 for _ in range(NUM_ACTIONS)] for _ in range(NUM_PITCH_STATES * NUM_VEL_STATES)]
#
def get_q_value(state, action_index):
    state_index = state[0] * NUM_VEL_STATES + state[1]
    return Q_TABLE[state_index][action_index]
#
def set_q_value(state, action_index, value):
    state_index = state[0] * NUM_VEL_STATES + state[1]
    Q_TABLE[state_index][action_index] = value
#
# ε-greedy法による行動選択
EPSILON = 0.1
def select_action(state):
    if random.random() < EPSILON:
        return random.randint(0, NUM_ACTIONS - 1)
    else:
        state_index = state[0] * NUM_VEL_STATES + state[1]
        max_q = -float('inf')
        best_action_index = 0
        for i in range(NUM_ACTIONS):
            if Q_TABLE[state_index][i] > max_q:
                max_q = Q_TABLE[state_index][i]
                best_action_index = i
        return best_action_index
#
# 報酬関数の設計 (非常に単純な例)
def get_reward(pitch):
    if abs(pitch) < 5:
        return 1.0
    elif abs(pitch) < 15:
        return 0.1
    else:    
        return -1.0
#
# 学習率と割引率
ALPHA = 0.1 #学習率
GAMMA = 0.9 #割引率
kp_best=1
ki_best=10
kd_best=0.1
rw_best=-100
#
if __name__ == "__main__":
    free()
    if calibrated == True:
        pid_controller = PIDController(0, 0, 0) # 初期ゲインは0
        last_time = time.ticks_ms()
        reward=0
        #
        try:
            for episode in range(20): # 学習エピソード数
                #print(f"Episode: {episode}")
                pid_controller.reset()
                total_reward = 0
                free()
                time.sleep(1) # 初期静止時間
#
                for step in range(200): # 1エピソードのステップ数
                    current_time = time.ticks_ms()
                    dt = (current_time - last_time) / 1000.0
                    last_time = current_time
                    eu=imu.euler()
                    pitch = eu[1]

                    angular_velocity = 0 # 角速度の取得はBNO055のデータから別途取得する必要があります

                    if pitch is not None:
                        current_state = discretize_state(pitch, angular_velocity)
                        action_index = select_action(current_state)
                        kp, ki, kd = ALL_ACTIONS[action_index]
                        pid_controller.kp = kp
                        pid_controller.ki = ki
                        pid_controller.kd = kd

                        control_output = pid_controller.update(pitch, dt)
                        #print(dt,pitch)
                        factor = 20
                        left_speed =int(control_output * factor)
                        right_speed =int(control_output * factor)
                        drive(right_speed,left_speed)
                        
                        reward = get_reward(pitch)
                        total_reward += reward
                        eu=imu.euler()
                        next_pitch = eu[1]
        
                        next_angular_velocity = 0#gy[0] # 角速度の取得

                        if next_pitch is not None:
                            next_state = discretize_state(next_pitch, next_angular_velocity)
                            best_next_q = -float('inf')
                            for i in range(NUM_ACTIONS):
                                q_value = get_q_value(next_state, i)
                                if q_value > best_next_q:
                                    best_next_q = q_value

                            old_q = get_q_value(current_state, action_index)
                            new_q = old_q + ALPHA * (reward + GAMMA * best_next_q - old_q)
                            set_q_value(current_state, action_index, new_q)

                        #time.sleep_ms(5)

                        if abs(pitch) > 20: # 倒れたと判定
                            break
                if rw_best<total_reward:
                    rw_best=total_reward
                    kp_best=kp
                    ki_best=ki
                    kd_best=kd
                print(f"Ep:{episode} tr:{total_reward} kp:{kp} ki:{ki} kd:{kd}")
                EPSILON = max(0.01, EPSILON * 0.99) # εを徐々に減らす
                free()

        
            # 学習済みQテーブルをJSON形式で保存
            with open("q_table.json2", "w") as f:
                json.dump(Q_TABLE, f)
            print("Qテーブルの学習完了とJSON保存")

            pid_controller.kp = kp_best
            pid_controller.ki = ki_best
            pid_controller.kd = kd_best
            pitch=0
            print(kp_best,ki_best,kd_best)
            time.sleep(3)
            
            while abs(pitch)<60:#True:
                current_time = time.ticks_ms()
                dt = (current_time - last_time) / 1000.0
                last_time = current_time
                eu=imu.euler()
                pitch = eu[1]
 
        #        
                if pitch is not None:
                    control_output = pid_controller.update(pitch, dt)
         
                    factor = 20
                    left_speed =int(control_output * factor)
                    right_speed =int(control_output * factor)
                    drive(right_speed,left_speed)
                    #print(right_speed,left_speed)
                    #time.sleep(0.005)
            free()
 
        except KeyboardInterrupt:
            print("制御終了")
            free()
 
    else:
        print("BNO055の初期化に失敗しました。")