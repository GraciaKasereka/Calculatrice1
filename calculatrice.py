#obtention des entrées 
num1= 1 
num2 = 3 
def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Erreur: Division par zéro"
    else:
        return num1 / num2 
#affichage des résultats
print("Addition:", addition(num1, num2))
print("Soustraction:", soustraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))