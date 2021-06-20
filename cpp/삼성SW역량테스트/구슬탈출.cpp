#include <iostream>
#include <string>

using namespace std;

void checknode(char board){
	for(int i=0; i<4; i++){
		if promising(board, i) {
			
		
	}

}

bool promising(char board, int i){
	switch(i){
		case '0':
			int red, blue;
			for(int i=0; i<N; i++)
				for(int j=0; j<M; j++)
					if(board[N][M] == 'R')
						red_n = N;
					if(board[N][M] == 'B')
						blue = N;

			while(true){
				if(board[red
				board[
		case '1':

		case '2':

		case '3':

		default:
			return false;
}



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
