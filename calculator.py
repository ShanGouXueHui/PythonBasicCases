# -*- coding: utf-8 -*-

'''
凑着这个例子，简单说一下注释的用法，详细的可以参考Python、Google编程规范或者其他大公司广泛的规范。
注意（^_^）：我后面的例子用于教程示例，代码逻辑简单，不会做这么详细的说明，主要还是“讲代码的思路”。

一、为啥需要注释
1、虽然现在写代码要求，代码可以“自注释”，也就是代码无需注释，看代码就可以看懂，
但读书还有“温故而知新”这种说法，说白了一百个人看有一百个解读，所以这种要求只是一种理想。
2、注释就是对代码的解释和说明，提高程序代码的可读性；就是让维护代码的人，学习代码的人，
利旧代码的人可以准确无误的理解程序员的目的，以及编程trick里的弯弯绕。

二、注释的分类
1、行注释：#开头的，在符号后那一行不会被编译，只是代码可读的参考
2、块注释：\'''开头的，块注释符号中间的部分不会被编译，只是代码可读的参考；
也叫DocStrings，可以通通过.__doc__在程序中调用（一般用来首行简述模块、函数、类功能，
第二行空行，第三行为函数的具体描述。）

三、应用场景
1、python文件开头的模块注释 - 用于说明模块作用、作者、创建日期、修订人、修订内容，修订日期等便于追溯
例如：
\'''
Author: 山狗学会
Description: 实现基本的加减乘除算法，作为验证单元测试的目标模块
Create Date： 2024-1-6
Modify by: xxxx
Modification: xxx
Modify Date: xxxx
\'''
2、函数、类 -- 说明函数功能，入参、返回函数、抛出异常等
例如：
\'''
Description: 演示基本算数加法计算
Parameters:
    a - 加法中第一个数字
    b - 加法中第二个数数字

Returns:
    sum - 返回两数相加求和值

Raises:
    exceptionValue - 非数字异常
\'''   
3、单行注释 - 主要是关键代码逻辑中解释，或者有点技巧的代码做一下解读
例如：
#xxxxxxx

4、特殊注释 - 文章开头两行注释，一个指定默认解释器（Linux/OS X有用，可以直接执行.py文件），
一个是指定文件编码，避免非英文乱码
例如：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

#Python的标准库logging，用作记录日志，可以满足大多数的日志记录需求
import logging

'''logging简介
默认分为六种日志级别（括号为级别对应的数值）：
NOTSET(0)
DEBUG(10)
INFO(20)
WARNING(30)
ERROR(40)
CRITICAL(50)
还可以自动以级别（一般人用不上），自定义级别的数值，不能和标准级别一样

logging 使用非常简单，使用 basicConfig() 方法就能满足基本的使用需要，
如果方法没有传入参数，默认 WARNING，那么WARNING和
比WARNING更严重的日志都会被打印出来
'''

#设置全局logging配置、以及日志格式
logging.basicConfig(filename="./PythonCases/run.log", 
                   filemode="w",                    
                   format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                   datefmt="%d-%M-%Y %H:%M:%S", 
                   level=logging.INFO,
                   encoding='utf-8')

class BasicCalculator(object):
    
    def add(self, a, b):
        self.parameterTypeCheck(a, b)
        logging.info('执行BasicCalculator.add方法，入参为%d, 和%d,反馈结果为%d.' % (a, b, a+b) )
        return a + b
    def minus(self, a, b):
        self.parameterTypeCheck(a, b)
        logging.warning('执行BasicCalculator.minus方法，入参为%d, 和%d,反馈结果为%d.' % (a, b, a-b) )
        return a - b
    
    def divide(self, a, b):
        self.parameterTypeCheck(a, b)
        logging.error('执行BasicCalculator.divide方法，入参为%d, 和%d,反馈结果为%d.' % (a, b, a/b) )
        return a/b
    
    def multiply(self, a, b):
        self.parameterTypeCheck(a, b)
        logging.critical('执行BasicCalculator.multiply，入参为%d, 和%d,反馈结果为%d.' % (a, b, a*b) )
        return a * b
    
    #如果类型不对，则抛出异常
    #高级语言通常都内置了一套try...except...finally...的错误处理机制来捕捉和处理异常，
    #Python机制是类似的
    def parameterTypeCheck(self, a, b):
        if not ((type(a) in(int, float)) and (type(b) in(int, float)) ):
            logging.critical('执行BasicCalculator.multiply，入参为%s, 和%s,反馈结果为%s.' % (a, b, '输入的字符不是数字，请输入数字进行运算。') )
            raise ValueError('输入的字符不是数字，请输入数字进行运算。')