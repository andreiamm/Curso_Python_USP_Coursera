def incomodam(n):
    if n <= 0:
        return ""
    else:
        return n * "incomodam "

def elefantes(n):
    if n < 1:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(1) + "\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"
    elif n > 2:
        parte2 = "\n" + str(n-1) + " elefantes incomodam muita gente"
        parte3 = "\n" + str(n) + " elefantes " + incomodam(n) + "muito mais" 
        return elefantes(n-1) + parte2 + parte3

#print(elefantes(4))
