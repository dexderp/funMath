from sympy import *; 
from scipy.special import comb;
from math import *;

#Computes the wave function for a given state of the hydrogen atom given the three 
#quantum numbers (n,l,m): 
# n - energy level 
# l - angular momentum 
# m - z component of l  
x = Symbol('x');
laggPoly = {0:1,1:1-x,}; 

def checkInts(listy):
	for i in range(len(listy)):
		if not listy[i].isdigit():
			return False; 

	return True;  


def computeLaggPoly(n): 
	if laggPoly.has_key(n):
		return laggPoly[n];
	else: 
		if not (laggPoly.has_key(n-1)): 
			computeLaggPoly(n-1);

		tempExpr = expand((((2*(n-1) + 1 - x)*(laggPoly[n-1])) - ((n-1)*laggPoly[n-2]))/n);
		return laggPoly[n];
		
def main(): 
	inputFlag = True; 
	while(inputFlag): 
		rawInput = raw_input('Please enter a comma seperated list of non negative integers: '); 
		inputList = rawInput.split(','); 

		if(len(inputList) == 3 and checkInts(inputList)):
			inputFlag = False; 

		else: 
			print('Invalid input. Enter in the following format - (2,3,4)'); 
			print('\n');
			inputFlag = True;


	n = int(inputList[0]); 
	computeLaggPoly(n); 
	print(laggPoly[n]);






if __name__ == '__main__':
	main();