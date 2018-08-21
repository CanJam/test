#-*- coding:UTF-8-*-


#使用“\”连接语句块
total = "sdjiejijiejie1" + \
        'djiejeije2' + \
        'djiejieieie'        
print (total)     
#在{}（）[]中不需要加 \
t1 = ['nvnvnv1','jvnvnnv2',
    'jcnjedeiorkj3']
print (t1)
#r消除\的转义
print (r"this is a line with not change \n" )
#*可以让字符串重复
print ("it will be repeat:  "*2)

#!/usr/bin/python3
str='learning python'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + "学习")
print('-'*30)
print('linijiji\njiji')
print(r'linijiji\njiji')
print('-'*30)
 
str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

input('\n\n按下回车键退出')

import sys; x = 'learning'; sys.stdout.write(x + '\n')

x = 'a' 
y = 'b'
print(x,end="") #不换行符号
print(y) 

import sys
from sys import argv,path 
print('==========Python import moder ================')
print('命令行为参数为：')
for i in sys.argv:
    print (i)
print('python的路径为',path)    


