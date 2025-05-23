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
    print('Bus error: Please check LIDAR wiring')
    sys.exit()
#
lidar = LIDAR(i2c_1, LIDAR_ADDRESS)
print(lidar.version())
lidar.set_min_max(1,200)
lidar.set_frequency(250)
#
min_dist=3.0
max_dist=0
while True:
    dist=lidar.distance()/100
    if dist==0:
        dist=2.1 
    #
    if min_dist>dist:
        min_dist=dist
    if max_dist<dist:
        max_dist=dist    
    print(min_dist,max_dist)
    utime.sleep_ms(50)
