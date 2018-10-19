# -*- coding: utf-8 -*-


def fib(n):
    x=0
    y=1
    for i in range(n-1):
        y=x+y
        x=y
        
    return y
            

print(fib(2018)) 