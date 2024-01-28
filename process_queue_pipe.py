#-*- coding: UTF-8 -*-

from multiprocessing import Process, Queue,Pipe
import time
import os


#定义多进程启动的类，参数为进程名称，用于区分不同的进程启动
#打印进程启动时间，名称，以及进程id
class ProcessByClass(Process):
    def __init__(self,name,q):
        #如果子类重写构造函数，它必须确保它在对进程执行任何其他操作之前调用基类构造函数
        super(ProcessByClass, self).__init__()
        self.name = name
        self.q = q
    #当start启动进程活动，它会自动将对象的 run() 方法安排在一个单独的进程中调用
    def run(self):
        print('Python类进程 ', self.name,' 已启动，开始发送数据')
        self.q.put('进程'+self.name+'通过Queque通信!')

#定义多进程启动的方法，参数为进程名称，用于区分不同的进程启动
#打印进程启动时间，名称，以及进程id
def processByFunc(process_name,conn):
    print('Python函数进程 ', process_name,' 已启动，发送信息中...')
    conn.send('子进程 ' + process_name + '向你问好！')
    print('Python函数进程 ', process_name,' 接收信息中...')
    print('进程 ' + process_name + ' 接收消息内容：' + conn.recv())
    conn.close()

if __name__ == '__main__':
    SIZE_OF_PROCESS = 3
    print('----------Queue----------')
    #定义一个队列
    q = Queue()
    start_time = time.time()
    
    #定义一个进程列表，用于调用join方法，等待进程执行结束  
    process_list = []
  
    for j in range(SIZE_OF_PROCESS):
        #线程名称已i为明
        p = ProcessByClass(str(j),q)
        #启动线程
        p.start()
        process_list.append(p)
    
    #等待线程执行结束
    for j in process_list:
        p.join()
        
    end_time = time.time()
    
    #获取各线程通过queue发送的内容（1主线程 <-->多子线程）
    print('通过Queue获取通信内容：') 
    for j in range(SIZE_OF_PROCESS):
        print(q.get())    
    
    print('通过Queue获取通信内容结束！') 
    
    
    print('----------Pipe----------')
    #生成一个双向管道, conn1给主线程用吗，conn2给子线程用
    conn1, conn2 = Pipe()
    p1 = Process(target = processByFunc, args=('child process',conn2))
    p1.start()
    print('主进程main接收信息中...')
    print('主进程接收消息内容：' + conn1.recv())
    print('主进程main发送信息中...')
    conn1.send('hello child process!')
    p1.join()
    print('通过Pipe通信结束！') 
    