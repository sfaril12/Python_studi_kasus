def hitung_kembalian():
    print("=== Program Menghitung Uang Kembalian ===")
    try:
        total_harga = float(input("Masukkan total harga belanja (Rp): "))
        uang_dibayar = float(input("Masukkan jumlah uang yang dibayarkan (Rp): "))
    except ValueError:
        print("Error: Inputan harus berupa angka")
        return  # Keluar fungsi jika input invalid
    except ZeroDivisionError:  # Tidak relevan di sini, dihapus lebih baik
        print("Error: Tidak boleh pembagian nol")
        return

    if uang_dibayar < total_harga:
        print("Uang yang dibayarkan tidak cukup. Harap bayar sesuai total harga.")
    else:
        kembalian = uang_dibayar - total_harga
        print(f"Total kembalian: Rp {kembalian:.2f}")

        # Detail kembalian menggunakan pecahan uang
        print("\n=== Detail Pecahan Uang Kembalian ===")
        pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500]
        for p in pecahan:
            if kembalian >= p:
                jumlah = int(kembalian // p)
                kembalian %= p  # Update sisa kembalian
                print(f"Pecahan Rp {p}: {jumlah} lembar/koin")

        # Sisa kembalian kecil (<500)
        if kembalian > 0:
            print(f"Sisa kembalian kurang dari Rp 500: Rp {kembalian:.2f}")

# Panggil fungsi
hitung_kembalian()