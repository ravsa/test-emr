import os
print('----------------ENV---------------------')
print(os.environ)
print('----------------------------------------')
import a
from a import ex2
from a.b import ex1
from a.b.c.ex3 import ex3
print(a.ex2.ex2())
print(ex2.ex2())
print(a.b.ex1.ex1())
print(ex1.ex1())
print(ex3())
