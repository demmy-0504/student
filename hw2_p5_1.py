n=int(input("input an integer number:"))
fib=[0,1]
for i in range(2,n):
	fib.append(fib[i-1]+fib[i-2])
	return fib #回傳算的值到清單中 #這行是必要的嗎 #為何outside function
result=fib(n+1)#為何要加一 #這行意思 #是因為列表從0開始然後你要的是第n個嗎
print("the",n,"-th fibonacci sequence resultis:",result[n])

