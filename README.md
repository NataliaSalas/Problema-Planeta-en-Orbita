# ProblemaPlanetaenOrbita
<br>
<i><b>Autor:</b></i> Natalia Salas - 6º semestre
<br>
<i><b>Asignatura:</b></i> Parallel and Distributed Computing
<br>
<b>Ciencias de la computación e inteligencia artificial</b></i>

## Contenido
Para comprobar cuánto puede mejorar el rendimiento del código Python al utilizar Cython, se utilizó el problema Planeta en Orbita, los valores de la masa y velocidad del planeta Tierra fueron extraídos de Wikipedia. Para saber cuánto puede aumentar el rendimiento de Python cuando se utiliza Cython solamente se tiene que comparar el tiempo que tarda en ejecutarse en ambos lenguajes de programación.

- Para la resolución de este trabajo, se crearon los siguientes programas: 

> - orbita_cy.pyx: Se crea el programa que resuelve el problema del planeta en órbita en lenguaje cython
> - orbita_py.py: Se crea el programa que resuelve el problema del planeta en órbita en lenguaje python
> - principal.py: Se fusionan el programa de python y de cython y allí se calcula el tiempo de ejecución de cada uno 
> - setup.py: Lo convierte en un objeto compartido, es un fichero de comparación 

- En el archivo ProblemaPlanetaenOrbita.ipynb se encuentra el análisis y las gráficas del rendimiento cython/python
