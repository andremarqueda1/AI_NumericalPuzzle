# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:28:14 2020
PÝTHON 3.X.X 
No dependencies needed
@author: Narváez Marqueda Ricardo André Sebast (RAM)
"""

INITIAL_STATE=[0,0,0,5,4] # Los ceros representan un espacio aún no ocupado
CONSTANTES=[1,2,3]# Números a colocar en las casillas desocupadas

class Node:

    def __init__(self, data):#Declaración del nodo
        self.data = data #Data será la lista que contendrá el estatus actual de las casillas
        self.hijos=[] #Hijos será una lista dado que es un arbol no binario
        self.padre=None #Referencia al padre para realizar backtracking
    
    #Imprimir valor del nodo actual
    def printValue(self):
        print("Node Value",self.data)
        
    #Insertar un hijo    
    def insertNode(self,node):
        self.hijos.append(node)
        node.padre=self
    #BORRAR, imprime el valor del padre
    def printPadre(self):
        print("My father's value is")
        self.padre.printValue()
    #Imprime el estatus general dado un nodo
    def showNodeStatus(self):
        print("El estado del nodo actual es")
        self.printValue()
        print("#hijos: ",len(self.hijos))
        if self.padre !=None:
            print("padre: ",self.padre.printValue())
        else:
            print("Nodo Raíz")
    
    def recorrerArbol(self):
        for i in range(len(self.hijos)):
            self.hijos[i].printValue()



#Función que aplica los operadores de manera recursiva
def operadorRaiz(nodo):
    estadoActual=nodo.data[:]#Se obtiene el estado actual del nodo
    operadoresDisponibles=CONSTANTES[:]#Se mantiene una bitácora de los operadores
    for i in range(3):#El rango es a tres dado que por la implementación de la lista solo los primeros 3 lugares son las casillas a utilizar
        if nodo.data[i]!=0:#Si ya se utilizó un operador en alguno de las casillas disponibles
            operadoresDisponibles.remove(nodo.data[i])#Se remueve de los operadores disponibles a utilizar
            
    if len(operadoresDisponibles)!=0:#Si ya no quedan operadores, el nodo en materia es una hoja
        for i in range(len(operadoresDisponibles)):#Operadores disponibles
            estadoActual=nodo.data[:]
            for j in range(estadoActual.count(0)): #Contando el número de espacios vacios lo cual será equivalente al número de hijos
                estadoActual=nodo.data[:]    
                if estadoActual[j]==0:#Si la casilla está vacía
                    estadoActual[j]=operadoresDisponibles[i]#Entonces se aplica el operador
                    hijo=Node(estadoActual)#Se crea el nuevo nodo, con el operador aplicado
                    nodo.insertNode(hijo)#Se inserta el nodo como hijo
                else:
                    pass
        for i in range(len(nodo.hijos)):
            operadorRaiz(nodo.hijos[i])#Repetir este procedimiento para cada uno de los hijos
            
            """
            Implementar BFS para verificar la integridad del arbol 
            Finalmente implementar lo de la ruta solución
 
 
            """

    
    

print ("Iniciando creación del árbol")
Raiz=Node(INITIAL_STATE)
operadorRaiz(Raiz)
Raiz.showNodeStatus()
Raiz.recorrerArbol()


