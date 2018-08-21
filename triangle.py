#-*-coding:UTF-8-*-

a = float(input('请输入三角形的第一条边长：'))
b = float(input('请输入三角形的第二条边长：'))
c = float(input('请输入三角形的第三条边长：'))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('三角形面积为%0.2f'%area)