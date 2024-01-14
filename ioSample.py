#-*- coding: UTF-8 -*-
import os
import pickle

#定义一个测试类
class Book(object):
    def __init__(self, name, author, numOfSold):
        self.name = name
        self.author = author
        self.numOfSold = numOfSold
    
    def isBookPopular(self):
        if self.numOfSold > 100000:
            return "<" + self.name + "> 是一本畅销书!"
    

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #Console示例，键盘是输入设备，屏幕是输出设备
    inputStr = input('请输入你的姓名：') 
    print('你好，',inputStr)
    
    #文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用,无法释放资源。
    # 所以，为保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
    try:
        myFile1= open('D:/Shangouxuehui_Git/PythonCases/IOSampleContect.txt', 
                     'r',
                     encoding='utf-8')
        print('try ... finally 语句下文件读测试')
        print(myFile1.read())
    finally:
        if myFile1:
            myFile1.close()
    
    #Python中还可以使用with语句来自动调用close()方法
    with open('D:/Shangouxuehui_Git/PythonCases/IOSampleContect.txt', 
              'a+',
              encoding='utf-8') as myFile2:
        print('with ... as 语句下文件写测试')
        myFile2.write('\n Hello, Andy!')
    
    #os模块相关函数测试
    print('os名称：', os.name)
    print('os环境变量path信息：',os.environ.get('PATH'))
    print('获取当前目录绝对地址：',os.path.abspath('.'))
    print('拆分文件名：',
          os.path.split('D:/Shangouxuehui_Git/PythonCases/IOSampleContect.txt'))
    
    print('打印当前目录下的目录文件....')    
    for x in os.listdir('.'):
        print(x)
    
    # 序列化自定义类的对象
    print('序列化book对象...')
    with open("./PythonCases/json_book.pickle", "wb") as j:
        # 创建一个类对象
        b1 = Book("三体", '大刘', 1000000)
        print(b1.isBookPopular())

        # 序列化自定义类的对象
        pickle.dump(b1, j)
        
    print('')
    print('反序列化book对象...')
    # 反序列化自定义类的对象
    with open("./PythonCases/json_book.pickle", "rb") as j:
        # 从文件中反序列化出对象
        b2 = pickle.load(j)
        print(b2.isBookPopular())
                
            
            


