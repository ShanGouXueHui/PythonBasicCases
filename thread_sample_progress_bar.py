
#-*- coding: UTF-8 -*-
import threading

import sys
import time
import os

#常数定义
PROGRESS_BAR_LENGTH = 101
#全局变量定义
COUNT = 1

class ThreadProgressBar (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print ("\n开始线程：" + self.name)
        normal_progress_bar()
        print ("\n退出线程：" + self.name)

def normal_progress_bar():
    global COUNT
    start_time = time.time()
    while(True):
        COUNT = COUNT + 1
        #进度100时退出        
        if COUNT >= PROGRESS_BAR_LENGTH:
            break
        
        end_time = time.time()
        #\r 表示将光标的位置回退到本行的开头位置,重新打印
        print("\r", end="")
        #带百分比进度，打印方块
        print("Download progress: {}%: ".format(COUNT), "▋" * (COUNT // 2),'[{:.2f}s]'.format(end_time-start_time), end="")
        sys.stdout.flush()
        
        #模拟IO读写时间
        time.sleep(0.05)
        
        
    
if __name__ == '__main__':
    #打印一个提示语
    #正常处理，初始化全局变量
    COUNT = 1
    print("正常，执行进度演示".center(PROGRESS_BAR_LENGTH // 2,"-"))
    normal_progress_bar()
    
    #打印一个提示语
    print('')
    print("多线程，执行进度演示".center(PROGRESS_BAR_LENGTH // 2,"*"))
    #多线程处理，初始化全局变量
    COUNT = 1
    # 创建新线程
    threadList = []
    for i in range(os.cpu_count()):
        t = ThreadProgressBar(i)
        t.start()
        threadList.append(t)

    for t in threadList:
        t.join()








