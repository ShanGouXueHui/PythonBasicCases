# -*- coding: UTF-8 -*-


#导入 pyplot 库，并设置一个别名 plt
import matplotlib
import matplotlib.pyplot as plt
#导入 numpy 库，并设置一个别名 np
import numpy as np

from PIL import Image

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    
    # 查询系统中支持哪些字体
    # font_in_system =sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

    # for f in font_in_system:
    #     print(f)
        
    #Matplotlib 中文显示不友好, 需设置字体
    plt.rcParams['font.family'] = 'Microsoft YaHei'  
    #plot 1：绘线图
    #预制坐标值
    x_plot = np.array([10, 22,33,44])
    y_plot = np.array([1, 9, 16, 39])
    
    #设置子图，第一行第1个子图
    plt.subplot(2, 3, 1)
    #使用破折现，圆点节点
    plt.plot(x_plot, y_plot, linestyle = 'dashed', marker = 'o')
    
    #设置轴标签和标题
    plt.title('Plot 1: 线图示例')
    plt.xlabel('x - Axis')
    plt.ylabel('y - Axis')
    
    #显示网格线, 可以通过axis='x'或者'y'仅显示轴方向网格线
    #color：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串
    #linewidth：设置线的宽度，可以设置一个数字。
    plt.grid(color = 'g', linewidth = 0.3)
    
    #plot 2：散点图
    x_scatter = np.array([11, 25, 33, 42, 71, 86]) 
    y_scatter = np.array([1, 23, 39, 46, 77, 78])
    
    #设置子图，第一行第2个子图
    plt.subplot(2, 3, 2)
    plt.scatter(x_scatter, y_scatter)
    
    #设置轴标签和标题
    plt.title('Plot 2: 散点图示例')
    plt.xlabel('x - Axis')
    plt.ylabel('y - Axis')
    
    #plot 3: 柱形图
    x_bar = np.array(["Petrol Car", "Diessel Car", "EV Car", "Flying Car"])
    y_bar = np.array([50000,30000, 20000, 1000])
    
    #设置子图，第一行第3个子图
    plt.subplot(2, 3, 3)
    plt.bar(x_bar, y_bar)
    #设置轴标签和标题
    plt.title('Plot 3: 柱状图示例')
    plt.ylabel('月度销售数量')
    
    
    #plot 4: 饼图
    y_pie = np.array([50, 20, 20, 10])
    labels_pie = ['苹果', '香蕉', '橘子', '提子']
    #设置子图，第2行第1个子图
    plt.subplot(2, 3, 4)
    plt.pie(y_pie, 
            labels=labels_pie,
            autopct=lambda p: '{:.0f}({:.1f}%)'.format(p * sum(y_pie) / 100,p))
    #设置标题
    plt.title('Plot 4: 饼图示例')
    
    #plot 5: 直方图
    #生成随机数作为输入数据,表示要绘制直方图的数据，可以是一个一维数组或列表
    cpu_usage_sample = np.random.randint(100)
    #设置子图，第2行第2个子图
    plt.subplot(2, 3, 5)
    #bins：可选参数，表示直方图的箱数。默认为10。
    #alpha: 透明度
    plt.hist(cpu_usage_sample, bins = 30, color = 'red', edgecolor = 'white', alpha = 0.7)
    #设置轴标签和标题
    plt.title('Plot 5: 直方图示例')
    plt.xlabel('CPU利用率')
    plt.ylabel('模块')
    
    #plot 6: 显示图片示例
    #加载图片
    img = Image.open('img.jpg')
    #转换为数组
    img_data = np.array(img)
    #设置子图，第2行第2个子图
    plt.subplot(2, 3, 6)
    #绘制图片
    plt.imshow(img_data)
    plt.title('Plot 6: 显示图片示例')
    #隐藏坐标
    plt.axis('off')
    
    #画布级标题
    plt.suptitle("多种绘图实例")
    plt.show()
    





