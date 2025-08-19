q = int(input("Number of operators: "))
qs = [[] for _ in range(q)]

while True:
    print("\n---Call Center---")
    print("1. Add a Call")
    print("2. Answer a Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        cid = input("Enter customer ID: ")
        t = int(input("Enter call time (in minutes): "))
        min_time = sum(call[1] for call in qs[0])
        idx = 0
        for i in range(1, q):
            total = 0
            for call in qs[i]:
                total += call[1]
            if total < min_time:
                min_time = total
                idx = i
        qs[idx].append((cid, t))
        print(f"Call from Customer {cid} added to Queue {idx + 1}.")

    elif choice == '2':
        op = int(input(f"Enter operator number (1-{q}): ")) - 1
        if 0 <= op < q:
            if len(qs[op]) == 0:
                print(f"No calls to answer in Queue {op + 1}.")
            else:
                cid, t = qs[op].pop(0)
                print(f"Answering call from Customer {cid} in Queue {op + 1} who waited {t} minutes.")
        else:
            print("Invalid operator number.")

    elif choice == '3':
        op = int(input(f"Enter operator number (1-{q}): ")) - 1
        if 0 <= op < q:
            if len(qs[op]) == 0:
                print(f"Queue {op + 1} is empty.")
            else:
                print(f"Calls in Queue {op + 1}:")
                for cid, t in qs[op]:
                    print(f"Customer {cid}, Call Time: {t} minutes")
        else:
            print("Invalid operator number.")

    elif choice == '4':
        empty = True
        for i in range(q):
            if len(qs[i]) > 0:
                empty = False
                break
        if empty:
            print("All queues are empty.")
        else:
            print("At least one queue has calls.")

    elif choice == '5':
        print("Exiting the progrom.")
        break

    else:
        print("Invalid choice.")
