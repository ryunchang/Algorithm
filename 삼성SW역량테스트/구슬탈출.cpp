#include <iostream>
#include <string>

using namespace std;

void checknode(char boardi[][]){
	for(int i=0; i<4; i++){
		if promising(board, i) {
			
		
	}

}

bool promising(char board, int i){
	switch(i){
		case '0':						// 위로 기울었을 때
			int red_N, red_M, blue_N, blue_M;
			for(int i=1; i<N-1; i++)
				for(int j=1; j<M-1; j++)
					if(board[N][M] == 'R') red_N, red_M = N, M;
					if(board[N][M] == 'B') blue_N, blue_M = N, M;
			while(true){
				if(board[red_N+1][red_M] == ".")  

				board[]
		case '1':

		case '2':

		case '3':

		default:
			return false;
}}



int main(){
	int N, M;
	cin >> N >> M;

	if(!(N>=3 && N<=10 && M>=3 && M<=10)){
		return 0;
	}

	char board[N][M];

	for(int i=0; i<N; i++)
		for(int j=0; j<M; j++)
			cin >> board[i][j];

	
	
	
	return 0;
}
