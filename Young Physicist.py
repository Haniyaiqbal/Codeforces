# // Problem: A. Young Physicist
# // Contest: Codeforces - Codeforces Beta Round 63 (Div. 2)
# // URL: https://codeforces.com/problemset/problem/69/A
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)
# 
# 

def q1():

	n = int(input())
	sumx, sumy, sumz = 0,0,0
	
	while n>0:
		
		x,y,z = [int(i) for i in input().split()]
		
		sumx+=x
		sumy+=y
		sumz+=z
	
		n-=1
		
	if sumx == 0 and sumy ==0 and sumz==0:
	
		return 'YES'
	else:
		return 'NO'
		
print(q1())
	