n = int(input("Enter the number of students: "))

a = []

for i in range(n):
    mark = int(input("Enter student mark: "))
    a.append(mark)

print("Marks before sorting:", a)

b = a.copy()

for i in range(n - 1):
    for j in range(n - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

print("Bubble Sort:", b)


c = a.copy()

for i in range(1, n):
    key = c[i]
    j = i - 1

    while j >= 0 and c[j] > key:
        c[j + 1] = c[j]
        j -= 1

    c[j + 1] = key

print("Insertion Sort:", c)

d = a.copy()

for i in range(n - 1):
    least = i

    for j in range(i + 1, n):
        if d[j] < d[least]:
            least = j

    d[i], d[least] = d[least], d[i]

print("Selection Sort:", d)
