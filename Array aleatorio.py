import multiprocessing
import random

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    a = [random.randint(1, 10) for _ in range(5)]
    b = [random.randint(1, 10) for _ in range(5)]
    c = multiprocessing.Array('i', 5)  # Shared array
    
    # Imprimir las listas generadas aleatoriamente
    print("Array aleatorio a:", a)
    print("Array aleatorio b:", b)

    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    # Imprimir la lista resultante
    print("Suma Paralelo c:", list(c))
