print("It's alright")
print("He is called 'Calvin'")
print('He is called "Harris"')

a = """ How deep is your love?
Is it like the ocean?
What devotion? Are you?
How deep is your love?
Is it like nirvana?
Hit me harder, again
How deep is your love?
"""
print(a)

#arrays
a = "Hello, World!"
print(a[12])

#loop
for s in "nirvana":
    print(s)

#length
a = "Hello ! "
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing, The first character has index 0!
b = "Hello, World!"
print(b[2:5])
#slice from starrt
b = "Hello, World!"
print(b[:5])
# s to the end
b = "Hello, World!"
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])