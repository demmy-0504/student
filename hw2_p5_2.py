k=input("enter a string:")
n=""+k+""
for i in range(0,len(n)):#怎麼知道是len(n) #為何要去頭去尾 用第一個if 不就會一個一個比了嗎 #打出來的成果是錯的
	if n[1+i:len(n)-1-i]==n[len(n)-2-i:i:-1]:
		print("longest palindrome substring is:",n[1+i:len(n)-1])
		break
	elif n[2+i:len(n)-1-i]==n[len(n)-2-i:i+1:-1]:
		print("longest palindrome substring is:",n[2+i:len(n)-1-i])
		break
	else:
		if n[1+i:len(n)-2-i]==n[len(n)-3-i:i:-1]:
			print("longest palindrome substring is:",n[1+i:len(n)-2-i])
			break
	i+=1
