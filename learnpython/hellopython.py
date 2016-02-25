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