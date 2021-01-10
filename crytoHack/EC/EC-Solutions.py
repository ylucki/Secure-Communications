
a = 497
p = 9739

def bits(n):
	while n:
		yield n & 1
		n >>= 1

def find_y(x):
	ysquare = ((x * x * x) + (497 * x) + 1768)
	print("ysquare = ", ysquare)
	print("ysquare mod p = ", ysquare % p)
	print("y mod p = ", (ysquare  % p) ** 0.5)
	return (ysquare  % p) ** 0.5

def inv_mod_p(x):
    """
    Compute an inverse for x modulo p, assuming that x
    is not divisible by p.
    """
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p-2, p)

def point_addition(x1, y1, x2, y2):
	lam = 0

	if x1 == 0 and y1 == 0:
		return x2, y2
	if x2 == 0 and y2 == 0:
		return x1, y1
	if x1 == x2 and y1 == -y2:
		return 0, 0

	if x1 != x2 or y1 != y2:
		lam = (y2 - y1) * inv_mod_p(x2 - x1)
	else:
		lam = (3*(x1 * x1) + a) * inv_mod_p(2 * y1)
	x3 = ((lam * lam) - x1 -x2) % p
	y3 = ((lam * (x1 - x3)) - y1) % p
	return x3 % p, y3 % p

def double_ecc(x1, y1):
	return point_addition(x1, y1, x1, y1)

def scalar_multiplication(x1, y1, n):
	rx = 0
	ry = 0
	x = x1
	y = y1

	for b in bits(n):
		if b:
			rx, ry = point_addition(rx, ry, x, y)
		x, y = double_ecc(x, y)
	print (rx, ry)

def hack_point_addition():
	px = 493
	py = 5564
	qx = 1539
	qy = 4742
	rx = 4403
	ry = 5202

	x1, y1 = point_addition(px, py, px, py)
	x2, y2 = point_addition(qx, qy, rx, ry)
	print(point_addition(x1, y1, x2, y2))

def hack_scalar_multiplication():
	#scalar_multiplication(5323, 5438, 1337)
	scalar_multiplication(2339, 2213, 7863)

def hack_ecdlp():
	nb = 1829
	qax = 815
	qay = 3190
	scalar_multiplication(qax, qay, nb)

def hack_efficient_exchange():
	qx = 4726
	nb = 6534
	qy = 6287
	scalar_multiplication(qx, qy, nb)

hack_efficient_exchange()


