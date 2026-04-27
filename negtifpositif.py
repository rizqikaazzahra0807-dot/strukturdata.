while True:
    angka = float(input("Masukkan angka: "))
    
    if angka >= 0:
        break
    else:
        print("Harus positif!")

print(f"Terima kasih! Kamu memasukkan angka: {angka}")