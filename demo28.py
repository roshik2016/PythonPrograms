list2 = ['a','b','c']
rm_list = list2.pop(1) # specify the index of the char to be removed
print (list2)
print ("element removed is", rm_list)

# using remove method to remove a particular value
list2.remove('a')
print(list2)

# using del mothod to remove more than one element at a time
list3 = ['u','v','y','z']
del list3[1:3] 
print (list3)