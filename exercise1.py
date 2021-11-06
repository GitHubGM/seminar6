try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

lines=file1.readlines()
flag=0
file2=open('output.txt','w')
file3=open('output.txt', 'r')
count=0
list1=[]
for line in lines:
	if line.startswith("Log:"):
		flag=1
		count=0
	elif line.startswith('This automatic notification message was sent by') and flag==1:
		flag=0
		list1.append(count)
	elif not line.startswith('This automatic') and flag==1:
		count+=1
list1.sort()
print(list1)
file2.write(str(list1))
file1.close()
