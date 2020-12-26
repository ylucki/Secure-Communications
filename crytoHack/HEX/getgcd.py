

def eu_gcd(x, y):
    if x < y:
        return eu_gcd(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    return x

def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

a = 66528
b = 52920

print(eu_gcd(a, b))

print("u,v: {} {}".format(u,v))


# To compute x^y under modulo m 
def power(x,y,m): 
  
    if (y == 0): 
        return 1
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
   
    return p if(y % 2 == 0) else  (x * p) % m 
  
# Function to find modular 
# inverse of a under modulo m 
# Assumption: m is prime 
def modInverse(a,m): 
  
    if (eu_gcd(a, m) != 1): 
        print("Inverse doesn't exist") 
   
    else: 
   
        # If a and m are relatively prime, then 
        # modulo inverse is a^(m-2) mode m 
        print("Modular multiplicative inverse is ", 
             power(a, m - 2, m)) 
  
# Driver code 
  
a = 3
m = 13
modInverse(a, m)


def quadRes(a,p):
    QR = 0
    b = 0
    for b in range(1,((p-1)//2) + 1):
        if (b ** 2) % p == a:
            print("b {}".format(b))
            QR = 1
    if (QR == 1):
        print("{} is a QR mod {}".format(a, p))
    else:
        print ("{} is a QNR mod {}".format(a, p))

p = 29
qlist = [14, 6, 11]

for i in qlist:
    quadRes(i,p)