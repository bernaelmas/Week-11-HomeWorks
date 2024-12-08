import multiprocessing
import time

def amdahl_law(p: float, n: int) -> float: 
   
    if not (0 <= p <= 1):
        raise ValueError("Paralelleştirilebilir oran (p) 0 ile 1 arasinda olmalidir.")
    if n <= 0:
        raise ValueError("İşlemci sayisi (n) pozitif bir tamsayi olmalidir.")
    
    speedup = 1 / ((1 - p) + (p / n))
    return speedup

def simulate_process(task_name: str, duration: int):
    
    for i in range(duration):
        print(f"{task_name} çalişiyor: {i + 1}. saniye")
        time.sleep(1)

if __name__ == "__main__":
    print("Amdahl Yasasi Hesaplayici")
    p = float(input("Paralelleştirilebilen kisim oranini (0-1 arasinda) girin: "))
    n = int(input("İşlemci/çekirdek sayisini girin: "))
    
    speedup = amdahl_law(p, n)
    print(f"Hizlanma (Speedup): {speedup:.2f}\n")
    
    print("Multiprocessing Simülasyonu Başlatiliyor...")
    
    process1 = multiprocessing.Process(target=simulate_process, args=("Görev 1", 5))
    process2 = multiprocessing.Process(target=simulate_process, args=("Görev 2", 5))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print("Tüm İşlemler Tamamlandi!")
