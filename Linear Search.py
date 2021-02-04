print("Linear Search")

n = int(input("Enter total number of elements : "))

print("Enter elements :", end = " ")
a = list(map(int, input().split()))

s = int(input("Enter element to search : "))

for i in range(0,n):
    if a[i] == s:
        searched = True
        break
    else:
        searched = False

if searched == True:
    print(str(s), "is found in the list.")
else:
    print(str(s), "is not found in the list.")