n = 5

''' Python Sort Library (Basic) '''
data = [8, 5, 4, 7, 2]
data.sort()

for x in data:
    print(x)

print("---------------")

''' Python Sort Library (Based on a key1) '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0]) # Stable Sort1 (When using a key)

for x in data:
    print(x)

print("---------------")

''' Python Sort Library (Based on a key2) '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: (x[0], x[1])) # Stable Sort2 (When using a key)

for x in data:
    print(x)

print("---------------")

''' Python Sort Library '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort() # Non-stable Sort (When not using a key)

for x in data:
    print(x)

print("---------------")
