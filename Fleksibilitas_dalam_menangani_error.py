import os 

class ValueAgeError(Exception):
    pass

def validasi_umur(umur):
    """Fungsi validasi umur dengan mekanisme exception"""
    if umur < 20:
        raise ValueAgeError("Umur pendaftar harus minimal 20 tahun")
    elif umur > 30:
        raise ValueAgeError("Umur pendaftar harus maksimal 30 tahun")
    elif umur <= 0:
        raise ValueError("anda menginput umur di bawah 0 (anda belum lahir)")

def data_pendaftar():
    data_umur = {}
    print()
    print("=" * 60)
    print("Input dan Simpan Data pendaftar PT. Morowali (20-30 tahun)")
    print("=" * 60)
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data pendaftar")
        print("2. Lihat Data pendaftar")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Pilihan Anda (1-3): "))
            
            if pilihan == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                nama = input("Masukkan nama: ").strip()
                if not nama:
                    print("Error: Nama tidak boleh kosong!")
                    input("\nTekan Enter untuk kembali...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                
                try:
                    umur = int(input("Masukkan umur: "))
                    validasi_umur(umur)
                    
                    data_umur[nama] = umur
                    print(f"Data {nama} berhasil disimpan!")
                    
                except ValueAgeError as e:
                    print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")
                
                input("\nTekan Enter untuk kembali...")
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif pilihan == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nData Tersimpan:")
                if not data_umur:
                    print("Belum ada data tersimpan")
                else:
                    for nama, umur in data_umur.items():
                        print(f"{nama}: {umur} tahun")
                
                input("\nTekan Enter untuk kembali...")
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif pilihan == 3:
                print("Program selesai. Sampai jumpa!")
                break  
                
            else:
                print("Error: Pilihan harus antara 1-3")
                input("\nTekan Enter untuk kembali...")
                os.system('cls' if os.name == 'nt' else 'clear')
                
        except ValueError:
            print("Error: Masukkan angka untuk pilihan menu!")
            input("\nTekan Enter untuk kembali...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input("\nTekan Enter untuk kembali...")
            os.system('cls' if os.name == 'nt' else 'clear')
data_pendaftar()