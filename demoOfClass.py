# -*- coding: utf-8 -*-

#Python中任何类，最终都可以追溯到根类object，是object的子类
class Car(object):
    #Python中双下划线开头的是私有变量，不能直接访问，例如__timeFor100KM
    #如果变量前后都有双下划线，表示可以访问但不建议，例如__timeFor100KM__
    #其实，私有变量也可以用类名访问，也就是说Python本身没有任何机制阻止你干坏事，一切全靠自觉，主打的一个自由
    __timeFor100KM = 3.6
   
    #__init__是类的构造函数，创建实例的时候必被自动调用，如果没有特殊要求，可以不定义，默认从 object 中继承
    #仅有子类需要增加自己的内容，采用重写，会自动覆盖父类的__init__
    #重写__init__时需要注意：第一个参数必须是 self，后续参数则可以自由指定，和定义函数没有任何区别。
    def __init__(self) :
        print("你刚刚构建了一个Car实例：", self.__class__.__name__)
    
    def printCarType(self):
        print('这是一辆通用车！')
    
    #定义属性 __timeFor100KM的set函数，相比于直接访问属性，他可以定义一些参数检查逻辑
    def setTimeFor100KM(self,duration):
        if duration <= 0 or duration > 10:
            raise ValueError("汽车百公里加速值必须在0秒~10秒之间，请设置正确的值。")
        self.__timeFor100KM = duration
    #定义属性 __timeFor100KM的get函数, 只读，屏蔽属性
    def getTimeFor100KM(self):
        return self.__timeFor100KM
    
    #如果你想直接通过实例直接访问属性，同时又想做参数检查，可以使用类的装饰器功能
    #@property用于设置只读属性，即get函数    
    @property
    def costPerKM(self):
        #需要注意，属性的名字不要和函数重名，会导致解释器分不清是函数还是属性，导致异常。
        return self._costPerKM
    #@function.setter用于标识set函数，可以用于检查参数
    @costPerKM.setter
    def costPerKM(self, unitPrice):
        if unitPrice <= 0 or unitPrice > 10:
            raise ValueError('油的单价必须在0元和10元之间，请设置正确的值。')
        self._costPerKM = unitPrice
    
    #如果可以通过属性值计算出来，则只需只读属性
    @property 
    def costOf100KM(self):
        return self._costPerKM*100

#定义一个电动车的子类
class EVCar(Car):
    #所有方法继承父类方法，仅重写printCarType()函数，用于标识车的类型
    def printCarType(self):
        print("这是一辆电动车！")

#继续定义一辆汽油车
class PetrolCar(Car):
    #所有方法继承父类方法，仅重写printCarType()函数，用于标识车的类型
    def printCarType(self):
        print("这是一辆汽油车！")

#还可以定义一辆柴油车，这就是类的可扩展性，可以允许新增子类
class DieselCar(Car):
    #所有方法继承父类方法，仅重写printCarType()函数，用于标识车的类型
    def printCarType(self):
        print("这是一辆柴油车！")

#这个全局的方法，就可以用来展示类的封闭性，不需要修改依赖Car类型，用子类传入即可打印子类方法
#同样的方法打印出来不同的内容，这也是类的多态性演示
def getCarType(car):
    car.printCarType()
    

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #定义一个通用车
    car = Car()
    
    #定义一个电车
    evCar = EVCar()
    #设置速度和每公里油耗价格
    evCar.setTimeFor100KM = 3.6
    evCar._costPerKM = 1
    #打印速度值，百公里油耗费用
    print("电动车百公里加速秒数：%0.2f" % evCar.getTimeFor100KM())
    print("电动车百公里油耗费用：",evCar.costOf100KM,"元。")
    print('')
    
    #定义一个汽油车
    petrolCar = PetrolCar()
    #设置速度和每公里油耗价格
    petrolCar.setTimeFor100KM = 7
    petrolCar._costPerKM = 6.16
    #打印速度值，百公里油耗费用
    print("电动车百公里加速秒数：",petrolCar.getTimeFor100KM())
    print("电动车百公里油耗费用：",petrolCar.costOf100KM,"元。")
    print('')
    
    #定义一个柴油车
    dieselCar = DieselCar()
    #设置速度和每公里油耗价格
    dieselCar.setTimeFor100KM = 9
    dieselCar._costPerKM = 5.13
    #打印速度值，百公里油耗费用
    print("电动车百公里加速秒数：",dieselCar.getTimeFor100KM())
    print("电动车百公里油耗费用：",dieselCar.costOf100KM,"元。")
    print('')
    
    carList = [car, evCar, petrolCar, dieselCar]
    print("使用getCarType(car)方法，打印car type, 无需单独定义三个函数:")
    for c in carList:
        getCarType(c)