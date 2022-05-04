from models.Servo import Servo

class Servo_controller(object):
    
    def __init__(self):
        self.servo = Servo()
    
    def open_door(self):
        self.servo.open_door()
    
    def close_door(self):
        self.servo.close_door()

