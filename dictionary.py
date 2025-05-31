thisdict = {"brand": "ford", "model": "mustang", "year": 1964}
print(thisdict)

thisdict = {"brand": "ford", "model": "mustang", "year": 1964}
print(thisdict["brand"])

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "Year": 2020}
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

car = {"brand": "ford", "model": "mustang", "year": 1964}

x = car.keys()
print(x)  # before the change

car["colour"] = "white"

print(x)  # afetr the changes

car = {"brand": "ford", "model": "mustang", "year": 1964}

x = car.values()
print(x)  # before the change

car["year"] = 2020
print(x)  # after the change

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018

print("thisdict")

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})

x = {"type": "fruit", "name": "apple"}
for y, z in x.items():
    print(y, z)

    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)
