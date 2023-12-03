#-*- encoding:utf-8 -*- 
#%d 用于格式化输出，百分号后面的值会替代%d
print('整数示例 1: %d' %12345)
print('整数示例 2: %d' %-888)
#%0.2f 用于格式化输出，百分号后面的值会替代%0.2;0.2中的2表示2位小数
print('浮点数示例 1: %0.2f' %-0.6666)
print('浮点数示例 2: %0.2f' %-0.3333)

#字符串是以单引号'或双引号"括起来的文本
print('hello ', "world")
#转义字符\可以转义很多字符
print('示例换行\n; 示例制表符前\t制表符后.')
#直接用r''表示不转义
print(r'示例换行\n; 示例制表符前\t制表符后.')

#布尔值（True/False），and、or和not运算
print('布尔值and运算True and False: %s' % (True and False))
print('布尔值or运算 5 > 3 or 4 < 2: %s' % (5 > 3 or 4 < 2))
print('布尔值not运算 not 1 > 2: %s' % (not 1 > 2))
#空值None
print('空值None: %s' % (None))

#变量，定义变量x，然后赋值
#整数赋值
x = 10
print('赋值x = 10: %s' % (x))
#字符串赋值
x = 'string'
print("赋值x = 'string': %s" % (x))
#使用自己给自己运算
x = x + ' test'
print("赋值x = x + ' test': %s" % (x))


#内置List数据类型
fruitList = ['apple','orange','banana']
print('fruit list: ', fruitList)
print('访问fruit list索引为1的元素: ', fruitList[1])
print('访问fruit list索引为-1的元素: ', fruitList[-1])

#List末尾增加一个元素
fruitList.append('grapes')
print('fruit list末尾增加一个水果: ', fruitList)

#List末尾减少一个元素
fruitList.pop()
print('fruit list末尾减少一个水果: ', fruitList)

#List中间插入一个元素
fruitList.insert(1,'peach')
print('fruit list索引为1插入一个水果: ', fruitList)

#List中间减少一个元素
fruitList.pop(2)
print('fruit list索引为2移除一个水果: ', fruitList)

#List包含List，二维数组
typeList = ['tree','grass','seed']
fruitList.append(typeList)
print('fruit list二维数组: ', fruitList)
print('fruit list二维数组,第二个元素: ', fruitList[3][1])


#Tuple和List非常类似，但是Tuple一旦初始化就不能修改
fruitTuple = ('apple','orange','banana')
print('fruit tuple: ', fruitTuple)
print('访问fruit tuple索引为1的元素: ', fruitTuple[1])
print('访问fruit tuple索引为-1的元素: ', fruitTuple[-1])

#List可以作为Tuple的一个元素，那么List本身的值是可以变化的
typeList = ['tree','grass','seed']
fruitTuple = ('apple','orange','banana', typeList)
print('fruit tuple: ', fruitTuple)
typeList.append('leaf')
print('fruit tuple,变化typeList: ', fruitTuple)

#Dict全称dictionary，使用键-值（key-value）存储
addressBook = {'home': 'Shenzhen Nanshan', 'company' : 'Shenzhen, Baoan'}
print('dictionary, addressBook: ', addressBook)
#通过dict[key]来赋值
addressBook['mall'] = 'Shenzhen Longhua'
print('dictionary, addressBook add a mall address: ', addressBook)
#通过pop(key)来删除值
addressBook.pop('home')
print('dictionary, addressBook pop a home address: ', addressBook)


#Set不存储Value只存储Key，通过set( )方法定义
bookSet1 = set(['原则','芯片战争','棉花战争'])
bookSet2 = set(['三体','流浪地球','棉花战争','棉花战争'])
print('Set, bookSet1: ', bookSet1)
print('Set, bookSet2自动去重: ', bookSet2)

#Set并集操作
print('Set并集, bookSet1 | bookSet2: ', (bookSet1 | bookSet2))
#Set交集操作
print('Set交集, bookSet1 & bookSet2: ', (bookSet1 & bookSet2))
