# I2C Scanner MicroPython
from machine import Pin, SoftI2C
#
#i2c0
#  gpio20=sda
#  gpio21=scl

#i2c1
#  gpio14=sda
#  gpio15=scl
#
i2c0 = SoftI2C(scl=Pin(21), sda=Pin(20))
i2c1 = SoftI2C(scl=Pin(15), sda=Pin(14))
#
print('--I2C0 & I2C1 SCANNER--')
device0 = i2c0.scan()
device1 = i2c1.scan()
#
if len(device0) == 0:
  print('No i2c0 device !')
else:
  print('i2c0 devices:', len(device0))
  for device in device0:
    print('i2c0 address:', hex(device))
#
if len(device1) == 0:
  print('No i2c1 device !')
else:
  print('i2c1 devices:', len(device1))
  for device in device1:
    print('i2c1 address:', hex(device))
#