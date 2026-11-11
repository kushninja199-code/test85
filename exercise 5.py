# code language:
# question:
# write two python codes which converts your language into code language and another code should convert code language to our language:
# if word has 3 or less letters then word should be printed reverse example for=rof
# if word has 4 or more letters than print three random alphbets at the starting and at the end also the first alphabet should be placed at the end of the word. example harry=uyiarryhwsx

a = input("write your code: ")
b=a.split(" ")
for i in range(0,len(b)):
    if len(b[i])<=3 :
        print(b[i][::-1],end=" ")
    elif len(b[i])>3:
        print("iuy"+b[i][1:]+b[i][0]+"poi",end=" ")


a = input("write your code: ")
b=a.split(" ")
for i in range(0,len(b)):
    if len(b[i])<=3 :
        print(b[i][::-1],end=" ")
    elif len(b[i])>3:
        print(b[i][-4]+b[i][3:-4],end=" ")