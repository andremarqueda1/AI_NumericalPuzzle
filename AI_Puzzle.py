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



def operadorRaiz(padre):
    for i in range(len(CONSTANTES)):#Operadores
        for j in range(padre.data.count(0)): #Contando el número de espacios vacios lo cual será equivalente al número de hijos
            temporalState=INITIAL_STATE[:]
            temporalState[j]=CONSTANTES[i]
            hijo=Node(temporalState)
            padre.insertNode(hijo)
            
def capas(nodo):
    
    
    pass


print ("Iniciando creación del árbol")
Raiz=Node(INITIAL_STATE)
operadorRaiz(Raiz)
Raiz.showNodeStatus()
Raiz.recorrerArbol()


