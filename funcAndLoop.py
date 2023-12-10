#if...elif...else模式演示
#根据房子的价格，给出房子的等级

#定义用于判定等级的房子价格，单位：万
priceOfApart = 900

if priceOfApart >= 1000:
    print('房子价值千万及以上，已进入奢侈房产等级！')
elif priceOfApart >= 500 and priceOfApart < 1000:
    print('房子价值500万与千万之间，已进入轻奢房产等级！')
else:
    print('房子价值500万一下，已进入普通房产等级！')
    
# for...in循环演示，依次把list或tuple中的每个元素迭代出来
# 模拟计算问界单小时销售额，单位万
priceOfAITOList = [25,38,25,38,26,29,32,33,20]
sumRevenue = 0
for unitPrice in priceOfAITOList:
    sumRevenue = sumRevenue + unitPrice
print('问界单小时销售额求和结果是： ',  sumRevenue)
    

#while循环演示，条件不满足或者遇到break语句时退出循环
#模拟计算制造mate 60 pro的累计时长，单位：小时

#使用条件退出循环
timeofMakingOne = 6
noOfMate60pro = 1000
sumDuration = 0
while noOfMate60pro > 0:
    sumDuration = sumDuration + 6
    noOfMate60pro = noOfMate60pro - 1
print('制造1000台mate 60 pro的累计时长是: ', sumDuration)    

#使用break退出循环
timeofMakingOne = 6
noOfMate60pro = 0
sumDuration = 0
while True:
    sumDuration = sumDuration + 6
    noOfMate60pro = noOfMate60pro + 1
    if noOfMate60pro == 500:
        break
print('制造', noOfMate60pro, '台mate 60 pro的累计时长是: ', sumDuration)  

#自定义函数，def ... :模式
#模拟根据上班通勤天数，求出汽车充电金额,假设默认每公里花费5元
def calcCostByWorkingDyays(distance, workingDays, perKMCost = 5):
    #上下班通勤，所以上一天班的公里数是举例的两倍，再乘以天数得出总公里数
    totalKM = distance * 2 * workingDays
    #根据单价算出总费用
    totalCost = totalKM * perKMCost
    #返回总费用
    return totalCost

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #山狗办公室通勤距离20公里，一月上班22天
    distance = 20
    workingDays = 22
    #使用默认单价，计算出通勤总计费用
    totalCost = calcCostByWorkingDyays(distance,workingDays)
    
    print('山狗办公通勤距离', distance,'公里，预计每月通勤费用为',totalCost,'元。')
 
