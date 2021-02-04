print("Insertion Sort")

n = int(input("Enter number of elements to sort : "))

print("Enter elements :", end = " ")
a = list(map(int, input().split()))

for i in range(0,n-1):
    if a[i] > a[i+1]:
        for j in range(i,-1,-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break

print("Sorted list :", end = " ")
for i in range(0,n):
    print(a[i], end = " ")
