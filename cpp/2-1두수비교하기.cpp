#include <iostream>

using namespace std;

int main(){
	int A, B;
	cin >> A >> B;

	if(!(A>=-10000 && A<=10000 && B>=-10000 && B<=10000)){
		cout << "수 범위 오류" <<endl;
		return 0;
	}
	if(A>B) cout << ">" << endl;
	else if(A<B) cout << "<" << endl;
	else cout << "==" << endl;

	return 0;
}
