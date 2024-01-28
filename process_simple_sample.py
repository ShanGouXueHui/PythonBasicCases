#-*- coding: UTF-8 -*-

from multiprocessing import Process
import os
import time

#定义多进程启动的方法，参数为进程名称，用于区分不同的进程启动
#打印进程启动时间，名称，以及进程id
def processByFunc(process_name):
    print('Python函数进程 ', process_name,' 已启动，进程ID为：', os.getpid())
    #一次停顿2秒
    time.sleep(2)

#定义多进程启动的类，参数为进程名称，用于区分不同的进程启动
#打印进程启动时间，名称，以及进程id
class ProcessByClass(Process):
    def __init__(self,name):
        #如果子类重写构造函数，它必须确保它在对进程执行任何其他操作之前调用基类构造函数
        super(ProcessByClass, self).__init__()
        self.name = name
    #当start启动进程活动，它会自动将对象的 run() 方法安排在一个单独的进程中调用
    def run(self):
        print('Python类进程 ', self.name,' 已启动，进程ID为：', os.getpid())
        time.sleep(3)
      
if __name__ == '__main__':
    #函数实现进程
    #定义一个进程列表，用于调用join方法，等待进程执行结束
    start_time = time.time()
    process_list = []
    
    #有多少个cpu就建立多少个进程，否则仍会需要等待
    for i in range(os.cpu_count()):
        #线程名称已i为明
        p = Process(target=processByFunc, args=(i,))
        #启动线程
        p.start()
        process_list.append(p)
    
    #等待线程执行结束
    for i in process_list:
        p.join()
        
    end_time = time.time()
    
    #方法执行1次是2秒，如果是串行的，则总的执行时间是2*cpu数，
    #如果是多线程，则执行时间可以并行，总时长肯定是小于2*cpu数
    print(('共计{}个CPU并行运行，所有函数进程已完成耗时：{:.2f} ').format(os.cpu_count(),(end_time - start_time))) 
    
    #类实现进程
    #定义一个进程列表，用于调用join方法，等待进程执行结束
    start_time1 = time.time()
    process_list1 = []
    
    #有多少个cpu就建立多少个进程，否则仍会需要等待
    for j in range(os.cpu_count()):
        #线程名称已i为明
        p1 = ProcessByClass(str(j))
        #启动线程
        p1.start()
        process_list1.append(p1)
    
    #等待线程执行结束
    for j in process_list1:
        p1.join()
        
    end_time1 = time.time()
    
    #方法执行1次是2秒，如果是串行的，则总的执行时间是2*cpu数，
    #如果是多线程，则执行时间可以并行，总时长肯定是小于2*cpu数
    print(('共计{}个CPU并行运行，所有类进程已完成耗时：{:.2f} ').format(os.cpu_count(),(end_time1 - start_time1))) 