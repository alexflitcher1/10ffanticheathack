# 10fastfingers anticheat hack
# including libraries
import pytesseract
import cv2
import keyboard
import pyautogui as pag
import matplotlib.pyplot as plt
from PIL import Image


while True:
    # check press the start-button
    if (keyboard.is_pressed("esc")):
        # doing screenshot require region
        pag.screenshot("1.png", region=(598, 323, 1184, 483)) # (left, top, width, and height) 
        # read the image with OpenCV
        image = cv2.imread("1.png")
        # get the text of the screenshot
        string = pytesseract.image_to_string(image)
        print(string)
        # write the text
        keyboard.write(string, delay=0.04)
        break
