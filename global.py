#global variable not used
x="fantastic"
def my():
    x="Awesome"
    print("Python is " + x)
my()
print("Python is "+ x)


#Global variable is used
y="nice"
def mypy():
    global y
    y="Excellent"
    print("python is "+ y)
mypy()
print("Python is " + y)