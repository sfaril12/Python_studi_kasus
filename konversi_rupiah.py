print("Program Konversi Rupiah ke Dollar, yen, yuan")
print("=================================")

kursdollar = 16000
kursyen = 100
kursyuan = 2000


while True:
    try:
        print()
        rupiah = int(input("Masukkan jumlah Rupiah (bilangan bulat positif): "))
        if rupiah > 0:
            break
        else:
            print("Masukkan bilangan bulat positif!")
    except ValueError:
        print("Masukkan harus bilangan bulat!")

def dollar(rupiah):
    dollar = (rupiah / kursdollar)
    return dollar
def yen(rupiah):
    yen = (rupiah / kursyen)
    return yen
def yuan(rupiah):
    yuan = (rupiah / kursyuan)
    return yuan

print(f"\nHasil Konversi:")
print(f"1 konversi ke dollar : Rp {rupiah:,} = ${(dollar(rupiah))} dollar")
print(f"2 konversi ke yen    : Rp {rupiah:,} = ¥{(yen(rupiah))} yen")
print(f"3 konversi ke yuan   : Rp {rupiah:,} = ¥{(yen(rupiah))} yuan")

#pseudocode
"""
PROGRAM KonversiRupiahKeMataUangAsing
BEGIN
    // Inisialisasi kurs mata uang
    SET kurs_dollar = 16000
    SET kurs_yen = 100
    SET kurs_yuan = 2000
    
    // Tampilkan header program
    PRINT "Program Konversi Rupiah ke Dollar, yen, yuan"
    PRINT "================================="
    
    // Input data dengan validasi
    WHILE TRUE
        TRY
            PRINT (baris kosong)
            INPUT rupiah_dengan_pesan "Masukkan jumlah Rupiah (bilangan bulat positif): "
            
            IF rupiah > 0 THEN
                BREAK  // Keluar dari loop jika input valid
            ELSE
                PRINT "Masukkan bilangan bulat positif!"
            END IF
        CATCH ValueError
            PRINT "Masukkan harus bilangan bulat!"
        END TRY
    END WHILE
    
    // Fungsi konversi mata uang
    FUNCTION konversi_ke_dollar(rupiah)
        RETURN rupiah / kurs_dollar
    END FUNCTION
    
    FUNCTION konversi_ke_yen(rupiah)
        RETURN rupiah / kurs_yen
    END FUNCTION
    
    FUNCTION konversi_ke_yuan(rupiah)
        RETURN rupiah / kurs_yuan
    END FUNCTION
    
    // Tampilkan hasil konversi
    PRINT (baris kosong)
    PRINT "Hasil Konversi:"
    PRINT "1 konversi ke dollar : Rp " + FORMAT_NUMBER(rupiah) + " = $" + konversi_ke_dollar(rupiah) + " dollar"
    PRINT "2 konversi ke yen    : Rp " + FORMAT_NUMBER(rupiah) + " = ¥" + konversi_ke_yen(rupiah) + " yen"
    PRINT "3 konversi ke yuan   : Rp " + FORMAT_NUMBER(rupiah) + " = ¥" + konversi_ke_yuan(rupiah) + " yuan"
END PROGRAM
"""