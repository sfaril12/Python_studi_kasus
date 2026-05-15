def simpan_data_umur():
    data_umur = {}
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data Umur")
        print("2. Lihat Data")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Pilihan Anda (1-3): "))
            
            if pilihan == 1:
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
                except ValueError:
                    print("Error: Umur harus berupa angka!")
            
            elif pilihan == 2:
                print("\nData Tersimpan:")
                for nama, umur in data_umur.items():
                    print(f"{nama}: {umur} tahun")
                if not data_umur:
                    print("Belum ada data tersimpan")
            
            elif pilihan == 3:
                print("Program selesai. Sampai jumpa!")
                break
                
            else:
                print("Error: Pilihan harus antara 1-3")
                
        except ValueError:
            print("Error: Masukkan angka untuk pilihan menu!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

simpan_data_umur()