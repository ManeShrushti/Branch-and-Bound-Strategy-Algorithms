mat=[]
visited=[]
N=0


def findcost(s):
	global total
	visited[s]=1
	print("%d --> " %int(s+1)),
	c= minval(s)
	
	if(c==1000):
		 c=0
       		 print("%d "%int(c+1))
      		 total+=mat[s][c]
        	 return
	findcost(c)

total=0

def minval(k):
	global total
	cn=1000
	mini=1000
	kmin=0
	for i in range(N):
		if((mat[k][i]!=0) and (visited[i]==0)):
			if((mat[k][i]+mat[i][k])<mini):
				mini=mat[i][0]+mat[k][i]
		                kmin=mat[k][i]
		                cn=i

	if(mini!=1000):	
		total+=kmin

	return cn



if __name__=='__main__':
	s=0
	n=raw_input("Enter the number of Cities\n")
	N=int(n)	
	print("Enter the travelling cost between each city\n")
	for i in range(N):
		temp_list=[]
		for j in range(N):
			if(i!=j):
				val=raw_input(str(i+1)+" --> "+str(j+1)+": ")
				print("\n")
				temp_list.append(int(val))
			else:
				temp_list.append(0)
		mat.append(temp_list)
		visited.append(0)
	findcost(s)
	print("Minimum cost : %d "%total)
