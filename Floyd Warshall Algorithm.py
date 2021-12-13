print("NOTE: Enter \'INF\' for infinite value of edges.\n")
n = int(input("Enter total number of vertices: "))

mat = []

for i in range(0,n):
    print("Enter the weight of edges connected to vertice " + str(i+1) + " separated by a space: ", end = "")
    mat.append(list(map(str, input().split())))

t = -1

for k in range(0,n):
    t += 1
    for i in range(0,n):
        for j in range(0,n):
            if i != j and i != t and j != t and mat[i][t] != "INF" and mat[t][j] != "INF":
                if mat[i][j] == "INF":
                    mat[i][j] = str(int(mat[i][t]) + int(mat[t][j]))
                elif int(mat[i][j]) > int(mat[i][t]) + int(mat[t][j]):
                    mat[i][j] = str(int(mat[i][t]) + int(mat[t][j]))

print("\nShortest Distance Matrix:")
for i in range(0,n):
    print(" ".join(mat[i]))
