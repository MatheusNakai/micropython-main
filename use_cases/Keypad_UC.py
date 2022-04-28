from controllers.Keypad_controller import Keypad_controller

class Keypad_UC(object):

    def __init__(self):
        self.keypad_controller = Keypad_controller()
        
    def Keypad4x4Read(self):
        return self.keypad_controller.Keypad4x4Read()