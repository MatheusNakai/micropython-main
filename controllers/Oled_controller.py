from models.Oled import Oled


class Oled_controller(object):
    
    def __init__(self):
        self.oled = Oled()

    def Oled_display(self, text:str, x:int, y:int):
        self.oled.Oled_display(text, x, y)

    def Oled_clear(self):
        self.oled.Oled_clear()
    
    def Oled_on(self):
        self.oled.Oled_on()
    
    def Oled_off(self):
        self.oled.Oled_off()
        