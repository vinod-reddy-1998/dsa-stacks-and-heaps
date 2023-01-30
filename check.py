word=input()
check=True
if word[-1]=="_":
    word=word[:-1]
m=word.split("_")
for i in word:

    if ord(i)>64 and ord(i)<90 or ord(i)==95:
        check=True
    else:
        check=False
        break
if check:    
    print(check,len(m))
else:
    print(check)