import time
import random
import win32api,win32con

#鼠标点击
def fire():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.randint(50,75)/1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(random.randint(25,40)/1000)
#键盘按下T
def KeyC_T():
    win32api.keybd_event(84,0,0,0)
    time.sleep(random.randint(15,25)/1000)
    win32api.keybd_event(84,0,win32con.KEYEVENTF_KEYUP,0)
#键盘按下G
def KeyC_G():
    win32api.keybd_event(71,0,0,0)
    time.sleep(random.randint(15,25)/1000)
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0)
#键盘按下key 
def KeyC(key):
    win32api.keybd_event(key,0,0,0)
    time.sleep(random.randint(15,25)/1000)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)


while 1:
    k=[1,1,1,1,1,1,1]
    time.sleep(0.0001)
    M_u=win32api.GetAsyncKeyState(0x06)
    M_d=win32api.GetAsyncKeyState(0x05)
    M_m=win32api.GetAsyncKeyState(0x04)
    for i in range(7):
        k[i]=win32api.GetAsyncKeyState(97+i)
    #判定
    if M_u<0:
        fire()
    if M_d<0:
        KeyC_T()
        KeyC(49)
        KeyC_T()
        KeyC_G()
    if M_m<0:
        KeyC_T()
        KeyC(50)
        KeyC_T()
        KeyC_G()
    for i in range(7):
        if k[i]<0:
            KeyC_T()
            KeyC(i+49)
            KeyC_T()


