#include <iostream>

using namespace std;

int main(){
	int A, B, C;

	cin >> A >> B >> C;
	
	if(!(A >= 2 && B <= 10000 && C <= 10000)){
		cout << "잘못된 값을 입력하였습니다." << endl;
		return 0;
	}

	cout << (A+B)%C << endl << ((A%C)+(B%C))%C << endl
		<< (A*B)%C << endl << ((A%C)*(B%C))%C  << endl;

	return 0;
}

