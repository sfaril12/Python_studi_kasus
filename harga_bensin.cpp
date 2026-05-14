# include <iostream>
using namespace std;
int main (){
    cout<< "berikut adalah jenis dan harga bensin: "<< endl;
    cout << "1. pertalite 10000/liter"<<endl;
    cout << "2. pertamax 15000/liter"<<endl;
    cout << "3. dexlite 20000/liter"<<endl;
    int pilih;
    cout << "masukan pilihan anda: ";
    cin>> pilih;
    int jml_ltr, hrg_akr;
    cout <<"anda beli berapa liter: ";
    cin >> jml_ltr;
    if (pilih == 1){
        hrg_akr = jml_ltr * 10000 ;

        cout << "anda harus membayar "<< hrg_akr << endl;
    }
    else if (pilih == 2){
        hrg_akr = jml_ltr * 15000 ;

        cout << "anda harus membayar "<< hrg_akr << endl;
    }
    else if (pilih == 3){
        hrg_akr = jml_ltr * 20000 ;

        cout << "anda harus membayar "<< hrg_akr << endl;
    }
    else{
        cout<< "inputan tidak valid";
    }
}
