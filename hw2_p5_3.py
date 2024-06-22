k=int(input("The number of the requested element in Fibonacci(n) number:"))
s1=input('The first string for Palindromic detection(s1)=')
s2=input('The second string for Palindromic detection(s2)=')
x=input('The plaintext to be encrypted:')
print('----- extract key for encrypt method -----')
fib_list=[0,1] 
fib_list.append(fib_list[i-1] + fib_list[i-2])
return fib_list #到底哪裡錯了
result = fib(k+1)
print('The',k,'-th Fibonacci Sequenceresult is:',result[k])
n1=' '+s1+' ' 
n2=' '+s2+' '
for i in range(0,len(n1)):
	if n1[1+i:len(n1)-1-i]==n1[len(n1)-2-i:i:-1]: 
		a=n1[1+i:len(n1)-1-i]
		print('Longest palindrome substing is:',a) 
		print('Length is: ',a)
		break
	else:
		if n1[2+i:len(n1)-1-i]==n1[len(n1)-2-i:i+1:-1]: 
			a=n1[2+i:len(n1)-1-i]
			print('Longest palindrome substing is: ',a) 
			print('Length is: ',len(a))
			break
		elif n1[1+i:len(n1)-2-i]==n1[len(n1)-3-i:i:-1]:#有甚麼問題嗎
			a=n1[1+i:len(n1)-2-i]
			print('Longest palindrome substing is:',a) 
			print('Length is: ',len(a))
			break
i+=1
for j in range(0,len(n2)):
	if n2[1+j:len(n2)-1-j]==n2[len(n2)-2-j:j:-1]: 
		b=n2[1+j:len(n2)-1-j]
		print('Longest palindrome substing is: ',b) 
		print('Length is: ',len(b))
		break 
	else:
		if n2[2+j:len(n2)-1-j]==n1[len(n2)-2-j:j+1:-1]:  
			b=n2[2+j:len(n2)-1-j]
			print('Longest palindrome substing is:',b) 
			print('Length is: ',len(b))
			break
		elif n2[1+j:len(n2)-2-j]==n2[len(n2)-3-j:j:-1]:
			b=n2[1+j:len(n2)-2-j]
			print('Longest palindrome substing is:',b) 
			print('Length is: ',len(b))
			break
j+=1 