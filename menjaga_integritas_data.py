import os 

def simpan_data_umur():
    data_umur = {}
    print()
    print("=" * 40)
    print("input dan simpan data umur")
    print("=" * 40)
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data Umur")
        print("2. Lihat Data")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Pilihan Anda (1-3): "))
            
            if pilihan == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                nama = input("Masukkan nama: ").strip()
                if not nama:
                    print("Error: Nama tidak boleh kosong!")
                    continue
                try:
                    umur = int(input("Masukkan umur: "))
                    
                    if umur <= 0:
                        print("Error: Umur harus lebih dari 0")
                    else:
                        data_umur[nama] = umur
                        print(f"Data {nama} berhasil disimpan!")
                        input("\nTekan Enter untuk kembali ke menu utama...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                except ValueError:  
                    print("Error: Umur harus berupa angka!")
                    input("Tekan Enter untuk kembali ke tampilan awal...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            
            elif pilihan == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nData Tersimpan:")
                for nama, umur in data_umur.items():
                    print(f"{nama}: {umur} tahun")
                
                if not data_umur:
                    print("Belum ada data tersimpan")
                    input("\nTekan Enter untuk kembali ke menu utama...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            
            elif pilihan == 3:
                print("Program selesai. Sampai jumpa!")
                break  
                
            else:
                print("Error: Pilihan harus antara 1-3")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                
        except ValueError:
            print("Error: Masukkan angka untuk pilihan menu!")
            input("Tekan Enter untuk melanjutkan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input("Tekan Enter untuk melanjutkan...")
            os.system('cls' if os.name == 'nt' else 'clear')

simpan_data_umur()