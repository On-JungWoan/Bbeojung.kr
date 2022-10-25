import pyautogui
import time
import shutil
import os

def remove(PATH):
    for (_, _, files) in os.walk(PATH):
        for file in files:
            os.remove(os.path.join(PATH,file))    

# while True:
#     print(pyautogui.position())
#     time.sleep(1)
#     if 0:
#         break

cnt = 0

while True:
    if cnt == 50:
        cnt = 0
        remove('C:/Users/USER/Desktop/Bbeojung.kr/Script/obj_detection/screenshot')
    pyautogui.screenshot(f'./screenshot/{cnt}.jpg', region=(8, 689, 600, 350))

    time.sleep(0.5)
    cnt += 1

