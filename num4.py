#-*- coding:UTF-8 -*-

lower = int(input('请输入范围内的第一个数：'))
upper = int(input('请输入范围内的最后一个数：'))

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
             print(num)                            
       