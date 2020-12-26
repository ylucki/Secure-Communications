#!/usr/lib/bin python3

p = 991
g = 209

# find the inverse element d such that g * d mod 991 = 1

for d in range(p):
    if (g * d) % p == 1:
        print(d)
        break


p = 28151
g = 2

found = False

while not found:
    for i in range(2,p):
        if pow(g,i,p) == 1:
            break
        if i == p-2:
            print(g)
            found = True
    g = g+1