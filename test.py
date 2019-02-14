def clean(x):
    y=''
    s=['.',',','-','/','}','{','"',':',';','(',')','[',']']
    for i in x:
        if i in s:
            continue
        else:
                y+=i
    return y

f=open("file16.txt")
content=f.read()
content=clean(content)
print(content)
