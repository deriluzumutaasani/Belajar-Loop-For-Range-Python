#Buatlah program yang menerima input sebuah bilangan bulat n kemudian mencetak segitigasiku-siku dengan n baris

n = int(input("Masukkan sebuah bilangan bulat: "))
for i in range(n): #perulangan sejumlah barisyang diinginkan
    for k in range(n-i-1):
        print("  ", end="")
    for j in range(i+1):#perulangan sejumlah bintang yang dicetak
        print("* ", end="")#agar tidak ganti baris
    print()#ganti baris sesuai i
