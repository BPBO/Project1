'''--------------------------------------------------------------------
    Tittle: Arbol Binario de Expresiones
    Developed by: Alex Montano Rojas
    Date: January of 2021
-----------------------------------------------------------------------
'''

from .InfijaPosfija import *


class Nodo:

    """Tipo de Dato Abstracto Nodo que sirve para crear instancias de
    la clase Nodo que conforman un Arbol de Expresiones"""

    def __init__(self,value):
        self.__dato = value
        self.__izq = None
        self.__der = None
    """ Arguments of class Nodo
        Note: 
            include arguments of type object
        Args:
            value(obj): first data of Nodo
        Returns:
            dato(obj): first value of Nodo
    """
    #Methods Getters and Setters of class Nodo
    #decorate property for dato
    @property
    def dato(self):
        """metodo selector que retorna el dato de la clase Nodo"""
        return self.__dato

    @dato.setter
    def dato(self, value):
        """metodo modificador que modifica el dato de la clase Nodo"""
        self.__dato = value
    
    def __getIzquierdo(self):
        """selector del atributo privado izq de la clase Nodo"""
        return self.__izq

    def __setIzquierdo(self, node):
        """modificador del atributo privado izq de la clase Nodo"""
        self.__izq = node
    #property for izquierdo
    izquierdo = property(__getIzquierdo, __setIzquierdo)
    
    @property
    def derecho(self):
        """selector del atributo privado der de la clase Nodo"""
        return self.__der

    @derecho.setter
    def derecho(self, node):
        """modificador del atributo privado der de la clase Nodo"""
        self.__der = node
    

#Clase Arbol de Expresiones---------------------------------------------------
class ArbolExp:

    """Crea una instacia de la clase Arbol Binario de Expresiones"""

    def __init__(self):
        self.__raiz = None
        self.__tam = 0

    #Getters and Setters
    def __getRoot(self):
        return self.__raiz

    def __setRoot(self, root):
        self.__raiz = root

    raiz = property(__getRoot, __setRoot)

    def __getTam(self):
        return self.__tam

    def __setTam(self, tam):
        self.__tam = tam

    size = property(__getTam, __setTam)

    def generar(self, cadena):
        
        """Genera un Arbol de Expresiones partir de una cadena que 
        representa una expresion """

        if Postfija(cadena) is not None:
            lista = Postfija(cadena)
            if lista is not None:
                listaDeNodos(lista) #convertimos en uan lista con cada elemento de tipo Nodo
                self.size = len(lista)
                pila = []
                l = len(lista)-1
                i = 0
                while i <= l:
                    if isNumber(lista[i].dato):
                        pila.append(lista[i])
                    elif esOperador(lista[i].dato):
                        if len(pila) < 2:
                            print("an error ocurred")
                        else:
                            op2 = pila.pop()
                            op1 = pila.pop()
                            newNodo = lista[i]
                            newNodo.derecho = op2
                            newNodo.izquierdo = op1
                            pila.append(newNodo)
                    i += 1
                if len(pila) != 1:
                    print("an error ocurred")
                else:

                    self.raiz = pila.pop()
        """ Arguments
        Note: 
            include arguments of type list
        Args:
            lista(list): List of string
        Returns:
            raiz(obj): root if the tree of expressions
    """

    def calcular(self, root):

        """Calcula el resultado de un arbol de expresiones"""

        if root is None:
            return 0 
        else:
            izq = self.calcular(root.izquierdo)
            der = self.calcular(root.derecho)
            if isNumber(root.dato):
                return root.dato
            else:
                if root.dato == "+":
                    return float(izq) + float(der)
                if root.dato == "-":
                    return float(izq) - float(der)
                if root.dato == "*":
                    return float(izq) * float(der)
                if root.dato == "/":
                    try:
                        return float(izq) / float(der)
                    except ZeroDivisionError:
                        print("no se puede dividir por cero")
        """
        Note:
            Tiene un unico parametro de tipo Nodo 
        Args:
            root(Nodo): Nodo raiz del arbol de expresiones
        Returns:
            int: Retorna un numero entero como resultado
        """

    def preOrder(self, root):
        """metodo que hace un recorrido en pre orden a un
         arbol binario"""
        if root is not None:
            print(root.dato, end="")
            self.preOrder(root.izquierdo)
            self.preOrder(root.derecho) 
    
    def inOrder(self, root):
        """metodo que hace un recorrido en orden a un
         arbol binario"""
        if root is not None:
            self.inOrder(root.izquierdo)
            print(root.dato, end="")
            self.inOrder(root.derecho)

    def postOrder(self, root):
        """metodo que hace un recorrido en post orden a un
         arbol binario"""
        if root is not None:
            self.postOrder(root.izquierdo)
            self.postOrder(root.derecho)
            print(root.dato, end="")
    
    def height(self, root):
        """Altura del Albol binario"""
        if root is None:
            return 0
        else:
            return max(self.height(root.izquierdo),
                        self.height(root.derecho)) + 1

    def empty(self):
        """Funcion que devuelve true si el arbol binario esta vacio"""
        return self.raiz is None

    def hoja(self, nodo):
        """Metodo que devuelve true si el nodo ingresado es hoja"""
        return nodo.izquierdo is None and nodo.derecho is None
        """
        Args: 
            nodo(Nodo): atributo de tipo Nodo
        Returns:
            boolean
        """


def listaDeNodos(lista):

    """Reemplaza cada elemento de la lista con un Nodo con el mismo 
    elemento como dato"""

    l = len(lista)
    if l != 0:
        i = 0
        while i < l:
            lista[i] = Nodo(lista[i])
            i += 1
    """
        Note:
            Tiene un unico parametro de tipo Lista
        Args:
            lista(list): Lista con elementos de tipo char
        Returns:
            lista(list): Lista con elementos de tipo Nodo
        """
        

"""if __name__ == "__main__":
    
    cadena = "((89)*5)+9/(7-4)"
    A = ArbolExp()
    A.generar(cadena)
    A.postOrder(A.raiz)
    print('\n')
    A.preOrder(A.raiz)
    print('\n')
    A.inOrder(A.raiz)
    print('\n')
    print(A.calcular(A.raiz))"""
