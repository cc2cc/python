#print [x*x for x in range(1,11) if x%2==0]
#print [m+n for m in 'ABCD' for n in '123']

#import os
#print [d for d in os.listdir('.')]

'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        print '------a=%d------' % (a)
        #a,b=b,a+b //
        x=a+b
        a=b
        b=x 
        
        n=n+1 
fib(6)
'''


'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b 
        n=n+1 
#fib(6)

for n in fib(6):
    print n
'''
'''
def add(x, y, f):
    return f(x) + f(y)
print add (-1,1,abs)

def add(x, y):
    return abs(x) + abs(y)
print add (-1,1)
'''
'''
def my(str):
    a=str[0].upper()
    b=str[1:].lower()
    return a+b
print map(my,['adam', 'LISA', 'barT'])

def prod(x,y):
    return x*y
print reduce(prod,[1,2,3,4,5])
'''

'''
def char2num(s):
        dic={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        s=dic[s]
        return s
a='123456'
print map(char2num,a)
'''

'''    
def not_prime(x):
    b=int(x**0.5)
    
    if x in (0,1):
        return False
        
    for i in range(2,b+1):
        if x % i == 0:
            return False
    return  True
            
print filter(not_prime, range(0,100))
'''



    

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
