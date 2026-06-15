# ===========================# ============================================
#   APLIKASI MANAJEMEN NILAI MAHASISWA
# ============================================

# LIST penyimpanan data mahasiswa [nama, nilai]
data_mahasiswa = [
    ["Zahra",    85],
    ["Citra",    78],
    ["Edlwis",   90],
    ["Rinjani",  72],
    ["Rembulan", 88]
]

# ── Fungsi cetak tabel ──────────────────────
def tampilkan_data():
    print("\n" + "-" * 38)
    print(f"  {'NO':<4} {'NAMA':<20} {'NILAI':>5}")
    print("-" * 38)
    if not data_mahasiswa:
        print("  Data kosong.")
    for i, m in enumerate(data_mahasiswa, 1):   # enumerate → buat nomor urut otomatis
        print(f"  {i:<4} {m[0]:<20} {m[1]:>5}")
    print("-" * 38)

# ── Tambah data ─────────────────────────────
def tambah_data():
    nama  = input("Nama  : ").strip()
    nilai = int(input("Nilai : "))
    data_mahasiswa.append([nama, nilai])         # append → tambah elemen baru ke list
    print(f"[✓] '{nama}' ditambahkan.")

# ── Ubah data ───────────────────────────────
def ubah_data():
    tampilkan_data()
    i = int(input("Nomor yang diubah: ")) - 1
    data_mahasiswa[i][0] = input("Nama baru  : ").strip()   # akses list dengan index
    data_mahasiswa[i][1] = int(input("Nilai baru : "))
    print("[✓] Data diperbarui.")

# ── Hapus data ──────────────────────────────
def hapus_data():
    tampilkan_data()
    i = int(input("Nomor yang dihapus: ")) - 1
    nama = data_mahasiswa[i][0]
    data_mahasiswa.pop(i)                        # pop(index) → hapus elemen dari list
    print(f"[✓] '{nama}' dihapus.")

# ── Cari data ───────────────────────────────
def cari_data():
    kata = input("Cari nama: ").lower()
    # list comprehension → buat list baru dari elemen yang cocok
    hasil = [m for m in data_mahasiswa if kata in m[0].lower()]
    if hasil:
        for m in hasil:
            print(f"  → {m[0]} | Nilai: {m[1]}")
    else:
        print("Data tidak ditemukan.")

# ── Urutkan nilai tertinggi ─────────────────
def urutkan_data():
    # sorted() dengan key lambda → urutkan berdasarkan index [1] (nilai), descending
    terurut = sorted(data_mahasiswa, key=lambda m: m[1], reverse=True)
    print("\n--- PERINGKAT NILAI ---")
    for i, m in enumerate(terurut, 1):
        print(f"  {i}. {m[0]:<20} {m[1]}")

# ── Rata-rata nilai ─────────────────────────
def rata_rata():
    # sum + list comprehension → ambil semua nilai lalu jumlahkan
    avg = sum(m[1] for m in data_mahasiswa) / len(data_mahasiswa)
    print(f"Rata-rata nilai: {avg:.2f}")

# ── MENU UTAMA ──────────────────────────────
menu = {
    "1": ("Tampilkan Data",          tampilkan_data),
    "2": ("Tambah Data",             tambah_data),
    "3": ("Ubah Data",               ubah_data),
    "4": ("Hapus Data",              hapus_data),
    "5": ("Cari Data",               cari_data),
    "6": ("Urutkan Berdasarkan Nilai", urutkan_data),
    "7": ("Hitung Rata-rata",        rata_rata),
    "8": ("Keluar",                  None),
}

while True:
    print("\n" + "=" * 38)
    print("  APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("=" * 38)
    for k, (label, _) in menu.items():          # iterasi dictionary menu
        print(f"  {k}. {label}")
    pilihan = input("Pilih 1-8: ").strip()

    if pilihan == "8":
        print("Sampai jumpa!")
        break
    elif pilihan in menu:
        menu[pilihan][1]()                       # panggil fungsi dari dictionary
    else:
        print("[!] Pilihan tidak valid.")