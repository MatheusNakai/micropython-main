from models.Oled import Oled


class Oled_controller(object):
    
    def __init__(self):
        self.oled = Oled()

    def oled_display(self, text:str, x:int, y:int):
        self.oled.oled_display(text, x, y)

    def oled_clear(self):
        self.oled.Oled_clear()
    
    def oled_on(self):
        self.oled.Oled_on()
    
    def oled_off(self):
        self.oled.Oled_off()
        