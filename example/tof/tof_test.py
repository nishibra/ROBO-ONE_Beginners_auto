from machine import I2C
import utime
import sys
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
lidar.set_min_max(5, 200) # 計測範囲5cmから200cm
lidar.set_frequency(250)
#
while True:
    dist=lidar.distance()/100.00 # 単位　m
    if dist==0:# 計測不能な場合
        dist=2.1
    print(dist)
    utime.sleep_ms(30)
