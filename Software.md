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
-押しボタン入力とLed点滅

-ADCとPSD入力

-Serial Servoのコントロール

## サーボモーターの設定

設定の画面コピー
![SERVO_SET](pics_git/ics_inv_s.png)


-PSDによるリングエッジの認識と回避

-PSDによる相手の認識と攻撃

-IMUライブラリー

-ToFライブラリー

-ToFとIMUによる相手認識

-倒立伸子の制御

-BLE 通信ライブラリー

[Pi Pico W でBluetooth Low Energy（BLE）を試してみる](https://wisteriahill.sakura.ne.jp/CMS/WordPress/2023/10/09/pi-pico-bluetooth-low-energy-ble/)

-BLEを使ったスマホによるロボットコントロール
