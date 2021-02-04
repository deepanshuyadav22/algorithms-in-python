print("Linear Search")

n = int(input("Enter total number of elements : "))

print("Enter elements :", end = " ")
a = list(map(int, input().split()))

s = int(input("Enter element to search : "))

a.sort()

l = 0
r = n - 1

for i in range(0,n):
    mid = (l + r) // 2
    if s == a[mid]:
        searched = True
        break
    elif s < a[mid]:
        r = mid
        searched = False
    else:
        l = mid
        searched = False

if searched == True:
    print(str(s), "is found in the list.")
else:
    print(str(s), "is not found in the list.")