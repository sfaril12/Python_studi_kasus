#definisi  
class pistol :
    merek = "colt peacemaker" #atribut class (default)
    kaliber = None
    jml_peluru = None
    
#membuat objek dari class pistol
pistol_jon = pistol()
pistol_jon.jml_peluru = 10

# perulangan untuk mensimulasikan penembakan sampai peluru habis
for i in range (10, -1, -1):
    if pistol_jon.jml_peluru == 0 : 
        print("peluruh habis")
        break
        
    else:
        print("peluru sekarang " ,pistol_jon.jml_peluru)
        print("senjata ditembakkan")
        print()
        pistol_jon.jml_peluru -= 1
        
        
    