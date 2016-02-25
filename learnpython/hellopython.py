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
quote = "\"Always remember you are unique"  ###escape character
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
print("to_do_list",to_do_list)
print("to_do_list[1][1]",(to_do_list[1][1]))

to_do_list.append("Onions")
print("Onions appended",to_do_list)

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
print("\n")


### Generate random numbers and while loop
random_num = random.randrange(0,100)

while(random_num != 15) :
    print(random_num, " ", end="")
    random_num = random.randrange(0,100)
print("\n")

i=0
while (i <= 20) :
    if(i%2 == 0) :
        print(i, " ", end="")
    elif(i==9) :
        break
    else :
        i += 1
        continue
    i += 1
print("\n")


###Functions, command line input, string operations
def addNumber(fNum,lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(2,6), "\n")

print("What is your name?")
name = sys.stdin.readline()
print("Hello", name)

long_string = "I'll catch you if you fall - The Floor. do not worry."

print ("First 4 characters = ",long_string[0:4])
print ("Last 5 characters = ",long_string[-5:])
print ("All characters until last 5 characters = ",long_string[:-5])
print ("Concatenate string with first 4 characters = ", long_string[:4] + " be there")
print ("%c is my %s and my number %d number is %.4f" % ("A","favorite letter",1,0.17))

###Capitalize only first letter of string
print (long_string.capitalize())
print (long_string.find("Floor")) #case sensitive

print(long_string.isalpha()) #check if all alphabets
print(long_string.isalnum()) #check if all numbers
print(long_string.replace("Floor", "Ground"))
print(long_string.strip()) #####################################have to check on this
split_list=long_string.split(" ")
print(split_list)



###File IO operations
test_file = open("test.txt", "wb")
print(test_file.mode)  ###mode in which file is opening
print(test_file.name)  ###file name
test_file.write(bytes("Write me to the file\n", "UTF-8"))
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)


###Class, Constructor, Inheritance, Overriding functions, Method overloading, Polymorphism
class Animal :
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self,name):
        set.__name = name

    def get_name(self):
        return self.__name

    def set_height(self,height):
        set.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self,weight):
        set.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self,sound):
        set.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        ###super(Dog,self).__init__(name, height, weight, sound)   didn't work have to further analyze
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_owner(self,owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} His owner is {}".format(self.__name,
                                                                                      self.__height,
                                                                                      self.__weight,
                                                                                      self.__sound,
                                                                                      self.__owner)

    def multiple_sounds(self,how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Alok")

print(spot.toString())

class AnimalTesting:
    def get_type(self,animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)


spot.multiple_sounds(4) ###not working needs to be investigated
spot.multiple_sounds()