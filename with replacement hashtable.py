ts = 10
t = [-1] * ts

while True:
    print("\n---HashTable---")
    print("1. insert 2. search 3. delete 4. display 5. exit")
    ch = input("Enter choice (1-5): ")

    if ch == '1':
        e = int(input("Enter number: "))
        c = sum(1 for x in t if x != -1)
        if c >= ts // 2:
            old = t
            ts *= 2
            t = [-1] * ts
            for x in old:
                if x != -1:
                    i = x % ts
                    while t[i] != -1:
                        i = (i + 1) % ts
                    t[i] = x
        i = e % ts
        if t[i] == -1:
            t[i] = e
        else:
            ex = t[i]
            if ex % ts != i:
                t[i] = e
                e = ex
                i = (i + 1) % ts
                while t[i] != -1:
                    i = (i + 1) % ts
                t[i] = e
            else:
                i = (i + 1) % ts
                while t[i] != -1:
                    i = (i + 1) % ts
                t[i] = e

    elif ch == '2':
        e = int(input("Enter number to search: "))
        i = e % ts
        start = i
        fnd = False
        while t[i] != -1:
            if t[i] == e:
                print(f"Found at index {i}")
                fnd = True
                break
            i = (i + 1) % ts
            if i == start:
                break
        if not fnd:
            print("Not found")

    elif ch == '3':
        e = int(input("Enter number to delete: "))
        i = e % ts
        start = i
        fnd = False
        while t[i] != -1:
            if t[i] == e:
                t[i] = -1
                print("Deleted")
                fnd = True
                break
            i = (i + 1) % ts
            if i == start:
                break
        if not fnd:
            print("Not found")

    elif ch == '4':
        print("\nHash Table:")
        for i in range(ts):
            print(f"{i}: {t[i]}")

    elif ch == '5':
        break

    else:
        print("Invalid choice")
