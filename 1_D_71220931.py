print("Ketik 1 untuk menghitung penjumlahan")
print("Ketik 2 untuk menghitung pengurangan")
print("Ketik 3 untuk menghitung perkalian")
print("Ketik 4 untuk menghitung pembagian")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus")
print("Ketik 6 untuk menghitung pemangkatan")
a = int(input("masukkan pilihan anda: "))
b = int(input("masukkan bilangan pertama: "))
c = int(input("masukkan bilangan kedua: "))
if a == 1 :
    jumlah = b + c
    print("hasil dari",b,"dijumlahkan dengan",c,"adalah",jumlah)
elif a == 2:
    jumlah = b - c
    print("hasil dari",b,"dikurangi dengan",c,"adalah",jumlah)
elif a == 3 :
    jumlah = b * c
    print("hasil dari",b,"dikali dengan",c,"adalah",jumlah)
elif a == 4 :
    jumlah = b/c
    print("hasil dari",b,"dibagi dengan",c,"adalah",jumlah)
elif a == 5 :
    jumlah = b%c
    print("hasil dari",b,"modulo dari",c,"adalah",jumlah)
elif a == 6 :
    jumlah = b**c
    print("hasil dari",b,"pangkat dengan",c,"adalah",jumlah)
    