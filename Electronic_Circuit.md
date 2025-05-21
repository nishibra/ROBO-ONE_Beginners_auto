# ROBO-ONE Beginners 自律型ロボット(RasPi Pico)　Electronic Circuit
## <電子回路>
電子回路部分の完成写真です。はんだ付けを極力少なくするようにしました。入出力の拡張も余裕があります。

![mather](pics_git/electro.png)  

### Pico拡張ボード
入出力Pinが電源とともに出力されているのでとても便利です。赤:3.3v 黒:gnd 黄:信号

![mather](pics_git/mboard.png)  

[拡張ボードの購入先](https://www.amazon.co.jp/dp/B0B45YWJH7?ref=ppx_yo2ov_dt_b_fed_asin_title)

### Raspberry Pi Pico
PicoやPico w,pico2,pico2wなどを使用します。Pico2W、Pico2Wを使用すれば、Bluetoothによるコントロールプログラムが利用できます。

[Pico-series Pin](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-2-family)

[Picoの購入先](https://akizukidenshi.com/catalog/g/g117947/)

### Serial変換I/F
サーボモーターを使用するためのシリアル通信の半二重通信から全二重通信に変換するボードです。

[Serial変換I/Fの購入先](https://www.besttechnology.co.jp/modules/onlineshop/index.php?fct=photo&p=299)

#### 配線方法
シリアル変換基板の配線状態です。

![serial](pics_git/serial_conn.png)  

![serial](pics_git/serial_h1.png)  

拡張基板に電源供給するためのコネクターをはんだ付けします。

![serial](pics_git/base.png)  

[購入先](https://www.amazon.co.jp/MKBKLLJY-15%E3%83%9A%E3%82%A2JST-2-54%E3%83%9F%E3%83%AA%E3%83%A1%E3%83%BC%E3%83%88%E3%83%AB2%E3%83%94%E3%83%B3%E3%82%AA%E3%82%B9%E3%81%A8%E3%83%A1%E3%82%B9%E3%82%B3%E3%83%8D%E3%82%AF%E3%82%BF%E3%82%B1%E3%83%BC%E3%83%96%E3%83%ABUL1007-100%E3%83%9F%E3%83%AA%E3%83%A1%E3%83%BC%E3%83%88%E3%83%AB%E8%B5%A4%E9%BB%92%E3%81%AE%E3%82%B3%E3%83%8D%E3%82%AF%E3%82%BF%E7%B7%9A%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB%E3%81%A8%E7%86%B1%E5%8F%8E%E7%B8%AE%E3%83%81%E3%83%A5%E3%83%BC%E3%83%96%E5%B0%8F%E3%81%95%E3%81%AA%E3%83%89%E3%83%AD%E3%83%BC%E3%83%B3%E9%9B%BB%E6%B1%A0%E7%AB%AF%E5%AD%90%E3%82%BD%E3%82%B1%E3%83%83%E3%83%88LED%E3%82%B9%E3%83%88%E3%83%AA%E3%83%83%E3%83%97%E3%83%A9%E3%82%A4%E3%83%88%E7%94%A8-%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%B3%E3%82%B0%E3%83%89%E3%83%AD%E3%83%BC%E3%83%B3/dp/B0DK4L34LJ/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=Pg55G&content-id=amzn1.sym.7133fed1-b7f0-4a9a-85e6-ec0056dbe781%3Aamzn1.symc.409c7fce-cbd2-4cf4-a6cb-824c258c8778&pf_rd_p=7133fed1-b7f0-4a9a-85e6-ec0056dbe781&pf_rd_r=CYAV1KFXHK1SWP9GP2GV&pd_rd_wg=QWG6P&pd_rd_r=ab2382f8-1e76-4e4d-9324-e0e0dca32048&pd_rd_i=B0DK4L34LJ&th=1)

シリアル変換基板のはんだ付けした状態です。

![serial](pics_git/serial_h2.png)  
![serial](pics_git/serial_h3.png)  
 
シリアルポート1に接続します。

![serial](pics_git/base_serial.png)  




### PSDセンサー
PSD（Position Sensitive Detector）は光が当たった位置に応じて、アナログ信号を出力する受光素子で、﻿距離を計測するセンサーです。出力はアナログ電圧ですのでADC端子に接続します。黒:gnd　赤:3.3v  黄:信号で、ケーブルは黒:gnd　赤:3.3v  白:信号に対応します。このセンサーの推奨電圧は5Vですが3.3Vでも問題なく動作しました。

![psd](pics_git/psd.png)  

[購入先](https://kondo-robot.com/product/02002)
```
右　 GP26
左   GP27
後ろ GP28
に接続します。接続方向を間違えないようにしてください。
```
### TOFセンサー
距離を測定するTOFセンサーです。比較的長距離の距離の計測に使用します。

![tof](pics_git/tof_c.png)

![tof](pics_git/tof_cd.png)  

![tof](pics_git/tfluna.png)  

[購入先](https://www.amazon.co.jp/dp/B087N2JRJ9/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B087N2JRJ9&pd_rd_w=S1om1&content-id=amzn1.sym.f293be60-50b7-49bc-95e8-931faf86ed1e&pf_rd_p=f293be60-50b7-49bc-95e8-931faf86ed1e&pf_rd_r=T8AB1F18CDD292K4XRB3&pd_rd_wg=BPNWh&pd_rd_r=b4a0289b-4286-4983-8f2f-0c5dc9c905ef&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw)
```
I2C1に接続します。
GP15    scl
GP14    sda
3V3     Vcc
GND     gnd
```

### IMU　9軸センサー
オイラー角の計測するためのセンサーです。I2C通信で使用します。

![imu](pics_git/imu_c.png)

![imu](pics_git/bno055.png)  

[購入先](https://www.amazon.co.jp/BNO055-%E7%B5%B6%E5%AF%BE%E6%96%B9%E5%90%91%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC-%E3%83%9C%E3%83%BC%E3%83%89%E8%A7%92%E5%BA%A6-%E3%82%B8%E3%83%A3%E3%82%A4%E3%83%AD%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97-%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB/dp/B0DWMH2Q5R/ref=sr_1_3_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1KRTL7M5EYEPF&dib=eyJ2IjoiMSJ9.7aJLRn6PFVtPx5BZzxavXWUdBq4QwEbMpnBcoDqnpMJmxHoVhYJ4gzQt6b_R9lhVuWffEwHppjduuULQRPCgax7qg5t5qgFQfHdc8DSfOuYBcyJi1Tv2cfpOwKojhLSk9xG_D2LIu75vhbSQgj49-fiQHrr2MgcUOlqcltPMqVsFAmkuQuwnJx7NgNiZH12yXYVYVfVzXwOzbCQOS0TwsJiqzJAj3fesd1y6poiZst4qXJ1A6YwIt4y0FtPf-0LaM-zUtKZkWWMeuuI35nSUb_oIfNsG15sHmvkodnjwpNY.NwwWaNmR0Ko6-cTkWFGggAtHZlMR-3M_aj71AKZnqQk&dib_tag=se&keywords=bno055+%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC&qid=1746504506&sprefix=bno055+%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%2Caps%2C178&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
```
I2C0に接続します。
GP21    scl
GP20    sda
3V3      Vcc
GND    gnd
```
![imu](pics_git/imu_h.png)  

### Push ボタンSW
押しボタンスイッチです。入力として使います。

![pb](pics_git/pb_c.png)  

![pb](pics_git/pb_sw.png)  
 
[購入先](https://akizukidenshi.com/catalog/g/g104367/)

![pb2](pics_git/pbsw_h.png)

1KΩ程度の抵抗を追加し、GP16に接続します。外側から締め付けるタイプを使用すると組み立てる前にはんだをしておくことが出来ます。

### LED
発光ダイオードです。1KΩ程度の抵抗を追加して使用します。リードの長い方が一般にアノードです。プラス側に接続します。

![led](pics_git/led_c.png)  


![led](pics_git/led.png)  

[購入先](https://akizukidenshi.com/catalog/g/g103261/)

![led](pics_git/led_h.png)  

GP17に接続する。GNDは接続しません。

### 電源SWハーネス
電源用のスイッチです。

![harness](pics_git/harness.png)  
 
[購入先](https://kondo-robot.com/product/lv_sw_harness)

### ニッケル水素バッテリー
このサイズのニッケル水素バッテリーのみが使用可能です。

![bat](pics_git/battery.png)  

[購入先](https://kondo-robot.com/product/02335)

### ROBOパワーセル用コネクターセットオス
拡張基板への電源供給用に使用します。

![con](pics_git/connector.png)  
 
[購入先](https://kondo-robot.com/product/01109)

### 電源ケーブルA
拡張基板への電源供給用に使用します。

![conm](pics_git/connmesu.png)  

[購入先](https://kondo-robot.com/product/02145)


