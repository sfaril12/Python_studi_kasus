import os

# Membuat class barang
class barang:
    def __init__(self,nama=None,harga=None,jumlah=None): # fungsi untuk kriteria barang
        
        # Variabel untuk mendefenisikan barang
        self._nama = nama
        self._harga = harga
        self._jumlah = jumlah
    def tampil_barang(self): # fungsi untuk tampil barang
        print(f"nama  barang : {self._nama}")
        print(f"harga barang : {self._harga}")
        print(f"jumlah barang : {self._jumlah}")
 
# Variabel global        
nama_barang = None
harga_barang = None
jml_barang = None
        
while True:    
    print ("=============================================")
    print ("SIMULASI MELIHAT HARGA TOTAL BARANG")
    print ("=============================================\n")

    print ("1. masukan barang")
    print ("2. cek harga total")
    print ("3. keluar")

    pilihan = int(input("masukan pilihan anda: "))
    os.system('cls' if os.name == 'nt' else 'clear') # system clear screen
    
    if pilihan == 1:
        print()
        print ("=============================================")
        print ("MASUKAN KRITERIA BARANG")
        print ("=============================================")
        nama_barang =  input("masukan nama barang   : ")
        harga_barang = int(input("masukan harga barang  : "))
        jml_barang =   int(input("masukan jumlah barang : "))
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    if pilihan == 2:
        print()
        print ("=============================================")
        print ("MELIHAT KRITERIA BARANG")
        print ("=============================================")
        ket = barang(nama_barang,harga_barang,jml_barang) # objek dari class barang
        ket.tampil_barang()
        print("total harga : ",ket._harga * ket._jumlah)
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    if pilihan == 3: 
        print()
        print ("=============================================")
        print("terima kasih sudah menggunakan layanan ini")
        print ("=============================================")
        break
    