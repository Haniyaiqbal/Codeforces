# // Problem: B. Borze
# // Contest: Codeforces - Codeforces Beta Round 32 (Div. 2, Codeforces format)
# // URL: https://codeforces.com/problemset/problem/32/B
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)
# 
# 

def q4():

	s = input()
	
	res = []
	
	i =0
	
	while i < len(s):
	
		if s[i] == '.':
		
			res.append('0')
			
			i+=1
			
		elif s[i] == '-':
		
			if i+1 < len(s) and s[i+1] == '.':
			
				res.append('1')
				
				i+=2
				
			elif i+1 < len(s) and s[i+1] == '-':
			
				res.append('2')
				
				i+=2
				
	return ''.join(res)
			
	
print(q4())