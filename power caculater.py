a=int(input("enter a number"))
b=int(input("enter another number"))

result = 1

for exponent in range(b, 0, -1):
    result *=a

print("Answer = " + str(result))