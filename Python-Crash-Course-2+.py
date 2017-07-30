
# coding: utf-8

# In[40]:


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


# In[41]:


#remove an item .pop Remove the item at the given position in the list, and return it.
first_motorcycle = motorcycles.pop(0)
print('the first motorcycle I owned was a ' + first_owned.title() + '.')


# In[62]:


#remove an item by value, The remove() method deletes only the first occurrence of the value you specify. If there’s
#a possibility the value appears more than once in the list, you’ll need to use a loop to
#determine if all occurrences of the value have been removed. 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati','suzuki']
motorcycles

motorcycles.remove('suzuki')
motorcycles


# In[61]:


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_ecpensive = 'ducati'
motorcycles

motorcycles.remove(too_ecpensive)
motorcycles

print(too_ecpensive.title() + "is too expensive for me.")

print('A '+ too_ecpensive.title() + "is too expensive for me.")


# In[85]:


#.sort method and sorted function 

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars, reverse =True))

print('\nHere is the original list again:')
print(cars)


# In[103]:


#reverse is different than sorted, method will change the objected 
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.reverse()
print(cars)

len(cars)


# In[108]:


#Python Index 
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[0])


# ### Chapter 4: Working with Lists 

# In[115]:


#for loops 

magicians = ['alice', 'david', 'carolina'] 

for name in magicians:
    print(name.title())


# In[146]:


# The colon at the end of a for statement tells Python to interpret the next line as the start of a loop. 

magicians = ['alice', 'david', 'carolina'] 

for name in magicians: 
    print(name.title() + ", that was a great trick!")
    print("I can't wait to see your ntext trick", name.title() + '\n')

#Any lines of code after the for loop that are not indented are executed once without repetition. 
print('Thank you, everyone.')


# In[147]:


message = "Hello Python world!"
print(message)


# In[170]:


# using range() function 

for value in range(1,5):
    print(value )
  
numbers = list(range(1,6))
print('\n' + str(numbers))


# In[186]:


even_numbers = list(range(2,11,2))
print (even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)
    
print('\n' + str(squares))
    


# In[206]:


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

import numpy as np

print(min(digits))
print(max(digits))
print(np.mean(digits))
print(np.std(digits))


# In[210]:


# list comprehension
square = [value**2 for value in range(1,11)]
print(square)


# In[211]:


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])


# In[214]:


players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())


# In[223]:


#copying a list 

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods
friend_food.append('carrot')
print(friend_food)
print(my_foods)


# In[227]:


#List is mutable and tuples is immutable.

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])


# In[229]:


dimensions = (200,50)

for i in dimensions:
    print (i)


# ### Chapter 5: If Statements 
# 

# In[233]:


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# In[234]:


car = 'bmw'
car == 'bmw'


# In[235]:


car = 'audi'
car == 'bmw'


# In[237]:


car = 'audi'
car == 'audi'


# In[246]:


requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print ('Hold the anchovies')


# In[248]:


requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings


# In[253]:


# if stagement 

age = 19
if age > 18:
    print("You are old enough to vote!")
    print('Have you registered to vote yep?')


# In[255]:


#if-else sttement 

age = 17

if age >=18:
    print("You are old engough to Vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too yound to vote.")
    print("Please register to vote as soon as you turn 18")


# In[262]:


# if-elif-else
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")


# In[265]:


# use if statements 

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")


# In[267]:


requested_toppings = ['mushrooms', 'extra cheese']

for toppings in requested_toppings:
    if toppings in requested_toppings:
        print("Adding mushrooms.")
    elif toppings in requested_toppings:
        print("Adding pepperoni.")
    elif toppings in requested_top:
        print("Adding extra cheese.")


# In[271]:


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + topping)

print("\nfinished")


# In[273]:


requested_toppings = []

if topping in requested_toppings:
    print("Adding" + topping )
else:
    print("Are you sure you want a plain pizza")


# In[279]:


# using multiple lists 
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for toppings in requested_toppings:
    if toppings in available_toppings:
        print("Adding " + toppings)
    else:
        print("Sorry, we don't have requested topping")
print("\nFinished making your pizza")


# ### Dictionaries

# In[293]:


alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])
print("You just earned " + str(alien_0['points']) + ' points!')


# In[313]:


#adding new key-value pairs 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['points'] =6
print(alien_0)

del alien_0['points']
print(alien_0)


# In[319]:


favorite_languages = {
    'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

print(favorite_languages['sarah'].title())


# In[336]:


user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
print (user_0.items())


for k, v in user_0.items():
    print("\nKey: " + k)
    print("value: " + v)

for name in user_0:
    print('\n' + name)


# In[344]:


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())


# In[356]:


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil','sarah']
for name in favorite_languages:
    print(name.title())
    
    if name in friends:
        print("Hi ",name.title()  +", I see your favorite language is " + favorite_languages[name] +'!')


# In[355]:


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take ou poll")


# In[359]:


#Looping Through a Dictionary’s Keys in Order
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", than you for taking the poll.")



# In[360]:


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# In[364]:


#To see each language chosen without repetition, we can use a set. 
#python without repetition

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 'yuan': 'python'
 }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# ##### Nesting
# 

# In[374]:


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for a in aliens:
    print(a)


# In[384]:


# create a alien 

aliens = []

for alien_number in range(30):
    new_alien =  {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print("Total number of aliens: " + str(len(aliens)))


# In[391]:


#update the information in dictionary by using for loops 

aliens = []

for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
for alien in aliens[0:5]:
    print(alien)
print("...")


# In[399]:


pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
   
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza['toppings']:
   print('\t' + topping)


# In[417]:


# A list in a Dictionary 

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }


for name in favorite_languages.keys():
    print('\n' + name.title() + "'s favorite languages are:")
    
    for language in favorite_languages[name]:
        print('\t' + language.title())


# In[446]:


# A dictionary in a dictionary
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

users['aeinstein']['first']

for username in users.keys():
    print("\nUsername: " + username)
    print('Full name: ' + users[username]['first'].title() + ' ' + users[username]['last'].title())
    print('Location' + ' ' + users[username]['location'].title() )
    
 


# In[454]:


users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



# ### Chapter 7: User input and while loops 

# ###### input function
# 

# In[456]:


# The input() function pauses your program and waits for the user to enter some text

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# In[ ]:


name = input("Pleas enter your name: ")

print("Hello, " + name)


# In[ ]:


prompt =  "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your first name"

name = input(prompt)

print("\nHello" + name )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




