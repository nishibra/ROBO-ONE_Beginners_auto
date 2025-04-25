# ROBO-ONE Beginners auto (Pico)
## 使用環境
- Windows PC
- Android
- Raspbery Pi Pico W
   配線ボード
　 Kxrセット
　 serial 変換ボード
  バッテリー/充電器
  要はんだ付け
- 

## picoの使い方

```
リセントボタンを押しながら電源をいれる。
PCにPICOのフォルダーを認識
u2フィルをダウンロードし書き込み
thonnyをインストール
ツールオプションの設定
サンプルをロード
main.pyをpicoに保存
```

## Pico Display Pack by Pimoroni

https://shop.pimoroni.com/products/pico-display-pack?variant=32368664215635

https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_display

## Micro python

https://www.marutsu.co.jp/pc/static/large_order/zep/m-z-picoled-da1

https://www.kumikomi-kaihatu.com/technical-column/column-024/

https://micropython.org/download/rp2-pico/

# Thonny

Python IDE for begin

https://logikara.blog/raspi-pico-thonny-micropy/#mokuji_1

ラズパイPicoの使い方 MicroPython＆開発環境Thonny、SSLエラーの対処方法も紹介

https://logikara.blog/raspi-pico-thonny-micropy/

### bluetooth

Pi Pico W でBluetooth Low Energy（BLE）を試してみる

https://wisteriahill.sakura.ne.jp/CMS/WordPress/2023/10/09/pi-pico-bluetooth-low-energy-ble/

### i2c

https://randomnerdtutorials.com/raspberry-pi-pico-i2c-scanner-micropython/

### bt

https://github.com/juan518munoz/PicoSwitch-WirelessGamepadAdapter



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


