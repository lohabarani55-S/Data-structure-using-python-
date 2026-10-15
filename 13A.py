n = int(input("Enter the number of students: "))
roll_numbers = []
for i in range(n):
    roll = int(input("Enter roll number: "))
    roll_numbers.append(roll)
key = int(input("Enter roll number to search: "))
found = False

for i in range(n):
    if roll_numbers[i] == key:
        found = True
        break

if found:
    print("Linear Search: Roll number found")
else:
    print("Linear Search: Roll number not found")
sorted_rolls = sorted(roll_numbers)

low = 0
high = len(sorted_rolls) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if sorted_rolls[mid] == key:
        found = True
        break
    elif sorted_rolls[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Roll number found")
else:
    print("Binary Search: Roll number not found")
