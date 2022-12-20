print("hello world")
if 5 > 2:
    print("five is greater than two")

x = 5
y = "hello world"
print(x)

# comments like this will be ignored in code 

x = 5
y = "john"
print(type(x))
print(type(y))

a = 4
A = "sally"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print(x, y, z)
print(x + y + z)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)