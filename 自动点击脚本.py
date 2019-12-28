import pyautogui
import random

#移动到目标区域的一个随机点,在limitime点击随意次数
def rndClock_l(left,top,right,botton,limitime):
    pass

#移动到目标取区域内的一个随机点，点击经过后等待delaytime,并在limitime可以随机点击
#模式为，移动->等1秒->点击->等一定秒
def rndClick_d(left,top,right,botton,delaytime,limitime=0):
    subtime=3
    x=random.randrange(int(left),int(right))
    y=random.randrange(int(top),int(botton))
    pyautogui.moveTo(x,y)      #点击
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.press('ctrl')   #点击特效
    rndClock_l(left,top,right,botton,limitime)
    rdelaytime=delaytime+random.random()*subtime           #随机时间
    pyautogui.sleep(rdelaytime-limitime)

#接受一组点，依次点击
def continueClick(nodes):
    for node in nodes:
        rndClick_d(node[0], node[1], node[2],node[3],node[4],node[5])

#通过tagPicture以确认点击时机，并且应对升级、AI失误等特殊情况,flag=1时为剿灭模式，flag=0时为其他模式
#模式为，查找->等10秒->点击->等10秒
def checkClick(endpoint,flag):#endpoint结束标志
    delaytime=10
    while(True):
        print('升级:', pyautogui.pixelMatchesColor(1472,581,(34,182,249),tolerance=10) and pyautogui.pixelMatchesColor(1472,587,(34,182,249),tolerance=10) and pyautogui.pixelMatchesColor(1472,597,(34,182,249),tolerance=10))
        if (pyautogui.pixelMatchesColor(1472,581,(34,182,249),tolerance=10) and pyautogui.pixelMatchesColor(1472,587,(34,182,249),tolerance=10) and pyautogui.pixelMatchesColor(1472,597,(34,182,249),tolerance=10)):  # 升级点击
            pyautogui.sleep(10)
            rndClick_d(368 - 50, 754 - 50, 368 + 50, 754 + 50, delaytime)#点击位置统一化
        if flag==1:
            print('剿灭确认:',pyautogui.pixelMatchesColor(426,514,(0,152,220),tolerance=10))
            if(pyautogui.pixelMatchesColor(426,514,(0,152,220),tolerance=10)):#剿灭确认点击
                pyautogui.sleep(10)
                rndClick_d(368 - 50, 754 - 50, 368 + 50, 754 + 50, delaytime)
        print('结算:', pyautogui.pixelMatchesColor(endpoint[0], endpoint[1], endpoint[2], tolerance=10))
        if (pyautogui.pixelMatchesColor(endpoint[0], endpoint[1], endpoint[2], tolerance=10)):  # 结算点击
            pyautogui.sleep(10)
            rndClick_d(368 - 50, 754 - 50, 368 + 50, 754 + 50, delaytime)
            break
        print()
        pyautogui.sleep(10)


if __name__ == '__main__':
    pyautogui.sleep(5)
    #0-其他  1-剿灭
    mode=0
    times =7
    if mode==0:
        loopnode=[(1532,925,1756,974,10,0),(1540,579,1670,876,10,0)]
        endpoint=[373, 771, (63, 245, 255)]
        flag=0
    else:
        loopnode=[(1532,925,1756,974,10,0),(1540,579,1670,876,10,0)]
        endpoint=[841,846,(239,203,7)]
        flag=1
    #开始刷
    for i in range(times):
        print('第',i+1,'次')
        continueClick(loopnode)
        checkClick(endpoint, flag)