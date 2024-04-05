import cv2
import numpy as np
import subprocess
import time

def calculate_luminance(image):
    if len(image.shape) == 3:
        grayscale_image = np.dot(image[..., :3], [0.299, 0.587, 0.114])
    else:
        grayscale_image = image
    
    luminance = np.mean(grayscale_image) / 255.0
    
    return luminance

def handle_brightness(lum):
    global last_lt
    if lum < 0.1:
        lt = 10
    elif lum < 0.3:
        lt = 30
    elif lum < 0.5:
        lt = 50
    else:
        lt = 70
    subprocess.run(['brightnessctl', 'set', f'{lt}%'])

#cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

rval, frame = vc.read()
lum = calculate_luminance(frame)
handle_brightness(lum) 
#time.sleep(1)

#vc.release()
#cv2.destroyWindow("preview")

