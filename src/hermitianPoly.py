from sympy import *;

#This program provides a program to generate any nth order hermite polynomial. 
#User will provide an integer n and the corresponding hermite polynomial will be printed symbolically. 
x = Symbol('x');  
exponential = exp(-x**2); 


def HermitePoly(n):
	hermiteOrderN = ((-1)**n) * exp((x)**2) * diff(exponential,x,n);
	return (hermiteOrderN);

def main():
	inputFlag = True; 
	while(inputFlag):
		rawInput = raw_input('Please enter a non-negative integer: '); 
		print(rawInput);

		if rawInput.isdigit() :
			value = int(rawInput); 
			inputFlag = False;
		else:
			print('not an integer.Try again'); 

	nthOrder = HermitePoly(value);
	print(nthOrder);



main();