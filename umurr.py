# nama yang benar
nama_benar = "citra"

# validasi nama
while True:
    nama = input("Masukkan nama anda: ")
    if nama == nama_benar:
        print("Nama benar, lanjut program...\n")
        break
    else:
        print("Silahkan coba lagi")

# input angka
angka = int(input("Masukkan angka (1-10): "))

# tabel perkalian
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")