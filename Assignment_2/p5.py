l1 = []
l2 = list()

while True:
    ch = int(input(
        "\nEnter your choice:"
        "\n1. Add element to first list"
        "\n2. Add element to second list"
        "\n3. Join both lists"
        "\n4. Repeat first list"
        "\n5. Check element in first list"
        "\n6. Slice first list"
        "\n7. Display both lists"
        "\n0. Exit"
        "\nChoice: "
    ))

    if ch == 1:
        ele = int(input("Enter element: "))
        l1.append(ele)
        print("First list:", l1)

    elif ch == 2:
        ele = int(input("Enter element: "))
        l2.append(ele)
        print("Second list:", l2)

    elif ch == 3:
        print("Joined list:", l1 + l2)

    elif ch == 4:
        n = int(input("Enter number of repetitions: "))
        print("Repeated list:", l1 * n)

    elif ch == 5:
        ele = int(input("Enter element to check: "))

        if ele in l1:
            print("Element found")
        else:
            print("Element not found")

    elif ch == 6:
        start = int(input("Enter start index: "))
        stop = int(input("Enter stop index (excluded): "))
        step = int(input("Enter step (cannot be 0): "))

        if step == 0:
            print("Step cannot be zero")
        else:
            print("Sliced list:", l1[start:stop:step])

    elif ch == 7:
        print("First list:", l1)
        print("Second list:", l2)

    elif ch == 0:
        break

    else:
        print("Invalid choice")