#include <iostream>

using namespace std;

int main(){
	int year;
	bool res;
	cin >> year;

	res = ((year%4==0) ? (!(year%100==0) ? 1 : 0 ) : 0) || (year%400==0);

	cout << res << endl;

	return 0;

}
