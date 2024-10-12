# // Problem: B. Queue at the School
# // Contest: Codeforces - Codeforces Round 163 (Div. 2)
# // URL: https://codeforces.com/problemset/problem/266/B
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)
# 
def q3():
	
	n, t = [int(x) for x in input().split()]
	
	s = input()
	
	l = list(s)
	
	for i in range(t):
	
		j = 0
		
		while j<n-1:
		
			if l[j] == 'B' and l[j+1] == 'G':
			
				l[j], l[j+1] = l[j+1], l[j]
				
				j+=1
				
			j+=1
			
	return ''.join(l)
	
print(q3())