''' Merge_Sort '''

def merge(p, q, r):
    global arr
    temp = []
    idx = 0
    a, b = p, q + 1

    while a <= q and b <= r:
        if arr[a] <= arr[b]:
            temp.append(arr[a])
            a += 1
        else:
            temp.append(arr[b])
            b += 1
    
    while a <= q:
        temp.append(arr[a])
        a += 1
    
    while b <= r:
        temp.append(arr[b])
        b += 1

    i = p
    idx = 0
    while (i <= r):
        arr[i] = temp[idx]
        i += 1
        idx += 1

def merge_sort(p, r):
    global arr
    if p < r:
        q = ((p - 1) + r) // 2
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)
    
n = int(input())
arr = []
arr.append(-1)
for _ in range(n):
    arr.append(int(input()))

merge_sort(1, n)

for i in range(1,len(arr)):
    print(arr[i])
