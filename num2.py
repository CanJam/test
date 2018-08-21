#-*- coding:UTF-8 -*- 

year = int(input('请输入一个年份：'))
"""
if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print('{0}是润年'.format(year))
        else:
            print('{0}不是润年'.format(year))
    else:
        print('{0}是润年'.format(year))
else:
    print('{0}不是润年'.format(year))        

"""
if(year%4)==0 and (year%100)!=0 or (year%400)==0:
    print('{0}是润年'.format(year))
else:
    print('{0}不是润年'.format(year))    
