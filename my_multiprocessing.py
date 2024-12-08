from multiprocessing import Process
import os 
import time

def islem_yap(sayi):
    print(f"İşlemci: {os.getpid()} - Sayi: {sayi}, Kare: {sayi * sayi}")
    time.sleep(2)

if __name__ == "__main__":
    print("Çoklu İŞlemci (Multiprocessing) Başlıyor...\n")

    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    for sayi in sayilar:
        islem = Process(target = islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()

    for islem in islemler:
        islem.join()
    
    print("\nTüm İşlemler Tamamlandı!")