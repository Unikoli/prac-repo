list_item=[30,23,45,38,4.6,'unique']
print(list_item,'is a type of',type(list_item))
list_item[1]=213
print(list_item)
print(list_item[1])
print(list_item[-1])
print(list_item[0])
print(38 in list_item)
for i in list_item:
    print(i)
list_item=(30,23,45,38,4.6,'unique')    
print(list_item,'is a type of',type(list_item))
print('indexing eg',list_item[0],list_item[-1])
print('slicing eg',list_item[0:4])
print('membership eg','unqiue' in list_item)
for data in list_item:
    print(data)