![robo-one](pics/robo-one.png)  ![bra](pics/bra.png)
# ROBO-ONE Beginners auto

## ROBO-ONE Beginners 競技規則　[競技規則](https://github.com/nishibra/ROBO-ONE_Beginners)
## ROBO-ONE Beginners auto　[機械設計](Mechanical_Design.md)
## ROBO-ONE Beginners auto　[電子回路](Electronic_Circuit.md)
## ROBO-ONE Beginners auto　[ソフトウェア](Software.md)


## 参考資料
#### auto開発に必要なもの
>Windows PC
>スマホ(Android)

>工具
>>はんだごて
-  はんだ
-  ニッパー
-  ラジオペンチ
-  ドライバー
-  テスター

- Raspbery Pi Pico W
-  拡張ボード
-  kxrセット
-  serial 変換ボード
-  バッテリー/充電器


## picoの使い方の流れ

- リセントボタンを押しながら電源をいれる。
- PCにPICOのフォルダーを認識
- UF2フィルをダウンロードし書き込み
- thonnyをインストール
- ツールオプションの設定
- サンプルをロード
- main.pyをpicoに保存

### UF2ファイル

Pi Pico W でBluetooth Low Energy（BLE）を試してみる

https://wisteriahill.sakura.ne.jp/CMS/WordPress/2023/10/09/pi-pico-bluetooth-low-energy-ble/

https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

Download the correct MicroPython UF2 file for your board:

Pico 2 W

よりUF2ファイルをダウンロードし、picoのフォルダーにコピペしてください。








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

https://logikara.blog/raspi-pico-thonny-micropy/#mokuji_3


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


### 変更点
1.bleの名前

2.055のaddr 28 or 29 二か所変更
bno055_base.py
  def __init__(self, i2c, address=0x28, 

bno055.py
def __init__(self, i2c, address=0x28, crystal=True, 

tof
bytearray(value)


-[ラズパイ] VL53L1Xを使って距離を測定する

https://noda-farm.blog/archives/47






2.cariblationの方法

https://qiita.com/yomori/items/95101a8792287263792b
https://zenn.dev/ymt117/books/100kinsat-spr-basic/viewer/imu

-加速度計のキャリブレーション
デバイスを数秒間、6つの異なる安定した位置に置く。
位置の変更はゆっくりと動かすようにする。
6つの安定した位置は任意の方向でよいが、装置が少なくとも1回はX,Y,Z軸に垂直になるようにする。

-ジャイロスコープのキャリブレーション
デバイスを数秒間、単一の安定した位置に置く。

-磁力計のキャリブレーション
磁力計はHard-iron歪みとSoft-iron歪みの両方の影響を受けるが、多くの場合、Hard-ironの影響が原因。
装置全体をランダムな動き（たとえば、空中に数字の「8」を書くなど）をいくつか行うことでHard-ironに対するキャリブレーションを行う。

CALIB_STATレジスタで、加速度計のキャリブレーション状態を確認できる。すべてが3になると終了する。




