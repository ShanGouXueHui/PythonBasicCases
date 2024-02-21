# -*- coding: utf-8 -*-

import socket
import datetime
import time

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #与服务端建立连接,主动初始化TCP服务器连接，一般address的格式为元组（hostname,port）
    socket_server.connect(('127.0.0.1', 9000))
    
    #接收群欢迎消息
    print(socket_server.recv(1024).decode('utf-8'))
    
    #发送一条消息，使用时间来区分发自与不同客户端
    msg = 'client group message: ' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    socket_server.send(msg.encode('utf-8'))
    
    #接收其他客户端发的消息
    while True:
        #数据以字符串形式返回，bufsize指定要接收的最大数据量
        msg = socket_server.recv(1024)
        print('获取一条群消息：', msg.decode('utf-8'))




