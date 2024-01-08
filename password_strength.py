# Checking strength of an entered password

def check(passwd):
    if(len(passwd)==0):
        return 'Invalid'
    nums = 0
    chars = 0
    spl = 0
    for i in passwd:
        if i.isdigit():
            nums+=1
        elif i.isalpha():
            chars+=1
        else:
            spl+=1
    if(nums>=1 and spl>=1 and chars>=8):
        return 'Valid'
    else:
        return 'Invalid'

print(check('Sreenidhi!02'))
