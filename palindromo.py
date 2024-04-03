
def is_palindrome(input:str):
    input = input.lower()
    rever = input[::-1]
    if rever == input:
        result = True
    else:
        result = False
    # print(rever)
    # print(input)
    return result

def cant_palabras_palindromes(inputlist:str):
    cant = 0
    for p in inputlist:
        p=p.lower()
        p=p.replace(" ", "")
        rever = p[::-1]
        if rever == p:
            cant += 1
    return cant  


