print("Bubble Sort")

n = int(input("Enter number of elements to sort : "))

print("Enter elements :", end = " ")
a = list(map(int, input().split()))

for i in range(0,n):
    bs = False

    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            bs = True
    
    if bs == False:
        break

print("Sorted list :", end = " ")
for i in range(0,n):
    print(a[i], end = " ")