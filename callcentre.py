q = int(input("No. of operators: "))
qs = [[] for _ in range(q)]
logs = [[] for _ in range(q)]
wt = [[] for _ in range(q)]

while True:
    print("\n---Call Center---")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Next available Operator time")
    print("5. Check if a queue is Empty")
    print("6. Avg Wait Time per operator")
    print("7. Exit")
    print("8. View Call Log")

    c = input("Enter choice (1-8): ")

    if c == '1':
        cid = input("Customer ID: ")
        t = int(input("Call time (min): "))
        
        qt = [sum(call[1] for call in queue) for queue in qs]
        mt = min(qt)
        idx = qt.index(mt)
        
        qs[idx].append((cid, t))
        wt[idx].append(mt)
        print(f"Call {cid} added to Queue {idx + 1}. Wait: {mt} min.")

    elif c == '2':
        op = int(input(f"Operator no. (1-{q}): ")) - 1
        if 0 <= op < q:
            if qs[op]:
                cid, t = qs[op].pop(0)
                logs[op].append((cid, t))
                print(f"Answering call {cid} in Queue {op + 1}.")
            else:
                print(f"Queue {op + 1} is empty.")
        else:
            print("Invalid operator.")

    elif c == '3':
        op = int(input(f"Operator no. (1-{q}): ")) - 1
        if 0 <= op < q:
            if qs[op]:
                print(f"Queue {op + 1}:")
                for cid, t in qs[op]:
                    print(f"Customer {cid}, Time: {t} min")
            else:
                print(f"Queue {op + 1} is empty.")
        else:
            print("Invalid operator.")

    elif c == '4':
        qt = [sum(call[1] for call in queue) for queue in qs]
        mt = min(qt)
        idx = qt.index(mt)
        print(f"Operator {idx + 1} available in ~{mt} min.")

    elif c == '5':
        if any(qs):
            print("At least one queue has calls.")
        else:
            print("All queues are empty.")

    elif c == '6':
        for i in range(q):
            if wt[i]:
                tt = sum(wt[i])
                nc = len(wt[i])
                avg = tt / nc
                print(f"Op {i + 1}: Avg wait is {avg:.2f} min over {nc} calls.")
            else:
                print(f"Op {i + 1}: No calls added yet.")

    elif c == '7':
        print("Exiting.")
        break
    
    elif c == '8':
        op = int(input(f"Operator no. (1-{q}): ")) - 1
        if 0 <= op < q:
            if logs[op]:
                print(f"Log for Op {op + 1}:")
                for cid, t in logs[op]:
                    print(f"Customer {cid}, Time: {t} min")
            else:
                print(f"No calls answered by Op {op + 1}.")
        else:
            print("Invalid operator.")

    else:
        print("Invalid choice.")