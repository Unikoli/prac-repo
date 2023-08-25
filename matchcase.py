x,y=map(int,input('enter numbers::').split())

option=input('enter the operator')

while(True):
    option=input('enter the operator')
    match option:
        case '+':
            print('sum=',x+y)
        
        case '-':
            print('difference=',x-y)
        
        case '*':
            print('product=',x*y)
            
        case '/':
            print('division=',x/y)
            
        case '**':
            print('power=',x**y)
            
        case '//':
            print('floatin value=',x//y)
            
        case _:
            print('enter the correct oprator')
        