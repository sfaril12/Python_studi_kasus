import getpass
import os

class ErrorValue(Exception):
    pass
users = {}

def Daftar():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print("\n=== MENU DAFTAR ===")
        username = input("Buat username: ")
        
        if username in users:
            print("Username sudah digunakan!")
            return
            
        password = getpass.getpass("Buat sandi: ")
        
        print("\nmasukan data pribadi")
        
        nama = input("\nNama lengkap: ")
        jenis_kelamin = input("Jenis kelamin (L/P): ")
        agama = input("Agama: ")
        
        while True:
            try:
                umur = int(input("Umur: "))
                if umur <= 0:
                    raise ErrorValue("Umur harus lebih dari 0")
                if not umur :
                    raise ErrorValue("anda tidak menginput umur")
                break
            except Exception as e:
                print(f"error : {e}")
            except ValueError:
                print("error : inputan harus berupa angka")
            except ErrorValue as e:
                print(f"Error: {e}")
        
        pekerjaan = input("Pekerjaan: ")
        
        users[username] = {
            'password': password, 
            'data': {
                'nama': nama,
                'jenis_kelamin': jenis_kelamin,
                'agama': agama,
                'umur': umur,
                'pekerjaan': pekerjaan
            }
        }
        print("\nPendaftaran berhasil!")
        input("tekan enter untuk melanjutkan...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print("\n=== MENU LOGIN ===")
        username = input("Username: ")
        password = getpass.getpass("Sandi: ")
        
        if username not in users:   
            raise ValueError("username atau sandi salah!")
        
        if users[username]['password'] != password:
            raise ValueError("username atau sandi salah")
        
        print("\nLogin berhasil! Berikut data Anda:")
        for key, value in users[username]['data'].items():
            print(f"{key.capitalize()}: {value}")
        input("\ntekan enter untuk kembali ke tampilan awal...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError as a:
        print(f"error : {a}")
        input("tekan enter untuk kembali ke tampilan awal....")
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("tekan enter untuk melanjutkan...")
        os.system('cls'  if os.name == 'nt' else 'clear')

def main():
    while True:
        try:
            print("\n=== APLIKASI DATA PRIBADI ===")
            print("1. Daftar")
            print("2. Login")
            print("3. Keluar")
            choice = int(input("Pilih menu (1/2/3): "))
            
            if choice == 1:
                Daftar()
            elif choice == 2:
                login()
            elif choice == 3:
                print("Program dihentikan.")
                break
            else:
                print("\nPilihan tidak valid!")
        
        except ValueError:
            print("\ninputan harus berupa angka")
            input("tekan enter untuk kembali....")
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"\nTerjadi kesalahan sistem: {e}")
            input("tekan enter untuk kembali....")
            os.system('cls' if os.name == 'nt' else 'clear')
main()