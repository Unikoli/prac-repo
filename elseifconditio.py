a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))

def minimum():
    if(a<b):
        if(a<c):
            print('%d is minimum' %a)
        else:
            print('%d is minimum' %c)
    elif(b<c):
        print('%d is smallleset'%b)
    else:
        print('%d is smallest'%c)
minimum()
    
        
    
        
    