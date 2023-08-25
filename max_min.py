data=[10,20,30,40,50,69,45,67]

x=data.sort()

print('the smallest number is::', data[0])
print('the largest numebr is::',data[-1])
print(max(data))
print(min(data))
   

sum=0
for i in range(9):
    sum+=data[i]

print('the sum of the elements is',sum)