import pyscreenshot as Im
import PIL
from PIL import Image
import keyboard
import time
from time import sleep
from keyboard import *


keyboard.wait('esc')
p,q=0,0
while True:
    p = q//10
    im = Im.grab(bbox=(675+p, 270, 722+p, 271))
    val = list(im.getdata())
    for i in val:
        if i == (83,83,83) or i == (172,172,172):
            keyboard.press_and_release('space')
            q+=1
    if keyboard.is_pressed('ctrl'):
        q=0
        break
'''
while True:
    im = Im.grab(bbox=(700, 265, 740, 270))
    im.save('hi.png')
    a = Image.open('hi.png')
    x,y = a.size
    val = list(a.getdata())
    for i in val:
        if i == (172,172,172):
            keyboard.press_and_release('space')
    
#if __name__ == '__main__':
   # part of the screen
#    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
#    im.show()

'''
