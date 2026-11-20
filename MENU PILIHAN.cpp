#include <iostream>
using namespace std;

int main () {
	int pilihan;
	
	cout << "==== MENU PILIHAN ====" << endl;
	
	cout << "1. Air Mineral" << endl;
	cout << "2. Es Teh" << endl;
	cout << "3. Jus Jeruk" << endl;
	cout << "4. Kopi" << endl;
	cout << "5. Susu" << endl;
	
	cout << "Pilihan Minuman (1-5): ";
	cin >> pilihan;
	
	switch (pilihan){
		case 1: 
			 cout << "Pilihan anda adalah Air Mineral "  ;
			 break; // tidak lanjut meng eksekusi pilihan ke dua
 		case 2: 
			 cout << "Pilihan anda adalah Es Teh " ;
			 break;
        case 3: 
			 cout << "Pilihan anda adalah Jus Jeruk " ;
			 break;
		case 4: 
			 cout << "Pilihan anda adalah Kopi "  ;
			 break;
		case 5: 
			 cout << "Pilihan anda adalah Susu "  ;
			 break;
	    default :
	    	cout << "PILIHAN TIDAK VALID, COBA LAGI" ;
	
	}
	
	
 
}
