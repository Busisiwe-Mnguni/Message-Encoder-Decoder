ascii_list = []
string = int(input())
while string != -1:
	ascii_list.append(string)
	string = int(input())

another = []
for i in ascii_list:
	another.append(chr(i))

for j in range(len(another)):
	print(another[j], end = '')
