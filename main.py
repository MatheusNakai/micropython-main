""" from machine import Pin, I2C
import ujson
import utime
from ssd1306 import SSD1306_I2C

    
    
i2c= I2C(0,sda=Pin(0),scl=Pin(1))
oled = SSD1306_I2C(128,64,i2c)
led = Pin(28, Pin.OUT)
pir = Pin(16,Pin.IN, Pin.PULL_UP)
led.low()
utime.sleep(3)


i=0
oled.text("Insira sua senha",0,0)
oled.show()
non_number = ["A","B","C","D","*","#"]
password = []
while i<200:
    #print(pir.value())
    if pir.value()==0:
        #print("Led on")
        led.high()
        utime.sleep(0.2)
    else:
        #print("waiting")
        led.low()
        utime.sleep(0.1)
    i+=1
    key=Keypad4x4Read(col_list, row_list)
    if key not in non_number:
        password.append(key)
        utime.sleep(0.3)
    
    
 """

from models.User import User
from use_cases.FileRW_UC import FileRW_UC
f = FileRW_UC('json.txt')
user = User(10,1234)
user1 = User(11,1234)

l = [user.__dict__,user1.__dict__]

f.write(l)

