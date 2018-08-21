#-*- coding:UTF-8 -*-

import cmath


num = float(input('请输入一个数字：'))

num_sqrt = num ** 0.5
print('%0.3f 的平方跟是%0.3f'%(num,num_sqrt))   

num = int(input('请输入一个数字：'))

num_sqrt = cmath.sqrt(num)
print('{0}的平方跟是{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))


#解二元方程式ax**2 + bx + c = 0
a = float(input('请输入a：'))
b = float(input('请输入b：'))
c = float(input('请输入c：'))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('输出的结果为：{0}和{1}'.format(sol1,sol2))