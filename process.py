from fibonacci import fibo
from time import time
import multiprocessing

class FiboWorker(multiprocessing.Process):
    def __init__(self, vec, start_index, end_index, pid):
        multiprocessing.Process.__init__(self)
        self.vec = vec
        self.start_index = start_index
        self.end_index = end_index
        self._pid = pid

    def run(self):
        for i in range(self.start_index, self.end_index):
            self.vec[i] = fibo(self.vec[i])
        print(f"[{self._pid}] Proceso terminado")

def calculo_tiempos_ejecucion():
    num_cpus = multiprocessing.cpu_count()  # CPUs disponibles
    vec = multiprocessing.Array('i', [33] * 144)  # Vector inicializado con 33
    procesos = []  # Vector de procesos
    n = len(vec) // num_cpus

    ts = time()  # se toma tiempo 
    for x in range(num_cpus):  # Ciclo para crear trabajadores
        start_index = x * n
        end_index = (x + 1) * n if x != num_cpus - 1 else len(vec)
        worker = FiboWorker(vec, start_index, end_index, x)
        worker.start()
        procesos.append(worker)

    for x in range(num_cpus):  # Ciclo para esperar por trabajadores
        procesos[x].join()

    return time() - ts

def main():
    tiempos_ejecucion = []
    for _ in range(5):
        tiempo_de_ejecucion = calculo_tiempos_ejecucion()
        tiempos_ejecucion.append(tiempo_de_ejecucion)

    tiempos_ejecucion.sort()
    tiempos = tiempos_ejecucion[1:-1]  # Elimina el tiempo más alto y el más bajo

    tiempo_acumulado = sum(tiempos) / len(tiempos)
    print(f"Promedio de los tiempos de ejecución: {tiempo_acumulado}")

if __name__ == "__main__":
    main()