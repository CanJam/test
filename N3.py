#-*- coding:UTF-8 -*-
"""
a,b = 0,1

while b<1000:
    print(b,end=',')
    a,b = b ,a+b


age = int(input("请输入狗狗的岁数："))
print("")
if age <= 0:
    print('???')
elif age == 1:
    print('相当于人的14岁')
elif age == 2:
    print('相当于人的22岁')
elif age > 2:
    human = 22 + (age - 2)*5
    print('对应人类的岁数：',human)



num = 7
guess = 0
print('这个是猜字游戏')
while num != guess:
    guess = int(input('请再输入：'))
    if guess == num:
        print('right')
    elif guess > num:
        print('大了')   
    elif guess < num:
        print('小了')        
      

num = int(input('请输入一个数字：'))

if num%2 == 0:
    if num%3 == 0:
        print('您输入可以整除2和3的数')
    else:
        print('您输入的数可以整除2,不可以整除3')
else:
    if num%3 ==0:
        print('您输入的数可以整除3,不可以整除2')
    else:
        print('您输入的数不可以整除2和3')                


        

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print('1到%d的总和：%d' %(n,sum))

var = 1
while var == 1:
    num = int(input('输入一个数字：'))
    print ('你输入的数字是：',num)
print ('Good,bye!')       

count = 0
while count < 5:
    print(count,'小于5')
    count += 1
else:
    print(count,'大于或等于5')    


flag = 1
while (flag): print('欢迎欢迎')
print('goodbye')    

l = ['c','c++','java','ptyhon']

for x in l:
    print(x)


sites = ['baidu','google','taobao','jindong']
for site in sites:

    if site == 'taobao':
        print('淘宝')
        break
    print('循环数据'+site)
else:
    print('没有循环数据')
print('完成循环')     


for letter in 'fuck':
    if letter == 'k':
        break
    print('当前的字母是：',letter)

var = 10
while var > 0:
    print('当前变量值为：',var)
    var -= 1
    if var ==5:
        break
print('goodbye')           


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'等于',x,'*',n//x)
            break
    else:
        print(n,'是质数')        
  

for letter in 'runoob':
    if letter == 'o':
        pass
        print('正在执行pass块')
    print('当字母：',letter)
print('goodbye')        


list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=',')


import sys

list=[1,2,3,4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


import sys

def fiboacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a     
        a,b = b, a+b
        counter += 1

f = fiboacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()   



def area(width,height):
    return width * height

def print_welcome(name):
    print('welcome',name)
print_welcome('fuck')
w = 4
h = 5
print('width = ',w,'height=',h,'area=',area(w,h))

def printme(str):
    print(str)
    return
printme('我要调用用户自定义函数')
printme('再次调用同一函数')    

def changeInt(a):
    a =10

b = 2
changeInt(b)
print(b)    


def changeme(mylist):
    mylist.append([1,2,3,4])
    print('函数内取值：',mylist)
    return

mylist = [10,20,30]    
changeme(mylist)
print('函数外取值: ',mylist)

def printme(str):
    print(str)
    return

printme(str = '练手')    


def printinfo(name,age = 24):
    print('名字：',name)
    print('年龄：',age)
    return

printinfo(age = 50 , name = 'canjam')
print('x'*50)
printinfo(name = 'zheng')

def printinfo(arg1,*vartuple): #参数会以元组(tuple)的形式导入,收集参数
    print('输出：')
    print(arg1)
    print(vartuple)
printinfo(50,55,10)    


def printinfo(arg1,*vartuple):
    print('输出: ')
    print(arg1)
    for var in vartuple:
        print(var)
    return 
printinfo(10)
printinfo(70,50,80)

def printinfo(arg1,**vardict):
    print('输出：')
    print(arg1)
    print(vardict)

printinfo(1, a = 2, b = 3)

def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3))


sum = lambda arg1,arg2: arg1 + arg2
print(sum(10,20))

total = 0
def sum(arg1,arg2):
    total = arg1 + arg2
    print('函数内：',total)
    return total

sum(10,20)
print('函数外',total)    

#  L –> E –> G –>B 的规则查找
x = int(2.9) #内建作用域

g_count = 0 #全局作用域
def outer():
    o_count = 1 #闭包作用域
    def inner():
        i_count = 2 #局部作用域


num = 1
def fun1():
    global num # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)    


def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()        



a = 10
def test(a):
    a = a + 1
    print(a)
test(a)

a = 1
b = 2

a,b = b,a
print(a,b)
"""















