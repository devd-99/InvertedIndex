import json

def squish(x):
    s = frozenset(x)
    return sorted(s)

def wordIntersect(x, y):
	s1 = set()
	for i in x:
		s1.add(i)
	s2 = set()
	for j in y:
		s2.add(j)
	return s1.intersection(s2)



def wordUnion(x, y):
	s1 = set()
	for i in x:
		s1.add(i)
	s2 = set()
	for j in y:
		s2.add(j)
	return s1.union(s2)




f = open("dict.json", "r")
if(f==""):
	print("dictionary is empty!")
	exit()
dictionary=json.load(f)
query = input()
token= query.split(" ")
if(len(token)==1):
	isFound=False
	for x in dictionary:
		if(query==x):
			isFound=True
			print(x, dictionary[x][0], squish(dictionary[x][1]))
	if(isFound==False):
		print("token not found")
		exit()
elif (len(token)==3):
	setList=[]
	token1Found=False
	token2Found=False
	for x in dictionary:
		if(token[0]==x):
			token1Found=True
			list1 = dictionary[x][1]
		if(token[2]==x):
			token2Found=True
			list2 = dictionary[x][1]
	if(token1Found==False or token2Found==False):
		print("Token not found")
		exit()
	if(str.lower(token[1])=="and"):
		# print("and")
		res = wordIntersect(list1, list2)
		print(token[0]," and ",token[2],":",res)
	elif(str.lower(token[1])=="or"):
		res = wordUnion(list1, list2)
		print(token[0]," and ",token[2],": ",res)
		# print("or")
else:
	print("invalid syntax")