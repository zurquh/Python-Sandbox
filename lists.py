# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Use a construcutor 
# numbers2 = ((1, 2, 3, 4, 5))

# print(numbers, numbers2)
print(fruits[1])

#Get length 
print(len(fruits))

#Append to lisr 
fruits.append('Mangos')

#Remove from list
fruits.remove('Grapes')

#Insert into position 
fruits.insert(2, 'Strawberries')

#change value 
fruits[0]= 'Blueberries'

#Remove with pop
fruits.pop(2)

#Reverse list 
fruits.reverse()

#Sort List
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

print(fruits)

