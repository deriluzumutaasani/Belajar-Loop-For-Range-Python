#For digunakan untuk melakukan eksekusi secara berulang berdasarkan urutan nilai tertentu
for i in range(3):
    print("Belajar perulangan")

#Range dengan satu parameter range(a) menghasilkan urutan nilai dari 0 s.d a-1
for i in range(3):
    print(f"ini adalah perulangan ke-{i}")

#Range dengan dua parameter range (a,b) menghasilkan nilai dari a s.d b-1
for i in range(7,10):
    print(f"ini dalah perulangan ke-{i}")

#Range dengan tiga parameter range (a,b,c) menghasilkan urutan nilai dari a s.d d b-1,lompatan/step senilai c
for i in range(2,12,3):
    print(f"ini adalah perulangan ke-{i}")