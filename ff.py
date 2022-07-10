from collections import deque
 
 
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
 

def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
 

def floodfill(mat, x, y, replacement):
 
    if not mat or not len(mat):
        return
 
   
    q = deque()
    q.append((x, y))
 
    target = mat[x][y]
 
  
    if target == replacement:
        return
 
 
    while q:
 
       
        x, y = q.popleft()
 
     
        mat[x][y] = replacement
 
     
        for k in range(len(row)):
          
            if isSafe(mat, x + row[k], y + col[k], target):
            el
                q.append((x + row[k], y + col[k]))
 
 
if __name__ == '__main__':
 
   
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
 
    
    x = 3
    y = 9
 
  
    replacement = 'C'
 
  
    floodfill(mat, x, y, replacement)
 
   
    for r in mat:
        print(r)
 
