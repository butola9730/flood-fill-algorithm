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
