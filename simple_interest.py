x=int(input('enter the principle'))
y=int(input('enter the rate'))
z=int(input('enter the time'))

def simple_interest():
    SI=(x*y*z)/100
    return (SI)
print('the simple interest is', simple_interest())