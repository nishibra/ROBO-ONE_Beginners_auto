# Switch LED test program
#
# LED GP16pin
# SW  GP17pin
#-----------------------------------------
#
from machine import Pin
import utime
#
switch = Pin(17, Pin.IN, Pin.PULL_UP)  # GP0のピンを入力ピンに定義。PULL_UPに設定
led = Pin(16, Pin.OUT, value=0)
while True:
    status = switch.value()
    print("status:", status)
    if status == 1:  # ボタンが押されたら
        led.on()  # LEDを点灯
    else:   
        led.off()  # LEDを消灯
    utime.sleep_ms(50)  # 50msec待つ
#-----------------------------------------