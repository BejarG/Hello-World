'''
Put here all the definitions fir specific formulas
'''
import math

def fibon_sequence(n):
    x = 1
    y = 1
    count = 1
    while count <= n:
        print('A new fibonacci number ',x + y)
        temp = x
        x = y
        y = y + temp
        count = count + 1



def swap(a,b):
    temp = a
    a = b
    b = temp
    return print(a,b)

def distance2d(x1,y1,x2,y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d


def distance3d(x1,y1,z1,x2,y2,z2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return d







