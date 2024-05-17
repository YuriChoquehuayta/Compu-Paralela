import multiprocessing
import random

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    # Generar arrays aleatorios
    a = [random.randint(1, 10) for _ in range(5)]
    b = [random.randint(1, 10) for _ in range(5)]
    print("Array aleatorio a:", a)
    print("Array aleatorio b:", b)
    
    # Suma ordinaria
    c_ordinaria = [a[i] + b[i] for i in range(5)]
    print("Suma ordinaria:", c_ordinaria)
    
    # Suma paralela
    c = multiprocessing.Array('i', 5)  # Array compartido
    
    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print("Suma paralela:", list(c))
