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

from collections import deque
 
 
# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
 
# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
 
 
# Flood fill using BFS
def floodfill(mat, x, y, replacement):
 
    # base case
    if not mat or not len(mat):
        return
 
    # create a queue and enqueue starting pixel
    q = deque()
    q.append((x, y))
 
    # get the target color
    target = mat[x][y]
 
    # target color is same as replacement
    if target == replacement:
        return
 
    # break when the queue becomes empty
    while q:
 
        # dequeue front node and process it
        x, y = q.popleft()
 
        # replace the current pixel color with that of replacement
        mat[x][y] = replacement
 
        # process all eight adjacent pixels of the current pixel and
        # enqueue each valid pixel
        for k in range(len(row)):
            # if the adjacent pixel at position (x + row[k], y + col[k]) is
            # is valid and has the same color as the current pixel
            if isSafe(mat, x + row[k], y + col[k], target):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))
 
 
if __name__ == '__main__':
 
    # matrix showing portion of the screen having different colors
    mat = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
 
    # start node
    x = 3
    y = 9
 
    # having target color `X`
    # replacement color
    replacement = 'C'
 
    # replace the target color with a replacement color
    floodfill(mat, x, y, replacement)
 
    # print the colors after replacement
    for r in mat:
        print(r)
 
