import multiprocessing
import random
import time

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]

if __name__ == "__main__":
    # Generar arrays aleatorios
    a = [random.randint(1, 10) for _ in range(1000)]
    b = [random.randint(1, 10) for _ in range(1000)]
    
    # Suma ordinaria
    start_time = time.time()
    c_ordinaria = [a[i] + b[i] for i in range(1000)]
    end_time = time.time()
    print("Tiempo de ejecución de la suma ordinaria:", end_time - start_time, "segundos")
    
    # Suma paralela
    start_time = time.time()
    c = multiprocessing.Array('i', 500)  # Array compartido
    
    processes = []
    for tid in range(500):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    end_time = time.time()
    print("Tiempo de ejecución de la suma paralela:", end_time - start_time, "segundos")
