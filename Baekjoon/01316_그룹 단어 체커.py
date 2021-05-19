n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    check = 0
    for idx in range(len(word) - 1):
        if word[idx] != word[idx+1]:
            temp = word[idx + 1:]
            if temp.count(word[idx]) > 0:
                check = 1
                break
    if check == 0:
        cnt += 1
print(cnt)

## 다른 사람 풀이 (1등)
# n = int(input())
# cnt = 0
# for i in range(n):
#     word = input()
#     if list(word) == sorted(word,key = word.find):
#         cnt += 1
# print(cnt)

