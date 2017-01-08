from sympy import *; 
from scipy.special import *;


#################################################################################
x = Symbol('x'); 
testPoly = x**2/2 - 2*x + 1
#we need to get the LCM and multiply it by the highest order coeff 

tempPoly = Poly(testPoly,x); 
arr = tempPoly.coeffs();
print(arr);