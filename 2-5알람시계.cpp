#include <iostream>

using namespace std;

int main(){
	int h, m;
	cin >> h >> m;

	if(m>=45){	m = m-45;}
	else if(h==0){	h=23; m=60+(m-45);}
	else{	h--; m=60+(m-45);}
	
	cout << h << " " << m << endl;

	return 0;
}
