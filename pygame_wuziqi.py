
# -*- coding: utf-8 -*-

import pygame
import sys
import time

from pygame import locals

#棋盘尺寸预定义,单位px
QIPAN_EDGE_LENGTH :int = 20
QIPAN_SIZE_OF_CHESS_PIECES :int = 18
QIPAN_GAP_OF_CHESS_PIECES :int = 2
QIPAN_GAP_OF_TWO_LINE :int = 40
QIPAN_LENGHT :int = 720

QIPAN_TOTAL_NUM_OF_CHESS = QIPAN_SIZE_OF_CHESS_PIECES * QIPAN_SIZE_OF_CHESS_PIECES

#棋盘颜色，RGB
QIPAN_COLOR = [238, 154, 73]
#棋盘画线黑色
QIPAN_LINE_COLOR = [0,0,0]
#线粗细
QIPAN_BOLD_LINE_SIZE :int = 4
QIPAN_NORMAL_LINE_SIZE :int = 2

#棋子颜色
CHESS_PIECES_WHITE = (255,255,255)
CHESS_PIECES_BLACK = (0,0,0)

#字体STXIHEI.TTF，如果本地没有字体，可以注释字体相关代码
#window字体默认存储位置：C:\Windows\Fonts\STXIHEI.TTF
WATERMARK_CONTENT = '山狗学会'
WATERMARK_FONT = 'STXIHEI.TTF'
WATERMARK_FONT_SIZE = 15

