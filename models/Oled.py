from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

class Oled(object):
    def __init__(self):
        self.i2c= I2C(0,sda=Pin(0),scl=Pin(1))
        self.oled = SSD1306_I2C(128,64,self.i2c)

    def display_text(self,text,x,y):
        self.oled.text(text,x,y)
        self.oled.show()
    
    def display_clear(self):
        self.oled.fill(0)
        self.oled.show()

    def display_on(self):
        self.oled.poweron()
    
    def display_off(self):
        self.oled.poweroff()