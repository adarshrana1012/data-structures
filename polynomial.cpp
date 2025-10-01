#include <iostream>
using namespace std;

struct Term {
    int coeff, exp;
    Term* next;
};

Term* createTerm(int coeff, int exp) {
    Term* term = new Term;
    term->coeff = coeff;
    term->exp = exp;
    term->next = nullptr;
    return term;
}
void append(Term*& head, int coeff, int exp) {
    Term* newTerm = createTerm(coeff, exp);
    if (!head) {
        head = newTerm;
    } else {
        Term* temp = head;
        while (temp->next)
            temp = temp->next;
        temp->next = newTerm;
    }
}
void inputPolynomial(Term*& head, int n, int polyNumber) {
    cout << "Enter " << n << " terms for polynomial " << polyNumber<<endl ;
    for (int i = 0; i < n; i++) {
        int coeff, exp;
        cout << "Term " << i + 1 << " (coeff and exp): ";
        cin >> coeff >> exp;
        append(head, coeff, exp);
    }
}
Term* add(Term* p1, Term* p2) {
    Term* result = nullptr;
    while (p1 && p2) {
        if (p1->exp > p2->exp) {
            append(result, p1->coeff, p1->exp);
            p1 = p1->next;
        } else if (p1->exp < p2->exp) {
            append(result, p2->coeff, p2->exp);
            p2 = p2->next;
        } else {
            int sum = p1->coeff + p2->coeff;
            if (sum != 0)
                append(result, sum, p1->exp);
            p1 = p1->next;
            p2 = p2->next;
        }
    }
    while (p1) {
        append(result, p1->coeff, p1->exp);
        p1 = p1->next;
    }
    while (p2) {
        append(result, p2->coeff, p2->exp);
        p2 = p2->next;
    }
    return result;
}
void print(Term* head) {
    if (!head) {
        cout << "0\n";
        return;
    }
    while (head) {
        cout << head->coeff << "x^" << head->exp;
        head = head->next;
        if (head) cout << " + ";
    }
    cout << endl;
}
int main() {
    Term *poly1 = nullptr, *poly2 = nullptr;
    int n1, n2;
    cout << "Enter num of terms in poly 1: "<<endl;
    cin >> n1;
    inputPolynomial(poly1, n1, 1);
    cout << "Enter num of terms in poly 2 "<<endl;
    cin >> n2;
    inputPolynomial(poly2, n2, 2);
    Term* sum = add(poly1, poly2);
    cout << "sum of polynomials: "<<endl;
    print(sum);
    return 0;
}
