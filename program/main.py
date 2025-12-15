import time
from multiprocessing import Process
import os
import threading

def islem_yap(sayi):
    print(f"İşlemci: {os.getpid()} - Sayı: {sayi}, Kare: {sayi * sayi}")
    time.sleep(2) 

def kare_hesapla(sayi):
    print(f"Hesaplanıyor (Thread/Process ID: {threading.get_ident()}): {sayi} -> {sayi * sayi}")
    time.sleep(1)

def amdahl():
    try:
        seri_islem = float(input("Seri gerçekleştirilecek işlem oranı yüzde kaçtır? "))
        if seri_islem <= 0 or seri_islem >= 100:
            print("Geçersiz değer girdiniz.")
            return
        seri_islem = seri_islem / 100
        cekirdek_sayisi = int(input("Kullanılacak çekirdek sayısı nedir? "))
        if cekirdek_sayisi < 1:
            print("Geçersiz değer girdiniz.")
            return
        hizlanma = 1 / (seri_islem + ((1 - seri_islem) / cekirdek_sayisi))
        print("Seri işlem oranı: ", seri_islem)
        print("Paralel işlem oranı: ", 1 - seri_islem)     
        print("Hızlanma oranı: ", hizlanma)
        if hizlanma <= 1:
            print("Bu işlemden verimlilik elde edilememiştir.")
    except ValueError:
        print("Lütfen sayısal bir değer girin.")

def multiprogram():
    def program1():
        for i in range(5):
            print(f"Program 1 çalışıyor: {i}")
            time.sleep(1)

    def program2():
        for i in range(5):
            print(f"Program 2 çalışıyor: {i}")
            time.sleep(1)

    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Tüm programlar tamamlandı!")

def multiprocessing():
    print("Çoklu İşlemci (Multiprocessing) Başlıyor...\n")
    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    for sayi in sayilar:
        islem = Process(target=islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()

    for islem in islemler:
        islem.join()
    print("\nTüm İşlemler Tamamlandı!")

def multi_program_process():
    def coklu_programlama():
        sayilar = [1, 2, 3, 4, 5]
        print("Çoklu Programlama Başladı (Thread)...\n")
        threads =[]
        for sayi in sayilar:
            t = threading.Thread(target=kare_hesapla, args=(sayi,))
            threads.append(t)
            t.start()
    
        for t in threads:
            t.join()
        print("\nÇoklu Programlama Tamamlandı!")

    def coklu_islemci():
        sayilar = [1, 2, 3, 4, 5]
        print("\nÇoklu İşlemci Başladı (Process)...\n")
        processes =[]
        for sayi in sayilar:
            p = Process(target=kare_hesapla, args=(sayi,))
            processes.append(p)
            p.start()
    
        for p in processes:
            p.join()
        print("\nÇoklu İşlemci Tamamlandı!")

    coklu_programlama()
    coklu_islemci()

if __name__ == "__main__":
    secim = input("YAPILACAK İŞLEMİ SEÇİN \nAMDAHL HESABI - 1\nÇOKLU PROGRAMLAMA - 2\nÇOKLU İŞLEMCİ - 3\nÇOKLU PROGRAMLAMA VE İŞLEMCİ - 4\n")
    if secim == "1":
        amdahl()
    elif secim == "2":
        multiprogram()
    elif secim == "3":
        multiprocessing()
    elif secim == "4":
        multi_program_process()
    else:
        print("YANLIŞ GİRDİ")
    os.system("pause")