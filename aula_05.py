def f(x):
    return x ** 2

print(f(1))
print(f(2))
print(f(3))
print(f(4))

x1 = 2
x2 = 3
y1 = f(x1)
y2 = f(x2)

taxa = (y2 - y1) / (x2 - x1)
print(taxa)

x1 = 2
x2 = 2.001
y1 = f(x1)
y2 = f(x2)

taxa = (y2 - y1) / (x2 - x1)

print(taxa)

