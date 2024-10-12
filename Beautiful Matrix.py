# // Problem: A. Beautiful Matrix
# // Contest: Codeforces - Codeforces Round 161 (Div. 2)
# // URL: https://codeforces.com/problemset/problem/263/A
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)
# 
def q2():
	
	mat = []
	
	for i in range(5):
		
		row = [int(x) for x in input().split()]
			
		mat.append(row)
 			
			
	for idx, row in enumerate(mat):
	
		for i in range(len(row)):
		
			if mat[idx][i] == 1:
			
				x,y = idx,i
				
	diff = abs(2-x) + abs(2-y)
	
	return diff
	
print(q2())
		
		
	
	