class Wuziqi(object):
    #记录落子的位置,currentStausOfWuziqi[(x_point,y_point)] = （True, True)
    #key: 坐标；Value：是否落子，是否黑子
    currentStausOfWuziqi = {}
    def __init__(self):
        self.startGame()
        
    def startGame(self):
        #初始化pygame环境
        pygame.init()
        #画棋盘
        #游戏主窗口
        qipan_screen = pygame.display.set_mode((QIPAN_LENGHT, QIPAN_LENGHT))
        
        #用于记录是否赢棋
        result = (False, [])
        
        #持续刷新游戏画面
        while True:
            for event in pygame.event.get():
                #获取事件，如果鼠标点击右上角关闭按钮，关闭
                if event.type == locals.QUIT:
                    sys.exit()
            
            #已和局或者赢棋，不再刷新界面      
            if (len(self.currentStausOfWuziqi) >= QIPAN_TOTAL_NUM_OF_CHESS) or result[0]:
                continue                
                       
            #每次画图都要刷新棋盘，否则会留下“轨迹”
            #刷新棋盘：棋盘颜色，RGB        
            qipan_screen.fill(QIPAN_COLOR)                                  
            #新棋盘画线，18*18的棋盘，边白20px，线间隔40px；
            #起始坐标位置20px，间隔40px（18+2），总长720px
            for i in range(20,720, 40):
                #先画竖线，边框略粗
                if i == QIPAN_EDGE_LENGTH or i == QIPAN_LENGHT - QIPAN_EDGE_LENGTH:
                    #起点坐标至终点坐标，画线
                    pygame.draw.line(qipan_screen, QIPAN_LINE_COLOR, 
                                    [i, QIPAN_EDGE_LENGTH], [i,QIPAN_LENGHT - QIPAN_EDGE_LENGTH],
                                    QIPAN_BOLD_LINE_SIZE
                                    )
                #正常棋盘线
                else:
                    pygame.draw.line(qipan_screen, QIPAN_LINE_COLOR,
                                    [i, QIPAN_EDGE_LENGTH],[i, QIPAN_LENGHT - QIPAN_EDGE_LENGTH],
                                    QIPAN_NORMAL_LINE_SIZE
                                    )
                    
                #再画横线
                ##起点坐标至终点坐标，画线
                if i == QIPAN_EDGE_LENGTH or i == QIPAN_LENGHT - QIPAN_EDGE_LENGTH:
                    pygame.draw.line(qipan_screen, QIPAN_LINE_COLOR, 
                                    [QIPAN_EDGE_LENGTH, i], [QIPAN_LENGHT - QIPAN_EDGE_LENGTH, i],
                                    QIPAN_BOLD_LINE_SIZE
                                    )
                else:
                    pygame.draw.line(qipan_screen, QIPAN_NORMAL_LINE_SIZE, 
                                    [QIPAN_EDGE_LENGTH, i], [QIPAN_LENGHT - QIPAN_EDGE_LENGTH, i],
                                    QIPAN_NORMAL_LINE_SIZE
                                    )
            
            #新棋盘上加上水印
            watermar_font = pygame.font.Font('STXIHEI.TTF', WATERMARK_FONT_SIZE)
            # 字体对象.render(文字内容,True,文字颜色,背景颜色)
            text = watermar_font.render(WATERMARK_CONTENT, True, (255, 255, 255),(238, 154, 73))
            qipan_screen.blit(text, (QIPAN_LENGHT/2-40, QIPAN_LENGHT/2-40))
            
            #获取鼠标坐标信息
            x, y = pygame.mouse.get_pos()
            #获取落子的点
            x_point, y_point = self.getChessPiecesPosition(x, y)
            #画一个圆圈，参数：棋盘，颜色，位置和尺寸，半径
            pygame.draw.circle(qipan_screen, (0, 255, 0), 
                               (x_point, y_point), 
                               20,
                               QIPAN_BOLD_LINE_SIZE)
            
            #点击鼠标落子，记录落子成功
            if (pygame.mouse.get_pressed()[0]):
                if not ((x_point,y_point) in self.currentStausOfWuziqi):
                    if len(self.currentStausOfWuziqi) % 2 == 0:
                        self.currentStausOfWuziqi[(x_point,y_point)] = (True, True)
                    else:
                        self.currentStausOfWuziqi[(x_point,y_point)] = (True, False)
                        
                #避免连续点击鼠标，暂停
                time.sleep(0.2)
                
            #重新画一遍已落下的棋子
            self.drawAllChessPieces(qipan_screen)
            #检查是否赢棋
            result = self.ifWin()
            if result[0]:
                # print(result[0],result[1])
                for p in result[1]:
                    pygame.draw.circle(qipan_screen, (0, 255, 0), 
                               (p[0], p[1]), 
                               20,
                               QIPAN_BOLD_LINE_SIZE) 
                pygame.display.update()
            
            #刷新游戏界面
            pygame.display.update()
    
    def drawAllChessPieces(self, qipan_screen):        
        for coord, check  in self.currentStausOfWuziqi.items():
            if check[1]:
                pygame.draw.circle(qipan_screen, CHESS_PIECES_BLACK, (coord[0], coord[1]),QIPAN_SIZE_OF_CHESS_PIECES,0)
            else:
                pygame.draw.circle(qipan_screen, CHESS_PIECES_WHITE, (coord[0], coord[1]),QIPAN_SIZE_OF_CHESS_PIECES,0)
   
    #根据鼠标位置，获取落子位置（棋盘落子点）
    #鼠标位置肯定会落在棋盘上的一个“方格”内，将2个对边中心点相连，就将方格隔离出来四个区域
    #如果坐标落在左上角区域，那么落子点就是“方格”的左上角定点，以此类推
    def getChessPiecesPosition(self, x, y):
        #向下取整：整除"//"
        n_x = (x - QIPAN_EDGE_LENGTH) // QIPAN_GAP_OF_TWO_LINE
        n_y = (y - QIPAN_EDGE_LENGTH) // QIPAN_GAP_OF_TWO_LINE
        #取余（%）
        n_x_left = (x - QIPAN_EDGE_LENGTH) % QIPAN_GAP_OF_TWO_LINE
        n_y_left = (y - QIPAN_EDGE_LENGTH) % QIPAN_GAP_OF_TWO_LINE
        
        #左上角顶点
        if n_x_left <= QIPAN_GAP_OF_TWO_LINE/2 and n_y_left <= QIPAN_GAP_OF_TWO_LINE/2:
            x = n_x
            y = n_y
        #左下角顶点
        elif n_x_left <= QIPAN_GAP_OF_TWO_LINE/2 and n_y_left > QIPAN_GAP_OF_TWO_LINE/2:
            x = n_x
            y = n_y + 1
        #右上角顶点
        elif n_x_left > QIPAN_GAP_OF_TWO_LINE/2 and n_y_left <= QIPAN_GAP_OF_TWO_LINE/2:
            x = n_x + 1
            y = n_y
        #左下角顶点
        else:
            x = n_x + 1
            y = n_y + 1
        
        return x * QIPAN_GAP_OF_TWO_LINE + QIPAN_EDGE_LENGTH, y * QIPAN_GAP_OF_TWO_LINE + QIPAN_EDGE_LENGTH
    
    def ifWin(self):                  
        #如果尚未落子，就直接返回未赢
        if (len(self.currentStausOfWuziqi) < 1):
            return (False, [])
        
        #获取最后一个棋子的坐标，并判断最后一个棋子是否赢棋;dict转换位list，是按照元素添加顺序来确定顺序的
        coord = list(self.currentStausOfWuziqi.keys())[-1]    
        x_point = coord[0]
        y_point = coord[1]
        
        
        #如果落子坐标不在已落子坐标内，则返回
        if not ((x_point,y_point) in self.currentStausOfWuziqi):
            return (False, [])
            
        chess_color = self.currentStausOfWuziqi[(x_point,y_point )][1]
        
        #横向五子连线判断，先往右遍历，再往左遍历
        #初始化游标，用于判断是否五子连线，记录赢棋记录
        x_cursor = 0
        y_cursor = 0
        #首个棋子是当前棋子
        no_cursor = 1
        res_list = []
        #首先向右判断,纵坐标不变
        y_cursor = y_point
        for i in range (1, 6):  
            #如果已经是右边边框落子，直接终止向右
            if x_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH:
                break
            #游标移动
            x_cursor = x_point + QIPAN_GAP_OF_TWO_LINE * i
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
            
        #如果五子连线返回结果，不用进一步分析棋局
        if no_cursor >= 5:
            return (True, res_list)
            
        #然后向左判断，纵坐标保持不变
        for i in range (1, 6):  
            #如果已经是左边边框落子，直接终止向左
            if x_point == QIPAN_EDGE_LENGTH:
                break
            #游标移动
            x_cursor = x_point - QIPAN_GAP_OF_TWO_LINE * i
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
            
        #如果五子连线返回结果，不用进一步分析棋局
        if no_cursor >= 5:
            return (True, res_list)
            
        #纵向五子连线判断，先往下遍历，再往上遍历
        #初始化游标，用于判断是否五子连线
        x_cursor = 0
        y_cursor = 0
        #首个棋子是当前棋子
        no_cursor = 1
        res_list = []
        #首先向下判断,横坐标不变
        x_cursor = x_point
        for i in range (1, 6):   
            #如果已经是下边边框落子，直接终止向下
            if y_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH:
                break
            #游标移动
            y_cursor = y_point + QIPAN_GAP_OF_TWO_LINE * i
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
            
        #如果五子连线返回结果，不用进一步分析棋局
        if no_cursor >= 5:
            # print('纵向',True, res_list)
            return (True, res_list)
            
        #然后向上判断，横坐标保持不变
        for i in range (1, 6):  
            #如果已经是上边边框落子，直接终止向上
            if y_point == QIPAN_EDGE_LENGTH:
                break
            #游标移动
            y_cursor = y_point - QIPAN_GAP_OF_TWO_LINE * i
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
        #如果五子连线返回结果，不用进一步分析棋局
        if no_cursor >= 5:
            return (True, res_list)
        
        #斜下五子连线判断，先往斜下遍历，再往斜后遍历
        #初始化游标，用于判断是否五子连线
        x_cursor = 0
        y_cursor = 0
        #首个棋子是当前棋子
        no_cursor = 1
        res_list = []
        #首先斜下判断        
        for i in range (1, 6):   
            #如果已经是下边边框落子，直接终止向下
            if (x_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH) or (y_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH) :
                break
            #游标移动
            x_cursor = x_point + QIPAN_GAP_OF_TWO_LINE * i
            y_cursor = y_point + QIPAN_GAP_OF_TWO_LINE * i
            
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
            
        #然后斜后判断        
        for i in range (1, 6):   
            #如果已经是上边边框落子，直接终止向上
            if (x_point == QIPAN_EDGE_LENGTH) or (y_point == QIPAN_EDGE_LENGTH) :
                break
            #游标移动
            x_cursor = x_point - QIPAN_GAP_OF_TWO_LINE * i
            y_cursor = y_point - QIPAN_GAP_OF_TWO_LINE * i
            
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
        #如果五子连线返回结果，不用进一步分析棋局
        if no_cursor >= 5:
            return (True, res_list)       
        
        #斜上五子连线判断，先往斜上遍历，再往斜后遍历
        #初始化游标，用于判断是否五子连线
        x_cursor = 0
        y_cursor = 0
        #首个棋子是当前棋子
        no_cursor = 1
        res_list = []
        #首先斜下判断        
        for i in range (1, 6):  
            #如果已经是边框落子，直接终止
            if (x_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH) or (y_point == QIPAN_EDGE_LENGTH) :
                break
            #游标移动
            x_cursor = x_point + QIPAN_GAP_OF_TWO_LINE * i
            y_cursor = y_point - QIPAN_GAP_OF_TWO_LINE * i
            
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
            
        #然后斜后判断        
        for i in range (1, 6):   
            #如果已经是边框落子，直接终止
            if (x_point == QIPAN_EDGE_LENGTH) or (y_point == QIPAN_LENGHT - QIPAN_EDGE_LENGTH) : 
                break
            #游标移动
            x_cursor = x_point - QIPAN_GAP_OF_TWO_LINE * i
            y_cursor = y_point + QIPAN_GAP_OF_TWO_LINE * i
            
            #游标所在坐标有棋子            
            if (x_cursor,y_cursor) in self.currentStausOfWuziqi:
                #且棋子颜色与最后一个棋子颜色一致，则连续棋子数量加1
                if chess_color == self.currentStausOfWuziqi[(x_cursor,y_cursor)][1]:
                    no_cursor = no_cursor + 1
                    res_list.append((x_cursor,y_cursor))
                else:
                    break
            else:
                break
        #如果五子连线返回结果，不用进一步分析棋局
        #如果四种赢棋方式均未赢棋，则返回False
        if no_cursor >= 5:
            return (True, res_list)  
        else:
            return (False, res_list)     
     
#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    Wuziqi()
