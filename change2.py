#-*- coding:UTF-8 -*-
#Python 十进制转二进制、八进制、十六进制
dec = int(input('输入数字：'))

print('十进制数为：',dec)
print('转换为二进制：',bin(dec))
print('转换为八进制：',oct(dec))
print('转换为十六进制：',hex(dec))

c = input('请输入一个字符：')

a = int(input('请输入一个ASCII码：'))
print(c + '的ASCII码为',ord(c))
print(a,'对应的字符为',chr(a))
