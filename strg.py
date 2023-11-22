str1=input("enter a string1")
str2=input("enter a string2")
if(len(str1)>len(str2)):
    long=len(str1)
    short=len(str2)
else:
    long=len(str2)
    short=len(str1)
matchcnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchcnt+=1
print("Similarity between two strings=",matchcnt/long);
        
