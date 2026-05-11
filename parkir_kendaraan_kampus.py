from datetime import datetime
import os
class Kendaraan:
    
    def __init__(self, plat, jenis):
        self.plat = plat
        self.jenis = jenis
        self.waktu_masuk = datetime.now()

    def tampilkan_data(self):
        print("Plat Nomor :", self.plat)
        print("Jenis      :", self.jenis)
        print("Masuk Jam  :", self.waktu_masuk.strftime("%H:%M:%S"))
        
    def hitung_biaya(self):
        waktu_keluar = datetime.now()
        lama_parkir = (waktu_keluar - self.waktu_masuk).seconds // 3600

        if lama_parkir == 0:
            lama_parkir = 1

        if self.jenis.lower() == "motor":
            biaya = lama_parkir * 2000
        else:
            biaya = lama_parkir * 5000

        return biaya

class Parkiran:

    def __init__(self):
        self.daftar_kendaraan = []

    def kendaraan_masuk(self):
        plat = input("Masukkan plat nomor : ")
        jenis = input("Jenis kendaraan (Motor/Mobil) : ")

        kendaraan = Kendaraan(plat, jenis)
        self.daftar_kendaraan.append(kendaraan)

        print("Kendaraan berhasil masuk parkiran!")

    def tampilkan_kendaraan(self):

        if len(self.daftar_kendaraan) == 0:
            print("Parkiran kosong")
        else:
            print("\n=== DAFTAR KENDARAAN ===")
            for kendaraan in self.daftar_kendaraan:
                kendaraan.tampilkan_data()
                print("-------------------")

    def kendaraan_keluar(self):
        plat = input("Masukkan plat kendaraan keluar : ")

        for kendaraan in self.daftar_kendaraan:
            if kendaraan.plat == plat:

                biaya = kendaraan.hitung_biaya()

                print("Kendaraan ditemukan")
                print("Total biaya parkir : Rp", biaya)

                self.daftar_kendaraan.remove(kendaraan)
                return

        print("Kendaraan tidak ditemukan")

parkiran = Parkiran()

while True:

    print("\n===== SISTEM PARKIR =====")
    print("1. Kendaraan Masuk")
    print("2. Tampilkan Kendaraan")
    print("3. Kendaraan Keluar")
    print("4. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        parkiran.kendaraan_masuk()
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif pilih == "2":
        parkiran.tampilkan_kendaraan()
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif pilih == "3":
        parkiran.kendaraan_keluar()
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif pilih == "4":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")
