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

- ConfigでインタープリターをMicroPython(Raspberry Pi Pico)に設定します。ポートが表示されていることを確認します。
- MicroPython(Raspberry Pi Pico)のポートに接続します。
- Shell画面が以下の要になれば設定完了です。
- すでにプログラムが書き込まれているときはThonnyのストップボタンをおすか、Pico拡張ボード上のリセットボタンを押した後、ポートに再接続します。
```
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> 
```
## サンプルプログラム
### 押しボタンSW入力とLed点滅
example/io/switch_led_test.pyはスイッチ入力によりLEDを点灯するプログラムです。

### ADCとPSD入力
example/psd/psd_test.pyはPSDセンサーの出力電圧をADコンバーターにより取り込みその電圧を距離に変換するプログラムです。

### Serial Servoのコントロール
example/krs/krs_driver.pyは近藤科学のKRSサーボモーターをコントロールするためのプログラムです。
サーボのボーレイトはは1250000bpsに設定されているものとして以下のように初期化しています。
```
class KRSdriver():
  def __init__(self):
   #set serial
    self.con = UART(1, baudrate=1250000, tx=Pin(8), rx=Pin(9))
    self.con.init(bits=8, parity=0, stop=1,timeout=50)
```
mainプログラムで各軸のポジションの取得やモーターの回転方向などのテストができます。
```
if __name__ == '__main__':
  print('Start KRS Test')
  krs=KRSdriver()
#
  get_position_all()　# すべての軸のポジションを取得
  arm_set() # アームのセットポジションへ移動
  drive_set() # モーターを直進後転回
```
またサーボモーターの設定は以下のようにしています。

![SERVO_SET](pics_git/ics_inv_s.png)

### I2cスキャナー
```
example/i2c/i2c_2ch_scaner.py
```
[参考 Raspberry Pi Pico: I2C Scanner (MicroPython) – Finding the Address of I2C Devices](https://randomnerdtutorials.com/raspberry-pi-pico-i2c-scanner-micropython/)

### IMUライブラリー
```
example/imu/bno055_test.py
example/imu/bno055_base.py
example/imu/bno055.py
```
[参照 micropython-bno055](https://github.com/micropython-IMU/micropython-bno055)

### ToFライブラリー
```
example/tof/tof_test.py
example/tof/tof_max_mini.py
example/tof/lider.py
```
[参照 tf-luna-micropython](https://github.com/davmoz/tf-luna-micropython)

### BLE 通信ライブラリー
```
example/ble/ble_test.py
example/ble/ble_simple_peripheral.py
example/ble/ble_advertising.py
```
[参照 Pi Pico W でBluetooth Low Energy（BLE）を試してみる](https://wisteriahill.sakura.ne.jp/CMS/WordPress/2023/10/09/pi-pico-bluetooth-low-energy-ble/)

### BLEを使ったスマホによるロボットコントロール
- スマホによる操縦プログラム
- PSDによるリングエッジの認識と回避
- PSDによる相手の認識と攻撃
```
example/beginners/robo_beginners.py
```
スマホのアプリBaconを使用します。アプリからダウンロードしてください。以下のアイコンです。

![SERVO_SET](pics_git/bacon.png)

コントロール画面は以下のように押したときにコマンドを発行し、離した時に発行されるコマンドを設定します。動画の様な画面を自由に作ってください。

![SERVO_SET](pics_git/bacon_s1.png)

[動画](https://www.youtube.com/shorts/bfC331REHko)
