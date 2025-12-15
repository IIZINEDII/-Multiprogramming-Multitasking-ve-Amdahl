# Multiprogramming-Multitasking-ve-Amdahl

Programın ilk seçeneği olan Amdahl Yasası basit bir hesaplama programıdır.
Seri işlemler ve çekirdek sayısındaki değişikliklerin programı ne kadar
hızlandıracağını hesaplamaya yarar.

İkinci seçenek Threadsler ile çoklu programlamadır.
Program-1 ve program-2 fonksiyonlarının threads 
kullanarak eş zamanlı çalıştırılmıştır.

Üçüncü şıkkımız Multiprocessing ile alakalıdır.
Her sayı için ayrı bir process oluşturularak hesaplamaların
paralel bir şekilde ayrı çekirdeklerde işlenmesi sağlandı.
os.getpid()'in her bir işlem için farklı kimlik belirlendiği
tespit edilebilir.

Son programımız Thread ve Processlerin karşılaştırılmasıdır.
Aynı işlemi hem Threads kullanarak hemde Multiprocess ile
işleyerek yöntemler arası farkı gösterilmiştir.
