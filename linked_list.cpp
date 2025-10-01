#include <bits/stdc++.h>
using namespace std;

struct Student {
    int roll;
    string name;
    float marks;
    Student* next;
};

struct StudentList {
    Student* head = nullptr;
    void add(int roll, string name, float marks) {
        Student* newNode = new Student{roll, name, marks, nullptr};
        if (!head) {
            head = newNode;
        } else {
            Student* curr = head;
            while (curr->next) {
                curr = curr->next; }
            curr->next = newNode;
 }
    }

    void remove(int roll) {
        if (!head) return;

        if (head->roll == roll) {
            Student* temp = head;
            head = head->next;
            delete temp;
            return;}
        Student* curr = head;
        while (curr->next && curr->next->roll != roll) {
            curr = curr->next;
        }
        if (curr->next) {
            Student* temp = curr->next;
            curr->next = temp->next;
            delete temp;
        }
    }

    void search(int roll) {
        Student* curr = head;
        while (curr) {
            if (curr->roll == roll) {
                cout << curr->roll << " " << curr->name << " " << curr->marks << "\n";
                return; }
            curr = curr->next;
        }
        cout << "Not found\n";
    }

    void display() {
        Student* curr = head;
        while (curr){
            cout << curr->roll << " " << curr->name << " " << curr->marks << "\n";
            curr = curr->next;}
    }

    void sortByRoll() {
        if (!head || !head->next) 
           return;
        bool swapped;
        do {swapped = false;
            Student** currPtr = &head;
            while ((*currPtr)->next) {
                Student* a = *currPtr; Student* b = a->next;
                if (a->roll > b->roll) {
                    a->next = b->next;
                    b->next = a;
                    *currPtr = b; 
                    swapped = true;}
                currPtr = &((*currPtr)->next);}
        } while (swapped);
    }

    void concatenate(StudentList& other) {
        if (!head) {
            head = other.head;
        } else {
            Student* curr = head;
            while (curr->next) {
                curr = curr->next;}
            curr->next = other.head;}
        other.head = nullptr; }};

int main() {
    StudentList list1, list2;
    int choice, roll;
    string name;
    float marks;

    do {
        cout << "1. Add to List 1\n";
        cout << "2. Delete from List 1\n";
        cout << "3. Search in List 1\n";
        cout << "4. Display List 1\n";
        cout << "5. Sort List 1 by Roll\n";
        cout << "6. Add to List 2\n";
        cout << "7. Display List 2\n";
        cout << "8. Concatenate List 2 to List 1\n";
        cout << "9. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter Roll, Name, Marks: ";
            cin >> roll >> name >> marks;
            list1.add(roll, name, marks);
        } else if (choice == 2) {
            cout << "Enter Roll to delete: ";
            cin >> roll;
            list1.remove(roll);
        } else if (choice == 3) {
            cout << "Enter Roll to search: ";
            cin >> roll;
            list1.search(roll);
        } else if (choice == 4) {
            cout << "List 1:\n";
            list1.display();
        } else if (choice == 5) {
            list1.sortByRoll();
            cout << "List 1 sorted by roll number.\n";
            list1.display(); 
        } else if (choice == 6) {
            cout << "Enter Roll, Name, Marks: ";
            cin >> roll >> name >> marks;
            list2.add(roll, name, marks);
        } else if (choice == 7) {
            cout << "List 2:\n";
            list2.display();
        } else if (choice == 8) {
            list1.concatenate(list2);
            cout << "List 2 has been concatenated into List 1.\n";
        } else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 9);

    return 0;
}
