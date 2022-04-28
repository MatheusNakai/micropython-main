from models.Oled import Oled


class Oled_controller(object):
    
    def __init__(self):
        self.oled = Oled()

    def Oled_display(self, text:str, x:int, y:int):
        self.oled.Oled_display(text, x, y)