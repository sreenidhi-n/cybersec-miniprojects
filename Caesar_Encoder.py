def rotate(string, n):
    return string[n:] + string[:n]

def NotTheSalad(cypher, shift):
    res = ''
    for i in range(len(cypher)):
        char = cypher[i]
        if char.isupper():
            res+=chr((ord(char)+shift-65)+65) #alphabet position+65
        else: 
            res+=chr((ord(char)+shift-97)+97)
    return res            

cypher = input("Enter a string: ")
shift = int(input("Enter a shift value: "))
print(NotTheSalad(cypher, shift))