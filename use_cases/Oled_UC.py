from controller.Oled_controller import Oled_controller

class Oled_UC(object):

    def __init__(self):
        self.oled_controller = Oled_controller()
        
    def display_text(self,text,x,y):
        self.oled_controller.display_text(text,x,y)