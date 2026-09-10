heap = []
def insert_job(job, priority):
    heap.append((priority, job))
    i = len(heap) - 1


    while i > 0:
        parent = (i - 1) // 2

        if heap[i][0] > heap[parent][0]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

heap = []
def insert_job():
    job = input("Enter Job Name: ")
    priority = int(input("Enter Priority: "))

    heap.append((priority, job))
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2

        if heap[i][0] > heap[parent][0]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

    print("Job inserted successfully!")
def delete_max():
    if len(heap) == 0:
        print("Heap is empty")
        return

    max_job = heap[0]
    last = heap.pop()

    if len(heap) > 0:
        heap[0] = last
        i = 0

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < len(heap) and heap[left][0] > heap[largest][0]:
                largest = left

            if right < len(heap) and heap[right][0] > heap[largest][0]:
                largest = right

            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
            else:
                break

    print("Deleted Job:", max_job[1])
    print("Priority:", max_job[0])


def peek():
    if len(heap) == 0:
        print("Heap is empty")
    else:
        print("Highest Priority Job:", heap[0][1])
        print("Priority:", heap[0][0])


def display():
    if len(heap) == 0:
        print("Heap is empty")
    else:
        print("\nJobs in Heap Order:")
        for priority, job in heap:
            print(job, "-", priority)


while True:
    print("\n===== JOB PRIORITY QUEUE =====")
    print("1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_job()

    elif choice == 2:
        delete_max()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")
