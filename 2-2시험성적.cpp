#include <iostream>

using namespace std;

int main(){
	int A;
	char result;
	cin >> A;

	result = (A >= 90) ? 65 : ((A>=80) ? 66 : ((A>=70) ? 67 : ((A>=60) ? 68 : 70)));
	cout << result << endl;

	return 0;
}
	
