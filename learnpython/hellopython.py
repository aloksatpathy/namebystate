import random
import sys
import os

print ("Hello World")

#Comment

'''
Multiline
comments
'''

'''
datatypes : Numbers Strings Lists Tuples Dictionaries
7 algorithmic operators:
+ - * /
% - remainder of a division
** - exponential operator
// - perform division and discard remainder
'''

###Arithmetic operations
print("5 + 2 = ",5+2)
print("5 - 2 = ",5-2)
print("5 * 2 = ",5*2)
print("5 / 2 = ",5/2)
print("5 % 2 = ",5%2)
print("5 ** 2 = ",5**2)
print("5 // 2 = ",5//2)


###String operations
quote = "\"Always remember you are unique"
multi_line_quote = ''' just
like everyone else\"'''

new_string = quote + multi_line_quote

print("%s %s %s" % ("I like the quote", quote, multi_line_quote))

print ("\n"*5)

print("I don't like ", end="")
print("newlines")


###List operations
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas', 'Apples']
print('First item', grocery_list[0])

grocery_list[0]="Orange Juice"
print('First item', grocery_list[0])
print(grocery_list[1:3])

other_events = ['Wash Car', 'Cash Check', 'Have breakfast']

to_do_list = [grocery_list, other_events]
print(to_do_list)
print((to_do_list[1][1]))

to_do_list.append("Onions")
print(to_do_list)

grocery_list.insert(3,"Strawberries")
print(to_do_list)

to_do_list.remove("Onions")
print("removed Onions",to_do_list)

grocery_list.sort()
print("sorted",grocery_list)

grocery_list.reverse()
print("reverse sorted",grocery_list)

del grocery_list[4]
print(grocery_list)

to_do_list2=grocery_list+other_events
print(to_do_list2)

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))



###tuples
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print(len(new_tuple),max(new_tuple),min(new_tuple),len(pi_tuple))



###dictionaries
super_villains = {"Fiddler": "Isaac Bowin",
                  "Captain Cold": "Leonard Snart",
                  "Weather Wizard": "Mark Mardon",
                  "Mirror Master": "Sam Scudder",
                  "Pied Piper": "Thomas Peterson"}
print("Captain Cold =",super_villains["Captain Cold"])

del super_villains["Fiddler"]
super_villains["Pied Piper"]="Hartley Rathaway"
print(len(super_villains))
print(super_villains.get("Pied Piper"))

print(super_villains.keys())
print(super_villains.values())




###Conditionals, logical operators and loops
### if else elif == != > >= <=

age = 31

if age > 18 :
    print("You are old enough to drive")
else :
    print("You are not old enough to drive")

if age>=21 :
    print("You are old enough to drive a tractor trailer")
elif  age>=18 :
    print("You are old enough to drive a car")
else :
    print("You are not old enough")

### logical operators and or not
if((age>=1) and (age<=18)) :
    print("You get a birthday")
elif(age==21)or(age>=65) :
    print("You get a birthday 2")
elif not(age == 30) :
    print("You don't get a birthday")
else :
    print("You get a birthday party yeah")

###loops
for x in range(0,10) :
    print(x, " ", end="")
print("\n")

for y in grocery_list :
    print(y, " ", end="")
print("\n")
for x in [2,4,6,8,10] :
    print(x, " ", end="")
print("\n")

num_list = [[0,1,2],[2,3,4],[3,4,5]]

for x in range(0,3) :
    for y in range(0,3) :
        print(num_list[x][y], " ", end="")