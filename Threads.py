from threading import Thread
from time import time
from fibonacci import fibo
import multiprocessing

class FiboWorker(Thread):
    def __init__(self, vec, start_index, end_index, tid):
        Thread.__init__(self)
        self.vec = vec
        self.start_index = start_index
        self.end_index = end_index
        self.tid = tid

    def run(self):
        for i in range(self.start_index, self.end_index):
            self.vec[i] = fibo(self.vec[i])

def calcular_tiempo_ejecuicion():
    num_cpus = multiprocessing.cpu_count() # CPUs disponibles
    vec = [33] * 144 # Vector inicializado con 33
    hilos = [] # Vector de hilos
    n = len(vec) // num_cpus

    ts = time() # se toma tiempo 
    for x in range(num_cpus): # Ciclo para crear trabajadores
        start_index = x * n
        end_index = (x + 1) * n if x != num_cpus - 1 else len(vec)
        worker = FiboWorker(vec, start_index, end_index, x)
        worker.start()
        hilos.append(worker)

    for x in range(num_cpus): # Ciclo para esperar por trabajadores
        hilos[x].join()

    return time() - ts

def main():
    tiempos_ejecucion = []
    for _ in range(5):
        tiempo_de_ejecucion = calcular_tiempo_ejecuicion()
        tiempos_ejecucion.append(tiempo_de_ejecucion)

    tiempos_ejecucion.sort()
    tiempos = tiempos_ejecucion[1:-1]  # Elimina el tiempo más alto y el más bajo

    tiempo_acumulado = sum(tiempos) / len(tiempos)
    print(f"Promedio de los tiempos de ejecución: {tiempo_acumulado}")

if __name__ == "__main__":
    main()