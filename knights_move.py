str = input()
s=str[0]
x = 8-int(str[1])
symb = 'abcdefgh'
y = symb.find(s)
matrix = [['.']*8 for _ in range(8)]
matrix[x][y] = 'Q'
for i in range(8):
    if matrix[i][y]!='Q':
        matrix[i][y] ='*'
    if matrix[x][i]!='Q':
        matrix[x][i] = '*'

for i in range(8):
    for j in range(8):
        if abs(x - i) == abs(y - j) and matrix[i][j]!='Q':
            matrix[i][j] = '*'
for row in matrix:
    print(*row)
print("Hello")
print("New row")
    




