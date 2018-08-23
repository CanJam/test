#-*- coding:UTF-8 -*-
"""
def add(x,y):
    return x + y

def jian(x, y):

   return x - y

def chen(x, y):
   
   return x * y

def chu(x, y):
   
   return x / y    

print("选择运算：","1、相加","2、相减","3、相乘","4、相除")

choice = int(input('请选择：'))
num1 = int(input('输入第一个数：'))
num2 = int(input('输入第二个数：'))

if choice == 1:
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == 2:
    print(num1,'-',num2,'=',jian(num1,num2))    
elif choice == 3:
    print(num1,'x',num2,'=',chen(num1,num2))
elif choice == 4:
    print(num1,'/',num2,'=',chu(num1,num2))  
else:
    print('非法输入')
"""

class oper:
    oper=""
    func=""
    def __init__(self,oper):
        self.oper=oper.strip()

    def opers(self,num1,num2):
        swicher={
            '+':'jia',
            '-':'jian',
            '*':'cheng',
            '/':'chu',
        }
        func=swicher.get(self.oper,'default')
        if func == 'default':
            print('运算符错误')
            exit()
        num1=float(num1)
        num2=float(num2)
        func=getattr(self,func)
        return func(num1,num2)

    def jia(self,num1,num2):
        return num1 + num2

    def jian(self,num1,num2):
        return num1 - num2

    def cheng(self,num1,num2):
        return num1 * num2

    def chu(self,num1,num2):
        return num1 / num2


import re

print("例如：2+2，自动计算结果")
nums=input("请输入：")
numsObj=re.search(r'(\d+)(.*?)(\d+)',nums,re.M)
if numsObj:
    num1=numsObj.group(1)
    fuhao=numsObj.group(2)
    num2=numsObj.group(3)
    operObj=oper(fuhao)
    res=operObj.opers(num1,num2)
    print('运算结果{}'.format(res))
else:
    print("输入错误，{}".format(nums))
"""

def divide(x,y):
    #相除
    if y ==0:
        print('0不能做为分母')
        return
    else:
        return x/y

choice =int(input("请选择运算:\n1,相加\n2,相减\n3,相乘\n4,相除\n请输入运算(1/2/3/4):"))
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
if choice ==1:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif choice ==2:
    print("{}-{}={}".format(num1,num2,num1-num2))
elif choice ==3:
    print("{}x{}={}".format(num1,num2,num1*num2))
elif choice ==4:
    print("{}/{}={}".format(num1,num2,divide(num1,num2)))
else:
    print("选择的运算为非法输入")    

"""    