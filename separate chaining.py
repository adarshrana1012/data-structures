size = 10
table = [[] for _ in range(size)]

while True:
    print("1)insert 2)search 3)delete 4)display 5)exit")
    ch = input("ch=")
    if ch == '1':
        roll = int(input("Enter roll no: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        table[roll % size].append([roll, name, marks]) 
    elif ch == '2':
        roll = int(input("Enter roll no to search: "))
        bucket = table[roll % size]
        found = False
        for record in bucket:
            if record[0] == roll:
                print("Found:", record[0], record[1], record[2])
                found = True
                break
        if not found:
            print("Not found")
    elif ch == '3':
        roll = int(input("Enter roll no to delete: "))
        bucket = table[roll % size]
        found = False
        for i in range(len(bucket)):
            if bucket[i][0] == roll:
                del bucket[i]
                print("Deleted")
                found = True
                break
        if not found:
            print("Not found")
    elif ch == '4':
        for i in range(size):
            print(f"{i}: {table[i]}")
    elif ch == '5':
        break
    else:
        print("Invalid choice")
