# Robo-One_Beginners_auto
## 使用環境
- Windows PC
- Android
- Raspbery Pi Pico W
   配線ボード
　 Kxrセット
　 serial 変換ボード
- バッテリー/充電器
- 

## install Thony
## microPython

### Serial 半二重通信
### BLE
### LED
### Buzzer
### BNO0055
### ADC 
### TF-Luna
```
Number  Function  Description
1     +5V         Power input
2     RXD/SDA     Receive/Data
3     TXD/SCL     Transmit/Clock
4     GND         Ground
5     Interface Input Configuration
                  Ground: boot it in I2C mode.
                  NC or connected to 3.3V: start in serial mode
6     Multiplexed Output
                  Switching mode function: Switching output
                  I2C mode and switch mode off: data ready indication
```
TF-Luna

https://www.waveshare.com/wiki/TF-Luna_LiDAR_Range_Sensor

【Raspberry Pi Pico W】I2Cの使い方（micropython×Thonny）

https://zenn.dev/hoshinagi1219/articles/fa53a5d95b4dda

tf-luna-micropython

https://github.com/davmoz/tf-luna-micropython/blob/main/main.py

class I2C – a two-wire serial protocol

https://docs.micropython.org/en/latest/library/machine.I2C.html


