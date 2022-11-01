import orbita_cy
import orbita_py
import time

ini_time = time.time()
orbita_cy.main()
fin_time = time.time()

time_cython = fin_time-ini_time

ini_time = time.time()
orbita_py.main()
fin_time = time.time()

time_python = fin_time-ini_time

print("Cython Time: ",time_cython)
print("Python Time: ",time_python)

print("Cython es: ",time_python/time_cython," mas rapido")