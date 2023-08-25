x='hellomother fuckerhowareyou'
print('h' in x)
print('mother' in x)
print('fuc' in x)
print(' ' in x)

print('mother' not in x)
print('r' not in x)
print(' ' not in x)

list=[10,40 , 30,56,89 ]
print(1500 in list)
print(40.5 in list)
print(10  not in list)

print('------------------')

x=56
y=45
p='hey'
q='fuck you'
print(x is y)
print(x  is not y)
print(p is q)

print('----------------------orecedence and associativity')
x=6
y=4
z=9
print(x+y-z*x)
print(x+(y-z)*x)

print('---------------------- average collection of collection integers')
data=[1,2,3]
sum_of=sum(data)
count=len(data)
average=sum_of/count
print(average)

print('------------------product of collection of real numbers')
data=[1,2,3]
pro=1
y=len(data)
for i in data:
    pro=pro*i
print('product is--->',pro)





