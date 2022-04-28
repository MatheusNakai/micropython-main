from controllers.Oled_controller import Oled_controller

class Oled_UC(object):

    def __init__(self):
        self.oled_controller = Oled_controller()
        
    def oled_text(self,text,x,y):
        self.oled_controller.oled_text(text,x,y)

    def display_clear(self):
        self.oled_controller.display_clear()

    def display_on(self):
        self.oled_controller.display_on()
    
    def display_off(self):
        self.oled_controller.display_off()