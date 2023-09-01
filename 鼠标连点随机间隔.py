import time
import random
import win32api,win32con

#鼠标点击
def fire():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.randint(70,150)/1000)#按下持续时间
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(random.randint(20,40)/1000)#松开后等待时间
#键盘按下key 
def KeyC(key):
    win32api.keybd_event(key,0,0,0)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)

while 1:
    time.sleep(0.0001)
    M_u=win32api.GetAsyncKeyState(0x06)#上侧键
    M_d=win32api.GetAsyncKeyState(0x05)#下侧键
    #判定
    if M_u<0:
        fire()
    if M_d<0:
        KeyC(72)#72是H键
