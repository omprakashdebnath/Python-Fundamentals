def add(a, b):
    result = a + b
    return result


print(add(5, 3))

# import standard math module
import math  # noqa: E402

# use math.pi to get value of pi
print("The value of pi is", math.pi)

import math as m  # noqa: E402

print(m.pi)
from math import pi  # noqa: E402

print(pi)

from math import *  # noqa: E402, F403

print("the value of pi is", pi)

a = 1
b = "hello"

import math  # noqa: E402

print(dir())
["__builtins__", "__doc__", "__name__", "a", "b", "math", "pyscripter"]
