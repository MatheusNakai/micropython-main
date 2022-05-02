from use_cases.FileRW_UC import FileRW_UC
from use_cases.Keypad_UC import Keypad_UC
from use_cases.Oled_UC import Oled_UC
from models.User import User
from machine import Pin, I2C
import utime

def check_password(list_of_dict, password):
    """
    Check if the password is correct.
    """
    for user in list_of_dict:
        if user["password"] == password:
            return True
    return False


def run():
    """
    The main function of the system.
    """
    led = Pin(28, Pin.OUT)
    movement_sensor = Pin(16,Pin.IN, Pin.PULL_UP)
    led.low()
    oled = Oled_UC()
    keypad = Keypad_UC()
    fileRW= FileRW_UC()

    list_user = fileRW.read()
    non_number = ["A","B","C","D","*","#"]
    number = ["1","2","3","4","5","6","7","8","9","0"]
    password = ""
    i=0
    oled.Oled_text("Welcome",0,0)

    while 200>i:
        if movement_sensor.value()==0:
            led.low()
            utime.sleep(0.2)
            oled.display_clear()
            oled.display_off()
        
        else:
            led.high()
            utime.sleep(0.1)

            oled.display_clear()
            oled.display_on()
            oled.Oled_text("Enter Password:",0,0)
            key = keypad.Keypad4x4Read()
            if key in non_number:
                if key == non_number[0]:
                    # Turn off the display and clear password
                    oled.display_off()
                    try:
                        password = ""
                    except:
                        pass
                elif key == non_number[1]:
                    # Clear password
                    try:
                        password = ""
                    except:
                        pass
                elif key == non_number[2]:
                    # Delete the last character in the password
                    try:
                        password = password[:-1]
                    except:
                        pass
                elif key == non_number[3]:
                    oled.display_clear()
                    # Submit the password
                    if len(password)<5:
                        oled.Oled_text("Password too short",0,1)

            if key in number:
                password += key
                oled.Oled_text(password,0,1)

            if len(password)==5:
                    if check_password(list_user, password):
                        oled.Oled_text("Welcome",0,0)
                        oled.display_on()
                        utime.sleep(1)
                        oled.display_clear()
                        oled.display_off()