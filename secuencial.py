import time
import numpy as np
from fibonacci import fibo

def vector_fibo():
    vector = np.full(144,33)
    for i in range(len((vector))):
        vector[i] = fibo(vector[i])

def measure_execution_time():
    tiempo_ejecucion = []
    for _ in range(5):
        tiempo_inicial = time.time()
        vector_fibo()
        tiempo_final = time.time()
        tiempo_ejecucion.append(tiempo_final - tiempo_inicial)
    
    tiempo_ejecucion.sort()
    tiempos = tiempo_ejecucion[1:-1]
    
    tiempo_total = sum(tiempos) / len(tiempos)
    return tiempo_total

tiempo_total_ejecuicion = measure_execution_time()
print(f"Tiempo promedio de ejecucion: {tiempo_total_ejecuicion} segundos")