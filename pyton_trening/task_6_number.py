def add(x, y):
    return x + y
print(add(2, 2))
print(add('i a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d
print(arg(1, 1, 1, 1))
print(arg(2, 2))
print(arg(2, 2, 1, 1))

def afr(a=(1, 2, 3, 4)):
    return a[1]
print(afr())

def compute_surface(radius, pi=3.14159):
    return pi * radius * radius
print(compute_surface(2))