#-*- coding:UTF-8 -*-
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end=' ')
    print()
"""

print('\n'.join(' '.join('%dx%d=%-2d'%(x,y,x*y)for x in range(1,y+1))for y in range(1,10)))