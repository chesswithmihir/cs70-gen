def gcd(a, b):
    if (b == 0):
        return a
    if a < b:
        return gcd(b, a)
    else:
        return gcd(b, a % b)

print("Welcome to GCD")
x = int(input("What is your first number? "))
y = int(input("What is your second number? "))
print(gcd(x, y))
