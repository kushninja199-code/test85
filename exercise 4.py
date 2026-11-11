f=open('story.txt','r')
text=f.read()
b=text.split(" ")
for a in range(0,len(b)):
    if b[a][0]=="i":
        print(b[a][::-1],end=' ')
    else:
        print(b[a],end=' ')
f.close()