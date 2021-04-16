def lcs(i, j, k):
    if k == 0:
        return 0
    elif mat[i][j-1] == k:
        lcs(i, j-1, k)
    elif mat[i-1][j] == k:
        lcs(i-1, j, k)
    else:
        lcs(i-1, j-1, mat[i-1][j-1])
        print(s2[i-1], end = "")

s1 = str(input("Enter first word: "))
s2 = str(input("Enter second word: "))

rows = len(s2) + 1
cols = len(s1) + 1
mat = []
temp = []

for i in range(0, cols):
    temp.append(0)
mat.append(temp)

for i in range(1, rows):
    mat.append([0])

for i in range(1, rows):
    for j in range(1, cols):
        if s2[i-1] != s1[j-1]:
            mat[i].append(max(mat[i][j-1], mat[i-1][j]))
        else:
            mat[i].append(mat[i-1][j-1] + 1)

print("Longest Common Subsequence is: ", end = "")
lcs(rows-1, cols-1, mat[rows-1][cols-1])

'''i = rows - 1
j = cols - 1
k = mat[i][j]
res = ""

while k != 0:
    if mat[i][j-1] == k:
        j -= 1
    elif mat[i-1][j] == k:
        i -= 1
    else:
        res += s2[i-1]
        i -= 1
        j -= 1
        k = mat[i][j]

print("Longest Common Subsequence is:",res[::-1])'''