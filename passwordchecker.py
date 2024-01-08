string = input("Enter a string: ")
numcount = 0
splcount = 0
lettercount = 0
for i in string:
    if i.isdigit():
        numcount+=1
    elif i.isalpha():
        lettercount+=1
    elif i in '!@#$%^&*()_+=,.?/~':
        splcount+=1
    else:
        continue
if(numcount>=1 and splcount>=1 and lettercount>=1 and numcount+lettercount+splcount>=8):
    print("Strong password")
else:
    print("Weak password")