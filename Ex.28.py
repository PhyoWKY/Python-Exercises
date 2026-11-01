# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))

# print(help("math"))

import math as m
print(m.pi)

from math import pi
print(pi)

print()

import math
a, b, c, d, e = 1, 2, 3, 4, 5
print(math.e ** a) # import math as m or import math
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

print()

import module_eg # Our own module

result = module_eg.pi
print(result)

result = module_eg.square(3)
print(result)

result = module_eg.cube(3)
print(result)

result = module_eg.circumference_of_circle(3)
print(result)

result = module_eg.area_of_circle(3)
print(result)