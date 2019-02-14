import json

def first(z):
    return z[0]


def clean(x):
    y=''
    s=['.',',','-','/','}','{','"',':',';','(',')','[',']','“','«','»','°']
    for i in x:
    	if i in s:
            continue
    	else:
    		y+=i
    return y


def squish(x):
    s = frozenset(x)
    return sorted(s)

d={}
ln=0
for x in range(1, 49):
    f=open("file"+str(x)+".txt", "r")

    if f.mode=='r':
        contents = f.read()
        contents = clean(contents)
        tokens = list(map(str, contents.split(" ")))
        # tokens = contents.split(" ")
        ln+=1

#you used contents instead of tokens below
        for word in tokens:
        	if word not in d:
	        	d[word]=[]
	        	d[word].append(1)
	        	d[word].append([ln])
	        else:
	        	d[word][0]+=1
	        	d[word][1].append(ln)


    else:
        exit()
    # for s in tokens:
    #     wordDict[s]=x
f = open("dict.json", "w+")
print('list of d')
ld=list(d)
ld.sort(key=str.lower)
count=0
# for k in ld:
# 	print(k,d[k][0],squish(d[k][1]))
json.dump(d, f)
#    print(str(dict[y]))
   
