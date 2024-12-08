import time

def program1():
    for i in range(5):
        print(f"Program 1 çalişiyor: {i}")
        time.sleep(1)

def program2():
    for i in range(5):
        print(f"Program 2 çalişiyor: {i}\n")
        time.sleep(1)

if __name__ == "__main__":
    import threading

    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Tüm programlar tamamlandı!")