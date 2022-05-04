from models.Oled import Oled


class Oled_controller(object):
    
    def __init__(self):
        self.oled = Oled()

    def display_text(self, text:str, x:int, y:int):
        self.oled.oled_display(text, x, y)

    def display_clear(self):
        self.oled.display_clear()
    
    def display_on(self):
        self.oled.display_on()
    
    def display_off(self):
        self.oled.display_off()
        