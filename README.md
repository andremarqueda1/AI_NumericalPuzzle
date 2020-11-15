# AI_NumericalPuzzle
Resolver el siguiente rompecabezas numérico por medio de una búsqueda ciega por amplitud.   

Los números (1,2,3) deben ser colocados una sola vez en una casilla y la suma Horizontal y Vertical debe resultar en 9.<br>
![Puzzle](https://github.com/andremarqueda1/AI_NumericalPuzzle/blob/main/Puzzle.png)


La búsqueda será realizada  por un programa que aplique los operadores para generarlos estados.  
Utilizar un lenguaje procedural (Python).   
El orden en que se crean los estados y el orden en que se revisan.  
Y al final dar la ruta de solución.

## Inteligencia Artificial

## ROMPECABEZAS NUMÉRICO

Integrante: Narváez Marqueda Ricardo André Sebastián
Número de cuenta 41705242-
Grupo 5
Fecha de ejecución: 12/11/
Fecha de entrega 26/11/
Profesora Dra. MARIA DEL CARMEN EDNA MARQUEZ MARQUEZ
Semestre 2021-


**Objetivos**
Resolver el siguiente rompecabezas numérico por medio de una búsqueda ciega por
amplitud.
_La suma Horizontal y Vertical debe resultar en 9_
● La búsqueda será realizada por un programa que ejecute los operadores para
generarlos estados.
● Utilizar un lenguaje procedural (Python).
● El orden en que se crean los estados y el orden en que se revisan.
● Y al final dar la ruta de solución.
Para el manejo del problema realizaremos una representación en forma de lista de la
siguiente manera (a motivo de no manejar matrices con espacios vacíos).
_Representación por A,B,C para los espacios en las columnas._


Esto en forma de lista sería de la siguiente manera:

### [A,B,C,5,4]

O bien, indexando la lista anterior:

### [<1>,<2>,<3>,5,4]

O bien en python:
nodo.data[0],nodo.data[1],nodo.data[2]...
Ahora bien una vez definido esto, podemos concretar que el caso de éxito es cuando las
siguientes ecuaciones se cumplan de manera satisfactoria:
_A_ + _C_ + 4 = 9 : _Suma Vertical
B_ + _C_ + 5 = 9 _Suma Horizontal_
Como sabemos que tenemos 3 elementos (3 números en este caso), tendremos los
siguientes operadores:
Colocar​ **1​** en [​ **A​** ]
Colocar ​ **1 ​** en [​ **B​** ]
Colocar ​ **1​** en [​ **C​** ]
Colocar ​ **2​** en [​ **A​** ]
Colocar ​ **2​** en [​ **B​** ]
...
Colocar ​ **3​** en [​ **C​** ]
Tal como se definió en la clase, el orden de los operadores puede ser tanto aleatorio,
como fijo para el desarrollo de la estructura árbol, y se tiene en consideración que una
vez aplicado un operador, éste no puede ser repetido la sucesión de nodos hijos, por
mencionar un ejemplo sencillo:
**Operador Colocar 3 en [B]**


Tanto la casilla B como el número 3 no podrán ser utilizados para los hijos, por lo que
solo nos quedarán los operadores: Colocar [1,2] en [A,C].
Al ser una búsqueda en amplitud los siguientes operadores a aplicar será regresar un
nivel anterior y aplicar el operador Colocar [1,2] en [A,C]. hasta terminar la capa actual
del árbol.
Solo por mostrar gráficamente lo que se debe de obtener teóricamente:
_Primer nivel del árbol al desarrollar la búsqueda ciega en amplitud.
Representación en forma de lista:
[_,_,_,5,4] → Raíz_

_- [3,_,_,5,4] → Hijos
- [_,3,_,5,4]
- [_,_,3,5,4]
- [1,_,_,5,4]
- [_,1,_,5,4]_
    _..._


**Implementación:**
Realicé un programa cuasi escalable (debido a que el tamaño del arreglo y las constantes
pueden ser modificadas):
La clase nodo la cual contendrá la bitácora de la aplicación de los operadores:
En ella encontraremos los métodos básicos de una estructura de tipo árbol tal como:
**La inicialización de la estructura__init__: ​** El cual dado que es un arbol no binario
(puede contener una o más ramas), por lo que tendrá una lista de referencia a memoria
respectivamente a los hijos.
**PrintValue: ​** Imprimirá en pantalla el estado actual del nodo que estemos recorriendo
**InsertNode: ​** El cual inserta un nodo por llamada
Más adelante tenemos la función operadorRaiz, el cual es el encargado de realizar la
operación de tomar las constantes disponibles y ubicarlas en las casillas. En este caso
opté por una implementación ordenada y bien definida, aunque si cambiamos
_operadoresDisponibles[i] por operadoresDisponibles[randomSel(0,2)] ​_ donde ​ _randomSel(0,2)_
tomará una constante aleatoria aún no utilizada en dicha capa, aleatorizando el proceso.


Una vez generada y bitacorizada la creación del arbol, podemos comenzar con el
recorrido a través de BFS.
Salida de ejecución del programa:


De acuerdo a la manera en que asigné las casillas y operadores, la solución gráficamente
se visualizará de la siguiente manera.
_Solución descrita por mi programa_

