from models.Keypad import Keypad

class Keypad_controller(object):

    def __init__(self):
        self.keypad = Keypad()

    def Keypad4x4Read(self):
        return self.keypad.Keypad4x4Read()