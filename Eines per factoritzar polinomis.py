# Immports




from math import gcd
from math import factorial
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
    a = a * (-1)
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



def sumar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    if len(polinomi_a) > len(polinomi_b):
        grau_superior = len(polinomi_a)-1
    else:
        grau_superior = len(polinomi_b)-1
    
    for i in range(0, grau_superior - (len(polinomi_a)-1)):
        polinomi_a.append(0)
    for i in range(0, grau_superior - (len(polinomi_b)-1)):
        polinomi_b.append(0)
    
    for i in range(0, grau_superior+1):
        polinomi_resultat.append(polinomi_a[i] + polinomi_b[i])
    
    return polinomi_resultat



def restar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    if len(polinomi_a) > len(polinomi_b):
        grau_superior = len(polinomi_a)-1
    else:
        grau_superior = len(polinomi_b)-1
    
    for i in range(0, grau_superior - (len(polinomi_a)-1)):
        polinomi_a.append(0)
    for i in range(0, grau_superior - (len(polinomi_b)-1)):
        polinomi_b.append(0)
    
    for i in range(0, grau_superior+1):
        polinomi_resultat.append(polinomi_a[i] - polinomi_b[i])
    
    return polinomi_resultat



def multiplicar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    grau_a = len(polinomi_a)-1
    grau_b = len(polinomi_b)-1
    grau = len(polinomi_a) + len(polinomi_b) - 2

    for i in range(0, grau+1):
        polinomi_resultat.append(0)
    
    for i in range(0, grau_a+1):
        for j in range(0, grau_b+1):
            polinomi_resultat[grau - (grau_a - i) - (grau_b - j)] += polinomi_a[i] * polinomi_b[j]
    
    return polinomi_resultat



def dividir_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    grau_resultat = len(polinomi_a) - len(polinomi_b)

    if grau_resultat < 0:
        raise Exception("El polinomi primer polinomi ha de ser de grau superior o igual al segon")

    for i in range(0, grau_resultat+1):
        polinomi_resultat.append(0)
    
    i = 0
    while i < len(polinomi_a) and len(polinomi_a)-1-i >= len(polinomi_b)-1:
        coef_a = polinomi_a[i]
        grau_a = len(polinomi_a) - 1 - i
        coef_b = polinomi_b[0]
        grau_b = len(polinomi_b) - 1

        polinomi_resultat[grau_resultat - (grau_a - grau_b)] = coef_a / coef_b

        for j in range(0, grau_b+1):
            polinomi_a[i+j] -= (coef_a / coef_b) * polinomi_b[j]
    
    return [polinomi_resultat, polinomi_a]



def punt_triangle_pascal(n, p):
    if p == 0 or p == n:
        return 1
    elif p == 1 or p == n-1:
        return n
    else:
        punt = factorial(n) / (factorial(p) * factorial(n-p))
        return punt



def binomi_de_newton(grau):
    coefs = []

    for i in range(0, grau+1):
        coefs.append(punt_triangle_pascal(grau, i))
    
    return coefs




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
        output += f" + {polinomi[i]}x^{grau - i}"
    
    print(output)
    print("")



def print_bin_new(coefs):
    output = f"El polinomi resultant es: "

    output += f"{coefs[0]}(a^{len(coefs)-1})(b^0)"

    for i in range(1, len(coefs)):
        output += f" + {coefs[i]}(a^{len(coefs)-1-i})(b^{i})"
    
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

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a) : ")) * -1

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

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a) : ")) * -1

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



def fer_suma():

    try:

        print("Introdueix el polinomi que vols sumar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols sumar")
        polinomi_b = demanar_polinomi()

        resultat = sumar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_resta():

    try:

        print("Introdueix el polinomi que vols restar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols restar")
        polinomi_b = demanar_polinomi()

        resultat = restar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_multiplicacio():

    try:

        print("Introdueix el polinomi que vols multiplicar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols multiplicar")
        polinomi_b = demanar_polinomi()

        resultat = multiplicar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_divisio():

    try:

        print("Introdueix el polinomi que vols dividir")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols dividir")
        polinomi_b = demanar_polinomi()

        resultat, resta = dividir_polinomis(polinomi_a, polinomi_b)

        print("El cuocient es: ")
        print_polinomi(resultat)
        print("El residu es: ")
        print_polinomi(resta)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def  fer_binomi_de_newton():

    try:

        grau = int(input("Introdueix el grau n del binomi ( (a+b)^n ) : "))

        resultat = binomi_de_newton(grau)

        print_bin_new(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre natural.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def  fer_punt_triangle_pascal():

    try:

        n = int(input("Introdueix la fila n del triangle: "))
        p = int(input("Introdueix la columna p del triangle: "))

        resultat = punt_triangle_pascal(n, p)

        print(f"Aquest punt del triangle de Pascal es: {resultat}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre natural.")
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
    Operacions basiques:
        Sum - Sumar polinomis
        Res - Restar polinomis
        Mul - Multiplicar polinomis
        Div - Dividir polinomis
    Factorització:
        Fac - Factoritzar polinomi
        Teo - Teorema del residu
        Exa - Trobar divisor exacte
        Ruf - Rufini
    Binomi de Newton:
        Bin - Binomi de Newton
        Pas - Punt triangle de Pascal
    S - Sortir
Opció: ''').strip().lower()
    print("")

    opcio_valida = False
    if entrada == "sum":
        fer_suma()
        opcio_valida = True
    elif entrada == "res":
        fer_resta()
        opcio_valida = True
    elif entrada == "mul":
        fer_multiplicacio()
        opcio_valida = True
    elif entrada == "div":
        fer_divisio()
        opcio_valida = True
    elif entrada == "fac":
        factoritzador()
        opcio_valida = True
    elif entrada == "teo":
        teorema_del_residu()
        opcio_valida = True
    elif entrada == "exa":
        trobar_divisor()
        opcio_valida = True
    elif entrada == "ruf":
        fer_rufini()
        opcio_valida = True
    elif entrada == "bin":
        fer_binomi_de_newton()
        opcio_valida = True
    elif entrada == "pas":
        fer_punt_triangle_pascal()
        opcio_valida = True
    
    if opcio_valida:
        input("Prem enter per continuar")
    print("")

input("Prem enter per sortir")
exit()