#-*- coding:UTF-8 -*-

a = input('请输入变量a：')
b = input('请输入变量b：')

a,b = b,a
print('交换后a的值为：{}'.format(a))
print('交换后b的值为：{}'.format(b))
