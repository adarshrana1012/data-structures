class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Student(roll, name, marks)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def remove(self, roll):
        if not self.head:
            return
        if self.head.roll == roll:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.roll != roll:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def search(self, roll):
        curr = self.head
        while curr:
            if curr.roll == roll:
                print(f"{curr.roll} {curr.name} {curr.marks}")
                return
            curr = curr.next
        print("Not found")

    def display(self):
        curr = self.head
        if not curr:
            print("List is empty.")
        while curr:
            print(f"{curr.roll} {curr.name} {curr.marks}")
            curr = curr.next

    def sort_by_roll(self):
        i = self.head
        while i:
            j = i.next
            while j:
                if i.roll > j.roll:
                    i.roll, j.roll = j.roll, i.roll
                    i.name, j.name = j.name, i.name
                    i.marks, j.marks = j.marks, i.marks
                j = j.next
            i = i.next

def main():
    student_list = StudentList()

    while True:
        print("\n1. Add 2. Delete 3. Search 4. Display 5. Sort by Roll 6. Exit:")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            roll = int(input("Enter roll: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            student_list.add(roll, name, marks)
        elif choice == 2:
            roll = int(input("Enter roll to delete: "))
            student_list.remove(roll)
        elif choice == 3:
            roll = int(input("Enter roll to search: "))
            student_list.search(roll)
        elif choice == 4:
            student_list.display()
        elif choice == 5:
            student_list.sort_by_roll()
            print("List sorted by roll number:")
            student_list.display()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
