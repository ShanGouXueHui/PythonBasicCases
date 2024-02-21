# -*- coding: utf-8 -*-

import socket
import threading
import time

#定义全局List变量，存储客户端连接，用于相互转发消息
socket_client_List = []

#从客户端收到消息后，转发给其他几个客户端
def join_conference(socket_client:socket.socket, addr_client):
    print('Accept a new connection from ', addr_client)
    #给客户端发送欢迎语
    socket_client.send(b'Welcome to join the group')
    
    #等其他客户端入群（建立连接）
    time.sleep(3)
    
    while True:
        #数据以字符串形式返回，bufsize指定要接收的最大数据量
        msg = socket_client.recv(1024)
        
        for s in socket_client_List:
            s.send(msg)

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。
    #设置监听端口9000
    socket_server.bind(('127.0.0.1', 9000))

    #开始监听端口，传入的参数指定拒绝连接之前，操作系统可以挂起的最大连接数量
    socket_server.listen(5)
    print('群消息转发服务已启动，开始提供服务......')

    #过一个永久循环来接受来自客户端的连接
    while True:
        #等待客户端连接
        socket_client, addr_client = socket_server.accept()
        socket_client_List.append(socket_client)
        #通过多线程，存储多个客户端连接
        t = threading.Thread(target=join_conference, args=(socket_client, addr_client))
        t.start()