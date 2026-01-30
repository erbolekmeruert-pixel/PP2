#1
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()
print("Python is " + x)
#2
def myfunc(): 
    global x
    x = "keremet"
myfunc()
print("Python is " + x)

#3
x = "top"
def myfunc():
    global x
    x = "dragon"
myfunc()
print("python is " + x)
