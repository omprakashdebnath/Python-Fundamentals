if 5 > 2:
    print("Five is greater then two!")
#This is a comment.
print("hellow, world!")

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x= "awesome"

def myfunc():
   print("python is " + x)
myfunc()

x = "awesome"

def myfunc():
   x = "fantastic"
   print("python is " + x)

myfunc()

print("python is " + x)

def myfunc():
   global x
   x = "fantastic"

myfunc()

print("python is " + x)

def myfunc():
   global x
   x = "debnath"

myfunc()

print("om prakash " + x)

x = "awesome"

def myfunc():
   global x
   x = "fantastic"

myfunc()

print("python is " + x)

x = 5
print(type(x))

x = range(6)
print(type(x))
x = str("hellow world")
print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))

print("it's alright")
print("he is called 'johny'")
print('he is called "johny"')
a = """bankhai,
khathinkhin kyotsu,
kharamatsu senju"""
print(a)

a = "hellow, wprld!"
print(a[1])

for x in "banana":
   print(x)
a = "hellow, world!"
print(len(a))

a = "omp, rakash, debnath"
print(len(a))

txt = "the bessst things in life are free!"
print("free" in txt)
txt = "the best thing in life are free"
print("tree" in txt)
a = "the bessst things in life are free!"
print("free" in a)
txt = "the best thing in life are free!"
if "free" in txt:
   print("yes, 'free' is present")

a = "the best thing in life are free!"
print("expensive" not in a)
a = "the best thing in life are free!"
print("free" not in a)
a = "the best thing in life are free!"
if "expensive" not in a:
   print("no, 'expensive' is not present. ")

a = "hellow, world"
print(a[2:5])
a = "hellow, world!"
print(a[:5])
a = "hellow, world!"
print(a[2:])
b = "hellow, world!"
print(b[-5:-2])
b = "hellow, world!"
print(b[-5:-3])
x = 'welcome'
print(x[3:5])

a = " hellow, world "
print(a.strip())
a = "hellow, world!"
print(a.replace("h", "j"))
a = "hello, world!"
print(a.split(","))
for x in "banana":
   print(x)
a = "hello, world!"
print(len(a))

a = "hello"
b = "world"
c = a + b
print(c)
a = "hello"
b = "world"
c = a + " " + b
print(c)

age = 36
txt = f"my name is john, I am {age}"
print(txt)
price = 59
txt = f"the price is {price} dollars"
print(txt)
price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)
txt = f"the price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called  \"vikings\" from the north."
print(txt)
txt = "hello, world"
x = txt[0]
print(x)

print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33

if b > a:
   print("b is greater than a")
else:
   print("b is not greater then a")

a = 24
b = 37

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")

print(bool("hello"))
print(bool(15))
x = "hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
   def _len_(self):
      return 0
   
myobj = myclass()
print(bool(myobj))

def myfunction() :
   return True

print(myfunction())

def myfunction() :
   return True

if myfunction():
   print("YES!")
else:
   print("NO!")
x = 200
print(isinstance(x, int))

print(10 + 5)
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
x = 5
x += 3
print(x)

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")