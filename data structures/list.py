x = [] #creat dicionary
x.append(9) #add item to end of list
x.append(7)


x.insert(0,5) #adds an item to the first position, where first parameter indicates whitch positon the segund parameter


# x.remove() #remove the pamater indicates 

 
# x.pop() #remove the parameter indicated or paramter placed 


# x.clear() #remove all items from list

x.count(1) #return the number of times

x.sort() # sort the list in ascending order


x.reverse()



##The list comprehesions

squere = []
for x in range(10):
    squere.append(x**2)
print(squere)

## the list comprehesions they are forms to write sequence to forms summarized

#Dicionary

knights = {'Gallahad': 'The pure', 'robin': 'The brave'}

for k, v in knights.items():
    print(k,v) 

#function zip, unity two or plus dicionary or tupla


question = ['Nome', 'quest', 'favorite color']
answers = ['lancelot', 'the  holy grail', 'blue']
for q, a in zip(question, answers):
    print(f'What is yout {q} it is {v}')
print()
