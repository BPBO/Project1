'''--------------------------------------------------------------------
    Tittle: desarrollo de funciones Prefija y Postfija
    Developed by: Alex Montano Rojas
    Date: January of 2021
-----------------------------------------------------------------------
'''
def Prefija(cadena):
    
    """Esta funcion realiza la conversion de notacion Infija a 
    Prefija"""

    if evaluarP(cadena) and evaluarO(cadena) and evaluarA(cadena):
        i = len(cadena)-1   #variable de control de ciclo
        pila = []           #pila auxiliar
        prefija = []        #lista resultado
        while(i >= 0):
            if isNumber(cadena[i]):
                num = cadena[i]
                if i - 1 >= 0:
                    while isNumber(cadena[i-1]):
                        num = num + cadena[i-1]
                        i -= 1
                        if i <= 0:
                            break
                prefija.append(voltearC(num))
            elif esOperador(cadena[i]):
                if pilaEmpty(pila):
                    pila.append(cadena[i])
                else:
                    j = len(pila)- 1    #direccion del tope de la pila
                    if esOperador(pila[j]) and jerarquia(pila[j]) > jerarquia(cadena[i]):
                        prefija.append(pila.pop())
                        pila.append(cadena[i])
                    elif esOperador(pila[j]) and jerarquia(pila[j]) < jerarquia(cadena[i]):
                        pila.append(cadena[i])
                    else:
                        pila.append(cadena[i])
                    
            elif cadena[i] == "(":
                l = len(pila) -1    
                while(pila[l] != ")"):
                    prefija.append(pila.pop())
                    l -= 1
                pila.pop()
            elif cadena[i] == ")":
                pila.append(cadena[i])
            i -= 1
        if not pilaEmpty(pila):
            while(not pilaEmpty(pila)):
                prefija.append(pila.pop())
        return voltearL(prefija)
    else:
        print("error, expresion no valida!")
        return None

def Postfija(cadena):
    
    """Esta funcion realiza la conversion de notacion Infija a 
    Postfija"""

    if evaluarP(cadena) and evaluarO(cadena) and evaluarA(cadena):
        l = len(cadena) #variable de control de ciclo
        i = 0           #variable de control de ciclo
        pila = []       #pila auxiliar
        postfija = []   #lista resultado
        while(i < l):
            if cadena[i] == "(": 
                pila.append(cadena[i])
            elif isNumber(cadena[i]):
                num = cadena[i]
                if i + 1 < l:
                    while isNumber(cadena[i+1]):
                        num = num + cadena[i+1]
                        i += 1
                        if i >= l-1:
                            break
                postfija.append(num)
            elif esOperador(cadena[i]):
                if pilaEmpty(pila):
                    pila.append(cadena[i])
                else:
                    j = len(pila)- 1    #direccion del tope de la pila
                    if esOperador(pila[j]) and jerarquia(pila[j]) > jerarquia(cadena[i]):
                        postfija.append(pila.pop())
                        pila.append(cadena[i])
                    elif esOperador(pila[j]) and jerarquia(pila[j]) < jerarquia(cadena[i]):
                        pila.append(cadena[i])
                    else:
                        pila.append(cadena[i])
            elif cadena[i] == ")":
                lp = len(pila) -1
                while(pila[lp] != "("):
                    postfija.append(pila.pop())
                    lp -= 1
                pila.pop()
            i += 1
        if not pilaEmpty(pila):
            while(not pilaEmpty(pila)):
                postfija.append(pila.pop())
        return postfija
    else:
        print("error, expresion no valida!")
        return None


def voltearL(v):
    """Invierte el orden de los elementos de la lista"""
    i = 0
    j = len(v)-1
    while i < j:
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
        i += 1
        j -= 1
    return v

def voltearC(v):
    """Invierte el orden de los caracteres de una cadena"""
    j = len(v)-1
    resp = ""
    while j >= 0:
        resp = resp + v[j]
        j -= 1
    return resp

def jerarquia(operador):
    """retorna el la jerarquia de un operador"""
    if operador == "+" or operador == "-":
        return 1
    else:
        return 2

def evaluarP(cadena):

    """Evalua parentesis"""

    l = len(cadena)
    i = 0
    pila = []
    while(i < l ):
        if (cadena[i] == "("):
            pila.append(cadena[i])
        if (cadena[i] == ")"):
            if pilaEmpty(pila):
                return False
            pila.pop()
        i += 1
    if not pilaEmpty(pila):
        return False
    else:
        return True

def pilaEmpty(pila):
    """retorna true si la pila esta vacia"""
    return len(pila) == 0


def evaluarO(cadena):

    """Evalua operandos de manera que haya un operando en los extremos"""

    if not isEmpty(cadena):
        l = len(cadena)
        if l > 2:
            i = 0
            j = l - 1
            flag = True
            if cadena[i] == "(":
                while cadena[i] == "(" and i < l:
                    i += 1
                flag = isNumber(cadena[i+1])
            else:
                flag = isNumber(cadena[i])
            if cadena[j] == ")":
                while cadena[j-1] == ")" and j > 0:
                    j -= 1
                flag = isNumber(cadena[j-1])
            else:
                flag = isNumber(cadena[j])
            return flag
        elif l == 2:
            return isNumber(cadena[0]) and isNumber(cadena[-1])
        else:
            return isNumber(cadena[0])



def isEmpty(cadena):
    """retorna true si la cadena esta vacia"""
    return len(cadena) == 0

def isNumber(n):
    """retorna true si 'n' es un numero"""
    return all(n[i] in "0123456789" for i in range(len(n)))

def evaluarA(cadena):

    """Evalua alternancia de datos de manera de haya operando y operador"""

    l = len(cadena)
    i = 1
    flag = True
    while(i < l-2) and flag:
        if cadena[i] == "(":
            while cadena[i+1] == "(" and i < l-2:
                i += 1
            flag = isNumber(cadena[i+1])
        elif cadena[i] == ")":   
            while cadena[i+1] == ")" and i < l-2:
                i += 1 
            if esOperador(cadena[i+1]):
                flag = cadena[i+2] == "(" or isNumber(cadena[i+2])   
        elif isNumber(cadena[i]):
            while isNumber(cadena[i+1]) and i < l-2:
                i += 1
            flag = esOperador(cadena[i+1]) or cadena[i+1] == ")"
        else:
            flag = isNumber(cadena[i+1]) or cadena[i+1] == "("
        i += 1
    return flag

def esOperador(o):
    """"retorna true si 'o' es un operador"""
    return o == "+" or o == "-" or o == "/" or o == "*"


"""if __name__ == "__main__":
    cadena = "((89)*5)+9/(7-4)"
    if Prefija(cadena) is not None:
        print(Prefija(cadena))"""
   
