# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:28:14 2020
PÝTHON 3.X.X 
No dependencies needed
@author: Narváez Marqueda Ricardo André Sebast (RAM)
"""

INITIAL_STATE=[0,0,0,5,4] # Los ceros representan un espacio aún no ocupado
CONSTANTES=[1,2,3]# Números a colocar en las casillas desocupadas
rutaSol=[]
class Node:

    def __init__(self, data):#Declaración del nodo
        self.data = data #Data será la lista que contendrá el estatus actual de las casillas
        self.hijos=[] #Hijos será una lista dado que es un arbol no binario
        
    #Imprimir valor del nodo actual
    def printValue(self):
        print("Node Value",self.data)
        
    #Insertar un hijo    
    def insertNode(self,node):
        self.hijos.append(node)
        node.padre=self
    #Imprime el estatus general dado un nodo
    



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
            
        
def BFS(nodo,flag):
    if flag==False: #Si aún no se ha encontrado la solución, continuar iterando
        sumaVertical=nodo.data[0]+nodo.data[2]+nodo.data[4]#Comprobar que se cumpla la suma vertical del nodo actual
        sumaHorizontal=nodo.data[1]+nodo.data[2]+nodo.data[3]#Comprobar que se cumpla la suma horizontal del nodo actual
        if sumaHorizontal==9 and sumaVertical==9:#Si se cumplen ambas
            flag=True#No se itera más y se realiza la impresión recursiva de la ruta solución
            global rutaSol
            rutaSol=nodo.data[:]
            return nodo.data
        else:#En caso contrario
            for i in range (len(nodo.hijos)):#Seguir recorriendo los hijos
                if len(nodo.hijos)!=0:#Si el nodo no es una hoja
                    nodo.hijos[i].printValue()#imprimir su valor
            for i in range(len(nodo.hijos)): 
                    if flag==True:#Si aun no se ha encontrado una solución
                        pass
                    else:
                        BFS(nodo.hijos[i],flag=False) #Continuar recursivamente analizando los hijos siempre y cuando no sea una hoja, en ese caso
                                                    #Regresar un nivel y analaizar los nodos hermanos

        
    
def rutaSolucion(estadoSolu):
    global INITIAL_STATE
    for i in range(len(INITIAL_STATE)-2):
        print("Colocar ", estadoSolu[i]," En la casilla",i)

print ("Iniciando creación del árbol")
Raiz=Node(INITIAL_STATE)
print ("Aplicando operadores y realizando bitácora de desarrollo:")
operadorRaiz(Raiz)
print ("Buscando ruta solución:")
BFS(Raiz,0)
print("SOLUCIÓN ENCONTRADA, DETENIENDO PROCESO:\n",rutaSol)
rutaSolucion(rutaSol)



