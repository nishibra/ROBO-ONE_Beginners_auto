# ROBO-ONE Beginners 自律型ロボット Software
このロボットはRaspberry Pi Picoを使った初心者向けの自律型ロボットです。MycroPythonを使用してプログラミングします。
プログラムに関しては下記概ね確認済みです。少しずつ公開していきます。

## 開発環境
- PCのOS
  Windows
- 統合開発環境
  Thonny
- 開発言語
  Micro Python

### Thonnyのインストール

[Thonnyのインストール【Windows編】](https://sanuki-tech.net/and-more/2022/install-thonny-python-ide/)

### Raspberry Pi Pico

[Pico-series Microcontrollers](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-2-family)

### picoの開発の流れ

- リセントボタンを押しながら電源をいれる。
- PCにPICOのフォルダーを認識
- UF2フィルをダウンロードし書き込み
- Thonnyを起動
- ツールオプションの設定
- サンプルプログラムをロード/実行
- main.pyとしてpicoに保存(自動起動)

### UF2ファイル
UF2は-USB Flashing Format(UF2)-Microsoftが開発したマイコン書き込み用のファイルフォーマットです。以下のサイトより適切なuf2ファイルをダウン―ドしてください。

[Download the correct MicroPython UF2 file for your board](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

### Picoの起動

UF2ファイルをダウンロードし、picoのフォルダーにコピペしてください。電源を入れるとPicoが起動します。
Thonnyにて以下を設定します。

- Config等
- Picoの設定
- Micro Pythonの初期設定


## サンプルプログラム
### 押しボタンSW入力とLed点滅
```
io/switch_led_test.py
```
### ADCとPSD入力
```
psd/psd_test.py
```
### Serial Servoのコントロール
```
krs/krs_driver.py
```
サーボモーターの設定

![SERVO_SET](pics_git/ics_inv_s.png)

### I2cスキャナー
```
i2c/i2c_2ch_scaner.py
```
[参考 Raspberry Pi Pico: I2C Scanner (MicroPython) – Finding the Address of I2C Devices](https://randomnerdtutorials.com/raspberry-pi-pico-i2c-scanner-micropython/)

### IMUライブラリー
```
imu/bno055_test.py
imu/bno055_base.py
imu/bno055.py
```
### ToFライブラリー
```
tof_test.py
tof_max_mini.py
lider.py
```
[参照 tf-luna-micropython](https://github.com/davmoz/tf-luna-micropython)

### BLE 通信ライブラリー
```
ble/ble_test.py
ble/ble_simple_peripheral.py
ble/ble_advertising.py
```
[参照 Pi Pico W でBluetooth Low Energy（BLE）を試してみる](https://wisteriahill.sakura.ne.jp/CMS/WordPress/2023/10/09/pi-pico-bluetooth-low-energy-ble/)

### BLEを使ったスマホによるロボットコントロール
- スマホによる操縦プログラム
- PSDによるリングエッジの認識と回避
- PSDによる相手の認識と攻撃
```
beginners/robo_beginners.py
```
