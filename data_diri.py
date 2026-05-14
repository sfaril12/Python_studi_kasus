print("program meminta inputan minimal 3 tipe data")
print("===========================================")
print()

print("masukan identitas pegawai:\n")
nama = str(input("masukan nama anda: "))
umur = int(input("masukan umur anda: "))
bb = float(input("masukan berat badan anda: "))

print()
print("tampilan output beserta tipe datanya:")
print("=====================================")
print()

print(f"halo, jadi nama anda adalah {nama}, umur anda {umur} dan berat badan anda adalah {bb}")
print()

print(f"nama        : {nama} , tipe datanya : {type(nama)}")
print(f"umur        : {umur} , tipe datanya : {type(umur)}")
print(f"berat badan : {bb} , tipe datanya : {type(bb)}")

# pseudocode
"""
ALGORITMA ProgramInputDataDiri
DEKLARASI
   nama : string
   umur : integer
   bb : float

BEGIN
   // Menampilkan header program
   OUTPUT "program meminta inputan minimal 3 tipe data"
   OUTPUT "==============================="
   OUTPUT newline
   
   // Meminta input data dari user
   OUTPUT "masukan identitas pegawai:"
   OUTPUT newline
   
   INPUT "masukan nama anda: " → nama
   INPUT "masukan umur anda: " → umur
   INPUT "masukan berat badan anda: " → bb
   
   // Menampilkan hasil output
   OUTPUT newline
   OUTPUT "tampilan output beserta tipe datanya:"
   OUTPUT "==============================="
   OUTPUT newline
   
   // Menampilkan data yang diinput
   OUTPUT "halo, jadi nama anda adalah " + nama + ", umur anda " + umur + " dan berat badan anda adalah " + bb
   OUTPUT newline
   
   // Menampilkan tipe data masing-masing variabel
   OUTPUT "nama : " + nama + ", tipe datanya : " + TYPE(nama)
   OUTPUT "umur : " + umur + ", tipe datanya : " + TYPE(umur)
   OUTPUT "berat badan : " + bb + ", tipe datanya : " + TYPE(bb)
END 
"""