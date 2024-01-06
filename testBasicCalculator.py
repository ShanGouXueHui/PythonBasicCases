# -*- coding: utf-8 -*-

'''
依据TDD理念，测试代码可以先于代码开发完成（个人觉得，还是至少要把代码框架搭好才能开始，
需求和代码框架设计还是要放在前面的，否则不知道要测什么），所以单元测试可以放在单独文件开发，
与开发的发布代码互不影响。
'''

#导入单元测试模块,类似于java中的junit；
#根据需要还可以用pytest，doctest，mock，coverage等模块
#更多资源参考http://pythontesting.net
import unittest
#导入要测试的类
import calculator


#定义测试类
'''
unittest核心的方法是：断言assertxxx()函数
包括，assertEqual()来检查预期的输出；调用assertTrue()或assertFalse()来验证一个条件；调用assertRaises()来验证抛出了一个特定的异常
'''
#编写单元测试时，需要编写一个测试类，从unittest.TestCase继承。
class CasesOfBasicCalculator(unittest.TestCase):
    #setUp和tearDown处理测试前后的准备和清理工作
    #这两个方法会分别在每调用一个测试方法的前后分别被执行。
    #避免在每个测试方法中重复相同的代码
    def setUp(self):
        self.test_class = calculator.BasicCalculator()
    def tearDown(self):
        del self.test_class
        
    #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，
    #测试的时候不会被执行。
    def test_add_16_8(self):
        self.assertEqual(self.test_class.add(16,8), 24)
        
    def test_minus_16_8(self):
        self.assertEqual(self.test_class.minus(16,8), 8)
    
    def test_divide_16_8(self):
        self.assertEqual(self.test_class.divide(16,8), 2)
    
    def test_multiply_16_8(self):
        self.assertEqual(self.test_class.multiply(16,8), 128)
    
    def test_parameterTypeCheck_sixty_eight(self):
        self.assertRaises(ValueError, self.test_class.parameterTypeCheck,'sixty', 'eight')
    

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中
if __name__ == "__main__":
    unittest.main()