#-*- coding:UTF-8 -*-
while True:
    try:
        num = float(input('请输入一个数：'))

        if num > 0:
            print('{}为正数'.format(num))

        elif num < 0:
            print('{}为负数'.format(num))
        else:
            print('{}为0'.format(num)) 
        break
    except ValueError:
        print('输入无效，请重新输入数字')           