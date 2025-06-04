def hello():
    print("Hello")


# even functions are objects
message = hello

# call new function
message()


def hello(func):
    def inner():
        print("Hello ")
        func()

    return inner


def name():
    print("Alice")


obj = hello(name)
obj()


def who():
    print("Alice")


def display(func):
    def inner():
        print("The current user is : ", end="")
        func()

    return inner


if __name__ == "__main__":
    myobj = display(who)
    myobj()


@hello
def name():
    print("Alice")


if __name__ == "__main__":
    name()


def sumab(a, b):
    summed = a + b
    print(summed)


def preety_sumab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is ", end=" ")
        return func(a, b)

    return inner


@preety_sumab
def sum(a, b):
    summed = a + b
    print(summed)


if __name__ == "__main__":
    sumab(5, 3)

import time  # noqa: E402


def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("function took " + str(time.time() - t) + " second to run")
        return res

    return wrapper


@measure_time
def myfunction(n):
    time.sleep(n)


if __name__ == "__main__":
    myfunction(2)
