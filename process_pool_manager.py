#-*- coding: UTF-8 -*-

from multiprocessing import Process, Pool, Manager

def processByFunc(process_name, my_list, my_value):
    print(process_name, ' 在List中增加数据：', my_value)
    my_list.append(my_value)
    
    
if __name__ == '__main__':
    SIZE_OF_PROCESS = 3
    with Manager() as my_manager:
        #通过Manager对象定义List
        my_list = my_manager.list()
        #Pool的默认大小是CPU的核数，样例就是用少量几个来测
        pool = Pool(SIZE_OF_PROCESS)
        #多出2个进程，要等前面SIZE_OF_PROCESS个进程执行完毕才执行
        for i in range(SIZE_OF_PROCESS + 2):
            pool.apply_async(func=processByFunc, args=(i,my_list, i*10000))
        
        #调用close()之后就不能继续添加新的Process了
        pool.close()
        #Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()
        pool.join()
        
        print('my_list最终值，应该是所有线程修改后的值，如下：')
        print(my_list)