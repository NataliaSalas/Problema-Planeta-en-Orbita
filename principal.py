"""
La idea principal es crear un ".csv" con la toma de timpos 
"""
import orbita_cy
import orbita_py
import time
    

#Se inicializa el planeta para Py
tierraPy = orbita_py.Planet()
tierraPy.x=100*10**3
tierraPy.y=300*10**3
tierraPy.z=700*10**3
tierraPy.vx=2.00*10**3
tierraPy.vy=29.87*10**3
tierraPy.vz=0.034*10**3
tierraPy.m=5.97424*10**24

#Se inicializa el planeta para Cy
tierraCy = orbita_cy.Planet()
tierraCy.x=100*10**3
tierraCy.y=300*10**3
tierraCy.z=700*10**3
tierraCy.vx=2.00*10**3
tierraCy.vy=29.87*10**3
tierraCy.vz=0.034*10**3
tierraCy.m=5.97424*10**24

#Se consideran las otras variables 
time_span = 400
n_steps = 6000000

#Se crea formato para la impresion sobre el fichero
formato_datos = "{:.5f},{:.5f},{:.5f}\n"
#Definición de experimentos 
#Reducción ruido Gaussiano
for i in range(20):
    #Toma de tiempos para Py
    ini_time = time.time()
    orbita_py.step_time(tierraPy, time_span, n_steps)
    fin_time = time.time()
    time_python = fin_time-ini_time

    #Toma de tiempos para Cy
    ini_time = time.time()
    orbita_cy.step_time(tierraCy, time_span, n_steps)
    fin_time = time.time()
    time_cython = fin_time-ini_time

    with open("planeta.csv","a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython, time_python/time_cython))
    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," mas rapido")