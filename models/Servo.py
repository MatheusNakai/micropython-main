import machine
from machine import Pin, PWM

class Servo(object):
    
    def __init__(self):
        self.pwm = PWM(Pin(2))
        self.pwm.freq(50)
        self.state = 'close'
    
    def open_door(self):
        if self.state== 'close':
            self.pwm.duty_u16(5000)
            self.state = 'open'
    
    def close_door(self):
        if self.state== 'open':
            self.pwm.duty_u16(100)
            self.state = 'close'
