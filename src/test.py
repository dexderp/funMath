from sympy import *; 

x = Symbol('x'); 
testPoly = x**2 + 1; 



poly = exp(-x**2); 
print(diff(poly,x,3));