''' Selection Sort '''

import sys
input = sys.stdin.readline

def Sort(data):
   for i in range(n):
      min_index = i # The index of the minimum value.
      for j in range(i + 1, n):
         if data[min_index] > data[j]:
               min_index = j
      data[i], data[min_index] = data[min_index], data[i] # Swap.

n = int(input())
data = list(map(int, input().split()))
Sort(data)
print(data)
