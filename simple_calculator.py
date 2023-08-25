x=int(input('enter first number'))
y=int(input('enter second number'))

choice=input('enter which operation you want to perform:::')


def calculation():
    if(choice=='+'):
         print("sum=",x+y)
    elif(choice=='-'):
         print('difference::',x-y)
    elif(choice=='*'):
          print('product::',x*y)
    elif(choice=='-'):
          print('division::',x/y)
    elif(choice==''):
          print('mooduculoeuhe::',x%y)
    elif(choice=='-'):
          print('difference::',x-y)
    elif(choice=='-'):
          print('florr divison::',x-y)
    else:
        print('doesnot match wtih the operator')
calculation()
         
                
                
            
        