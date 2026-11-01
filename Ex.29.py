# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1          # This x is Local to func1()
    print(x)
func1()

def func2():
    x = 2          # While this x is Local to func2()
    print(x)
func2()

def func3():
    x = 3          # Example of Enclosed scope
    def func4():
        print(x)
    func4()
func3()

y = 4              # Example of Global scope
def func5():
    print(y)
def func6():
    print(y)
func5()
func6()

from math import e  # Example of Built-in scope
def func7():
    print(e)
func7()

from math import pi # This Built-in scope gets dominated by Global scope
def func8():
    print(pi)
pi = 3              # According to the order of (LEGB), it will use
func8()             # the Global scope first!
