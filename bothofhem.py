from multiprocessing import Process
import threading
import time

def kare_hesapla(sayi):
    print(f"Hesaplaniyor (Thread/Process ID: {threading.get_ident()}): {sayi} -> {sayi * sayi}")
    time.sleep(1)

def coklu_programlama():
    sayilar = [1, 2, 3, 4, 5]
    print("Çoklu Porgramlama Başladi (Thread)...\n")
    threads = []
    for sayi in sayilar:
        t = threading.Thread(target=kare_hesapla, args=(sayi,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("\nÇoklu Programlama Tamamlandi!")

def coklu_islemci():
    sayilar = [1, 2, 3, 4, 5]
    print("Çoklu İşlemci Başladi (Process)...\n")
    processes = []
    for sayi in sayilar:
        p = Process(target=kare_hesapla, args=(sayi,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("\nÇoklu İşlemci Tamamlandi!")

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()