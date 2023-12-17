#-*- encoding:utf-8 -*-
from datetime import datetime
import functools
from operator import itemgetter

#定义一个decorator，在调用一个函数时，自动打印调用的函数名称和时间戳。
def autoAddLogs(function):
    #外衣逻辑
    @functools.wraps(function)
    def wrapper(*args, **kw):      
        #函数对象自带__name__属性, datetime是内置函数
        print('At time ', datetime.now(), ',calls function', function.__name__)
        
        #实际函数逻辑
        return function(*args, **kw)
    return wrapper

@autoAddLogs
def hello():
    print('hello decorator')
    
#对自然数n，对小于n的自然数平方值求和。
def sum(n):
   
    sum = 0
    for i in range(n):
        sum = sum + (lambda x: x*x)(i)
        
    print('对小于n的自然数平方值求和, 当n为', n, '时，和为：', sum)
    

#只看美女的信息
def isGirl(gender):
    if gender == 'female':
        return True
       
    else:
        return False         

def countGirls(genderList):
    noOfGirls = len(list(filter(isGirl, genderList)))
    print('Totally have %d girls!' % noOfGirls)
    
#按照汽车的价格做排序,制定第二个值为排序标准
def dictSortByValue(theDict):
    print(sorted(theDict, key=itemgetter(1), reverse=True))
    

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    
    carPriceDict = [('bentley', 300), ('BMW', 100), ('Mercedes-Benz', 150), ('Huawei', 25),('Tesla', 70)]
    dictSortByValue(carPriceDict)
    
    # genderList = ['male','female','female','male','female']
    # countGirls(genderList)
      
    # sum(3)    
    # hello()