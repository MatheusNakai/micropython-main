

from controller.Servo_controller import Servo_controller

class Servo_UC(object):
    
    def __init__(self):
        self.servo_controller = Servo_controller()
    
    def open_door(self):
        self.servo_controller.open_door()
    
    def close_door(self):
        self.servo_controller.close_door()
