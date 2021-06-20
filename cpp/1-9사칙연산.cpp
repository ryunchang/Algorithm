#include <iostream>

using namespace std;

int main(){
	int A, B;

	cin >> A >> B;
	
	if(!(A>=1 && B<=10000)){
		cout << "잘못된 값을 입력하였습니다." << endl;
		return 0;
	}

	cout << A+B << endl << A-B << endl
		<< A*B << endl << A/B << endl << A%B << endl;

	return 0;
}

	
