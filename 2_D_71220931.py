pertama = input("masukkan nama pemain pertama: ")
kedua = input("masukkan nama pemain kedua: ")
ketiga = input("masukkan nama pemain ketiga: ")
i1 = int(input("masukkan jumlah kartu pemain pertama: "))
i2 = int(input("masukkan jumlah kartu pemain kedua: "))
i3 = int(input("masukkan jumlah kartu pemain ketiga: "))
if (i1> i2 and i3):
    print(pertama, "menang dengan jumlah kartu sebanyak", i1)
elif (i2>i1 and i3):
    print(kedua, "menang dengan jumlah kartu sebanyak", i2)
elif (i3>i1 and i2):
    print(ketiga, "menang dengan jumlah kartu sebanyak", i3)
elif (i1>21):
    print("jumlah kartu yang dimiliki melebihi batas")
elif (i2>21):
    print("jumlah kartu yang dimiliki melebihi batas")
elif (i3>21):
    print("jumlah kartu yang dimiliki melebihi batas")

