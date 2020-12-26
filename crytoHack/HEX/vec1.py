#!/usr/lib/bin python3
import numpy as np

#v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u. 


#print(9*14+36*14+18*4)

a = np.array([4, 6, 2, 5])
print(np.inner(a,a))

def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    return Q

v = np.array([[4,1,3,-1], [2,1,-3,4], [1,0,-2,7], [6, 2, 9, -5]])
u = gram_schmidt_columns(v)

def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():  
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)




def gram_sc(A):
    """Orthogonalize a set of vectors stored as the columns of matrix A."""
    # Get the number of vectors.
    n = A.shape[1]
    for j in range(n):
        # To orthogonalize the vector in column j with respect to the
        # previous vectors, subtract from it its projection onto
        # each of the previous vectors.
        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
        A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    return A
u = gram_sc(v)
print(u)

A = np.array([[4.0,1.0,3.0,-1.0], [2.0,1.0,-3.0,4.0], [1.0,0.0,-2.0,7.0], [6.0, 2.0, 9.0, -5.0]])
print(gram_sc(A))