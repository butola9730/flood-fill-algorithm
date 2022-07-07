# flood-fill-algorithm

#include<iostream>
using namespace std;
#define M 8
#define N 8
void fillColorAdj(char screen[][N], int x, int y, char oldColor, char color){

   if (x < 0 || x >= M || y < 0 || y >= N)
      return;
   if (screen[x][y] != oldColor)
      return;
   if (screen[x][y] == color)
      return;
   screen[x][y] = color;

   fillColorAdj(screen, x+1, y, oldColor, color);
   fillColorAdj(screen, x-1, y, oldColor, color);
   fillColorAdj(screen, x, y+1, oldColor, color);
   fillColorAdj(screen, x, y-1, oldColor, color);
}
void fillcolor(char screen[][N], int x, int y, char color){

   char oldColor = screen[x][y];
   if(oldColor==color) return;
   fillColorAdj(screen, x, y, oldColor, color);
}
int main(){

   char screen[M][N] = {{'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'},
      {'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'},
      {'W', 'B', 'B', 'W', 'W', 'B', 'W', 'W'},
      {'W', 'Y', 'Y', 'Y', 'Y', 'B', 'W', 'B'},
      {'B', 'W', 'W', 'Y', 'Y', 'B', 'W', 'B'},
      {'B', 'W', 'W', 'Y', 'Y', 'Y', 'Y', 'B'},
      {'W', 'B', 'W', 'W', 'W', 'Y', 'W', 'W'},
      {'W', 'W', 'B', 'B', 'W', 'Y', 'Y', 'W'},};
   int x = 5, y = 5;
   char color = 'R';

   cout<<"The initial screen cordinates are : \n";
   for (int i=0; i<M; i++){

      for (int j=0; j<N; j++)
         cout<<screen[i][j]<<"\t";
      cout<<endl;
   }

   fillColor(screen, x, y, color);
   cout<<"\nThe screen cordinates after coloring are : \n";
   for (int i=0; i<M; i++){

      for (int j=0; j<N; j++)
         cout<<screen[i][j]<<"\t";
      cout<<endl;
   }
}

#by python

import random

m =[[2,3,3,3,3,3,4,4,4,4,4,4],
	[2,3,3,3,3,3,4,4,4,4,4,4],
	[3,3,3,1,3,3,4,1,4,4,0,4],
	[3,3,1,1,1,3,1,1,1,4,4,4],
	[3,1,1,1,1,1,1,1,1,1,4,4],
	[3,1,1,0,0,0,0,0,1,1,4,4],
	[3,1,1,0,0,0,0,0,1,1,4,4],
	[2,1,1,1,1,0,0,0,1,1,2,2],
	[2,1,1,1,0,0,0,0,1,2,2,2],
	[2,2,1,1,1,0,0,2,2,2,1,0],
	[2,2,2,1,1,0,0,2,2,2,1,1],
	[2,2,2,2,2,2,2,2,2,0,1,0]
	]

def flood_recursive(matrix):
	width = len(matrix)
	height = len(matrix[0])
	def fill(x,y,start_color,color_to_update):
		#if the square is not the same color as the starting point
		if matrix[x][y] != start_color:
			return
		#if the square is not the new color
		elif matrix[x][y] == color_to_update:
			return
		else:
			#update the color of the current square to the replacement color
			matrix[x][y] = color_to_update
			neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
			for n in neighbors:
				if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
					fill(n[0],n[1],start_color,color_to_update)
	start_x = random.randint(0,width-1)
	start_y = random.randint(0,height-1)
	start_color = matrix[start_x][start_y]
	fill(start_x,start_y,start_color,9)
	return matrix

flood_recursive(m)
