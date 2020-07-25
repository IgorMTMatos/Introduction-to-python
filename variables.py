x, y, z = "Orange", 'Summon', "Cherry"
w = v = c = 30
string = "string"
example = 'example'
stringexample = string + example
m = 40


def globalf(second):
    global m
    m = second


print(x)
print(y)
print(z)

print(w)
print(v)
print(c)

print(string+"_example")
print(stringexample)

print(m)
globalf(22)
print(m)
