#-*- coding:UTF-8 -*-

a,b,c,d = 2014,201.4,True,4+3j
print(type(a),type(b),type(c),type(d))

a = 111
print (isinstance(a,int))

class A:
    pass

class B(A):
    pass

print (isinstance(A(),A)) #type()不会认为子类是一种父类类型。
print(type(A()) == A)     #isinstance()会认为子类是一种父类类型。
print(isinstance(B(),A))
print(type(B()) == A)

x = "python"
print (x[0],'t')

list = ['abc','12356','2.23','leanding',101.0]
tlist = ['can',123,'jam']
print(list)
print(list[4:])
print(list[1:3])
print(list + tlist)
print(tlist * 2)

nlist = ['12','22',1,121212,'adasd']
a=nlist[1:2] = ['jam','can']
print(a)
print(nlist)
a[0:1] = []
print (a)
print (nlist)

name = {'can','jam','lucy','gugii','can','lenging'}
name2 = set('')
print (name)
print (name2)
if 'dam' in name :
    print('dam in')
else:
    print('dam not in')

set1 = set('abracadabra')
set2 = set('alacazam')
print(set1)
print(set1 & set2)
print(set1 - set2)
print(set1 | set2)
print(set1 ^ set2)        

dict = {}
dict['one'] = "diyi"
dict[1] = 'dier'
print (dict['one'])
print (dict[1])
dict2 = {'1111':'xnxnx','252525':'7878'}
print (dict2)
print (dict2.keys())
print (dict2.values())

a = 21
b = 10
c = 0

c = a+b
print (c)

c +=a
print (c)

c -=a
print (c)

c *=a
print (c)

c /=a 
print (c)

c = 2

c %= a
print (c)

c **= a
print (c)

c //= a
print (c)

    
a = 10
b = 10
c = '12121'
d = '12'

if (a and b):
    print (1)
else:
    print (-1)

if (a or b ):
    print (1)
else:
    print (-2)

if not (a and b):
    print (2)
else:    
    print (-3)            

if c not in d:
    print ('ture') 
else:
    print ('false')       

if d not in c:
    print ('ture') 
else:
    print ('false')        

if a  is   b :
    print ('not')
else:
    print ('y')    


