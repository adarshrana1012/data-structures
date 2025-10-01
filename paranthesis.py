s = input("Enter an expression: ")
stk = []
for c in s:
    if c in '([{':
        stk.append(c)
        print("push:", c, "stack:", stk)
    elif c in ')]}':
        if not stk:
            print("Not Balanced")
            break
        t = stk.pop()
        print("pop:", t, "stack:", stk)
        if c == ')' and t != '(':
            print("Not Balanced")
            break
        if c == ']' and t != '[':
            print("Not Balanced")
            break
        if c == '}' and t != '{':
            print("Not Balanced")
            break
else:
    if not stk:
        print("Balanced")
    else:
        print("Not Balanced")

        
