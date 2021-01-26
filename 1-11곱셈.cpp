#include <iostream>
#include <string>
#include <cstdlib>

#define length 3
#define zero '0'

using namespace std;

int main(){
	string  A, B;
	int *res = new int(length);

	cin >> A >> B;
	

	// 계산부
	for(int i = 0; i < B.size(); i++){
		res[i] = int(atoi(A.c_str())) * ( (int)B[i]-(int)zero ); 
	}
	
	// 출력부
	for(int i = B.size()-1; i >= 0 ; i--){
		cout << res[i] << endl;
	}
	cout << res[0]*100 + res[1]*10 + res[2] << endl;
	
	return 0;
}


