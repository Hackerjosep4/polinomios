# Immports




from math import gcd
from functools import reduce
from sympy import divisors



# Funcions


def factoritzar_polinomi(polinomi):
    numeros_extra = []
    factors = []
    polinomi_nou = []
    faccom = factor_comu(polinomi)
    if faccom != 1:
        numeros_extra.append(faccom)
        for i in range(0, len(polinomi)):
            polinomi[i] = polinomi[i] / faccom

    if polinomi[-1] == 0:
        factors.append(0)
        for i in range(0, len(polinomi)-1):
            polinomi_nou.append(polinomi[i])
        
        numeros_extra_nou, factors_nou = factoritzar_polinomi(polinomi)
        for ext in numeros_extra_nou:
            numeros_extra.append(ext)
        for fac in factors_nou:
            factors.append(fac)
        
    elif len(polinomi) == 3:
        
        numeros_extra_nou, factors_nou = factoritzar_2_grau(polinomi)
        for ext in numeros_extra_nou:
            numeros_extra.append(ext)
        for fac in factors_nou:
            factors.append(fac)
        
    elif len(polinomi) > 3:

        
        divisor_exacto = divisivilitat(polinomi)
        if divisor_exacto == 0:
            raise Exception("No hi ha divisor exacte (es un polinomi sense divisors enters)")
        
        factors.append(divisor_exacto)
        polinomi, _ = rufini(polinomi, divisor_exacto)
        
        numeros_extra_nou, factors_nou = factoritzar_polinomi(polinomi)
        for ext in numeros_extra_nou:
            numeros_extra.append(ext)
        for fac in factors_nou:
            factors.append(fac)
        
    elif len(polinomi) == 2:
        if polinomi[0] == 1:
            factors.append(polinomi[1])
        else:
            numeros_extra.append[polinomi[0]]
            factors.append(polinomi[1]/polinomi[0])
        

    return [numeros_extra, factors]



def factor_comu(polinomi):
    faccom = reduce(gcd, polinomi)
    return faccom



def factoritzar_2_grau(polinomi):
    numeros_extra = []
    factors = []

    if polinomi[0] != 1:
        numeros_extra.append(polinomi[0])
    
    a = polinomi[0]
    b = polinomi[1]
    c = polinomi[2]

    delta = ((b ** 2) - (4 * a * c))

    if delta < 0:
        raise Exception("La ecuació de 2n grau no te solució")

    sol1 = ((-1 * b) + (delta ** (1 / 2))) / (2 * a)
    sol2 = ((-1 * b) - (delta ** (1 / 2))) / (2 * a)

    factors.append(sol1 * -1)
    factors.append(sol2 * -1)

    return [numeros_extra, factors]



def rufini(polinomi, a):
    a = a * -1
    polinomi_nou = []

    res_anterior = 0
    for i in range(0, len(polinomi)):
        res =  polinomi[i] + (res_anterior*a)
        polinomi_nou.append(res)
        res_anterior = res

        polinomi_nou.pop()

    return [polinomi_nou, res_anterior]



def residu(polinomi, a):
    a = a * -1
    residu = 0
    grau = len(polinomi)-1

    for i in range(0, grau+1):
        residu += polinomi[i] * (a**(grau-i))

    return residu



def divisivilitat(polinomi):
    divisores = []
    for divisor in divisors(polinomi[-1]):
        divisores.append(divisor)
        divisores.append(divisor * -1)
    
    divisor_exacto = 0
    for div in divisores:
        if residu(polinomi, div) == 0:
            divisor_exacto = div
            break
    return divisor_exacto



def print_factors(nums_extra, factors):

    output = f"La factorització es: "

    if len(nums_extra) > 0:
        output += f"{nums_extra[0]}"

        for i in range(1, len(nums_extra)):
            output += f" * {nums_extra[i]}"
    

    if len(nums_extra) == 0:
        if factors[0] < 0:
            output += f"(x{factors[0]})"
        elif factors[0] == 0:
            output += f"x"
        else:
            output += f"(x+{factors[0]})"
    else:
        if factors[0] < 0:
            output += f" * (x{factors[0]})"
        elif factors[0] == 0:
            output += f" * x"
        else:
            output += f" * (x+{factors[0]})"

    for i in range(1, len(factors)):
        if factors[i] < 0:
            output += f" * (x{factors[i]})"
        elif factors[i] == 0:
            output += f" * x"
        else:
            output += f" * (x+{factors[i]})"
    

    print(output)
    print("")



def print_polinomi(polinomi):
    grau = len(polinomi)-1
    output = f"El polinommi es: "

    output += f"{polinomi[0]}x^{grau}"

    for i in range(1, len(polinomi)):
        output += f" + {polinomi[0]}x^{grau - i}"
    
    print(output)
    print("")



def print_solucions(solucions):
    output = f"Les posibles solucions son: "

    output += f"{solucions[0]}"

    for i in range(1, len(solucions)):
        output += f" / {solucions[i]}"
    
    print(output)
    print("")



def calc_solucions(factors):
    solucions = []

    for fac in factors:
        solucions.append(fac * -1)

    return solucions



def demanar_polinomi():
    grau = int(input("Siusplau introdueix el grau del polinomi: "))
    polinomi = []
    for i in range(0, grau + 1):
        a = input(f"Introdueix el coeficient de grau {grau-i} : ").strip()
        polinomi.append(int(a))
    print("")
    
    return polinomi



def factoritzador():

    try:

        print("Hola, a continuacio factoritzarem polinomis")
        
        polinomi = demanar_polinomi()

        numeros_extra, factors = factoritzar_polinomi(polinomi)

        print_factors(numeros_extra, factors)
        print_solucions(calc_solucions(factors))

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def teorema_del_residu():

    try:

        polinomi = demanar_polinomi()

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a)")) * -1

        resultat = residu(polinomi, a)

        print(f"El residu es: {resultat}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def trobar_divisor():

    try:

        polinomi = demanar_polinomi()

        resultat = divisivilitat(polinomi)

        print_polinomi(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_rufini():

    try:

        polinomi = demanar_polinomi()

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a)")) * -1

        resultat, residu = rufini(polinomi, a)

        print_polinomi(resultat)
        print(f"El residu es: {residu}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")




# Codi d'interaccio amb l'usuari / Codi d'iniciació del programa

entrada = ""

while entrada != "s":
    entrada = input('''
Menu:
    F - Factoritzador
    T - Teorema del residu
    D - Trobar divior
    R - Rufini
    S - Sortir
Opció: ''').strip().lower()
    print("")

    opcio_valida = False
    if entrada == "f":
        factoritzador()
        opcio_valida = True
    elif entrada == "t":
        teorema_del_residu()
        opcio_valida = True
    elif entrada == "d":
        trobar_divisor()
        opcio_valida = True
    elif entrada == "r":
        fer_rufini()
        opcio_valida = True
    
    if opcio_valida:
        input("Prem enter per continuar")
    print("")

input("Prem enter per sortir")
exit()