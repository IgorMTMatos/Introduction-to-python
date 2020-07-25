phrase = """1line
2line
3line"""


print(phrase)

a = "a"
b = "ab"

s = "  abcdefghijk,lmnopqrstuvwxyz"
print(s)
print(s[9])
print(s[3:9])
print(s[-6:-2])
print(len(s))
print(s.strip())
print(s.strip().upper())
print(s.strip().replace("h", "H"))
print(s.split(","))
print("hij" in s)
print("hij" not in s)
print(a+b)
