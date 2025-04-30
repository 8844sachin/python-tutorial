#This is legal variable
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''Illegal variable name
2myvar = "John"
my-var = "John"
my var = "John"
'''

#Multiple value assign with multiple variable
x,y,z="morning","afternoon","evening"
print(x)
print(y)
print(z)

#Single value assign to multiple variable
a=b=c=10
print(c)
print(a)
print(a+c)

#unpack a collection
hello=["Mon","Tue","Wed"]
x,y,z=hello
print(y)
