import time
import usb_hid
from adafruit_hid.keycode import Keycode as kc
from adafruit_hid.keyboard import Keyboard as kb
from adafruit_hid.mouse import Mouse as mo
import board
import digitalio

btnList = [
    digitalio.DigitalInOut(board.GP1),
    digitalio.DigitalInOut(board.GP2),
    digitalio.DigitalInOut(board.GP3),
    digitalio.DigitalInOut(board.GP4),
    digitalio.DigitalInOut(board.GP5),
    digitalio.DigitalInOut(board.GP6)
]

myKb = kb(usb_hid.devices)
myMo = mo(usb_hid.devices)

def btn1_macro():
    myMo.click(mo.MIDDLE_BUTTON)
    myMo.click(mo.MIDDLE_BUTTON)

def btn2_macro():
    myKb.send(kc.TWO)

def btn3_macro():
    myKb.send(kc.THREE)

def btn4_macro():
    myKb.send(kc.FOUR)

def btn5_macro():
    myKb.send(kc.FIVE)

def btn6_macro():
    myKb.send(kc.SIX)

macrosList = [
    btn1_macro,
    btn2_macro,
    btn3_macro,
    btn4_macro,
    btn5_macro,
    btn6_macro,
]
keyZipList = list(zip(btnList, macrosList))

for btn in btnList: 
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN

isListening = { ii: False for ii in range(len(btnList)) }

while True:
    for ii, keyTup in enumerate(keyZipList):
        iiBtn, iiMacro = keyTup

        if isListening[ii]:
            if iiBtn.value:
                iiMacro()
                isListening[ii] = False
        else:
            if not iiBtn.value:
                isListening[ii] = True
