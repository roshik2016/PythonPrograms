fruit = 'mango'
print(fruit[1:4]) # prints between the range
print(fruit[:4]) # prints from the start 
print(fruit[1:]) # prints till the last value
print(fruit[1:1]) # does not give any character

new_fruit = "apple " + fruit[0:]
print(new_fruit)
print(len(new_fruit))