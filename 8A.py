class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None
def insert(root, node):
    if root is None:
        return node

    if node.name < root.name:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)

    return root



def search(root, name):
    if root is None:
        return None

    if root.name == name:
        return root

    if name < root.name:
        return search(root.left, name)

    return search(root.right, name)



def search_time(root, time):
    if root is None:
        return None

    if root.time == time:
        return root

    result = search_time(root.left, time)

    if result is not None:
        return result

    return search_time(root.right, time)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.name, "|", root.time, "|", root.purpose)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.name, "|", root.time, "|", root.purpose)
        preorder(root.left)
        preorder(root.right)



def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.name, "|", root.time, "|", root.purpose)



def delete(root, name):
    if root is None:
        return None

    if name < root.name:
        root.left = delete(root.left, name)

    elif name > root.name:
        root.right = delete(root.right, name)

    else:
        
        if root.left is None:
            return root.right

        
        if root.right is None:
            return root.left

        
        temp = root.right

        while temp.left:
            temp = temp.left

        root.name = temp.name
        root.time = temp.time
        root.purpose = temp.purpose

        root.right = delete(root.right, temp.name)

    return root



def count(root):
    if root is None:
        return 0

    return 1 + count(root.left) + count(root.right)


root = None

while True:

    print("\n========== VISITOR MANAGEMENT SYSTEM ==========")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Count")
    print("8. Exit")
    

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Error: Please enter a number from 1 to 8.")
        continue

    
    if choice == 1:

        name = input("Enter visitor name: ")
        time = input("Enter entry time: ")
        purpose = input("Enter purpose: ")

        new_node = Node(name, time, purpose)
        root = insert(root, new_node)

        print("Entry inserted successfully.")


    
    elif choice == 2:

        name = input("Enter visitor name to delete: ")

        result = search(root, name)

        if result is not None:
            root = delete(root, name)
            print("Entry deleted successfully.")
        else:
            print("Visitor not found.")


    
    elif choice == 3:

        print("\n1. Search by Name")
        print("2. Search by Time")

        try:
            s = int(input("Enter search choice: "))
        except ValueError:
            print("Error: Please enter 1 or 2.")
            continue

        
        if s == 1:

            name = input("Enter visitor name: ")

            result = search(root, name)

            if result is not None:
                print("\nVisitor Found")
                print("Name    :", result.name)
                print("Time    :", result.time)
                print("Purpose :", result.purpose)
            else:
                print("Visitor not found.")


        
        elif s == 2:

            time = input("Enter entry time: ")

            result = search_time(root, time)

            if result is not None:
                print("\nVisitor Found")
                print("Name    :", result.name)
                print("Time    :", result.time)
                print("Purpose :", result.purpose)
            else:
                print("Visitor not found.")

        else:
            print("Invalid search choice. Enter 1 or 2.")


    
    elif choice == 4:

        print("\n----- INORDER TRAVERSAL -----")

        if root is None:
            print("Tree is empty.")
        else:
            inorder(root)


    
    elif choice == 5:

        print("\n----- PREORDER TRAVERSAL -----")

        if root is None:
            print("Tree is empty.")
        else:
            preorder(root)


    
    elif choice == 6:

        print("\n----- POSTORDER TRAVERSAL -----")

        if root is None:
            print("Tree is empty.")
        else:
            postorder(root)


    
    elif choice == 7:

        print("Total number of visitors:", count(root))


    
    elif choice == 8:

        print("Program terminated.")
        break


    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
