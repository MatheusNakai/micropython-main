from use_cases.FileRW_UC import FileRW_UC
from use_cases.Keypad_UC import Keypad_UC
from use_cases.Oled_UC import Oled_UC
from models.User import User
from machine import Pin, I2C




def run():
    """
    The main function of the system.
    """
    led = Pin(28, Pin.OUT)
    pir = Pin(16,Pin.IN, Pin.PULL_UP)
    led.low()
    oled = Oled_UC()
    keypad = Keypad_UC()
    fileRW= FileRW_UC()
    non_number = ["A","B","C","D","*","#"]
    password = []

    
    oled.display_text("Welcome",0,0)
    print("Hello World!")