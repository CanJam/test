#-*- coding:UTF-8 -*-
"""
num = int(input('请输入您需要几项:'))

n1 = 0
n2 = 1
count = 2

if num <= 0:
    print('请输入一个正数')
elif num == 1:
    print('斐波那契数列：')
    print(n1)
else:
    print('斐波那契数列：')
    print(n1,',',n2,end=',')
    while count < num:
        nth = n1 + n2
        print(nth,end=',')
        n1 = n2
        n2 = nth
        count += 1

"""

num = int(input('shuru xiang'))

a = 0
b = 1

if num <= 0:
    print('shuru zheng')
elif num == 1:
    print('shuliewei:')
    print(a)
else:
    print('shuleiwei:')
    print(a,',',b,end = ',')
    for n in range(1,num-1):
        ns = a + b
        a,b = b,ns
        print(ns,end=',')






