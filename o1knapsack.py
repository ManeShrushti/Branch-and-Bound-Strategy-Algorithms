
def knapSack(p,w,m,n): 

    if (n==0 or m==0): 
        return 0
 
    if (w[n-1]>m): 
        return knapSack(p,w,m,n-1) 

    else: 
        return max(p[n-1] + knapSack(p,w,m-w[n-1],n-1), 
                   knapSack(p,w,m,n-1)) 
  

if __name__=='__main__':
	profit=[]
	weight=[]
	profits=raw_input("Enter the profits\n")
	pr=profits.split(' ')
	weights=raw_input("Enter the weights\n")
	wt=weights.split(' ')
	m=raw_input("Enter the capacity of bag\n")
	if(len(pr)==len(wt)):
		for i in pr:
			profit.append(int(i))
		for j in wt:
			weight.append(int(j))
		print knapSack(profit,weight,int(m),len(profit))
	else:
		print("profit and weights size does not match\n") 
