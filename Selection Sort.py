print("Selection Sort")

n = int(input("Enter number of elements to sort : "))
#n = 5

print("Enter elements :", end = " ")
a = list(map(int, input().split()))
#a = [25, 62, 12, 22, 11]

for i in range(0,n-1):
    min_ele = min(a[i:])
    min_ele_ind = a.index(min_ele)

    if min_ele_ind == i:
        continue
    else:
        for j in range(min_ele_ind,i,-1):
            a[j-1], a[j] = a[j], a[j-1]

print("Sorted list :", end = " ")
for i in range(0,n):
    print(a[i], end = " ")
print()