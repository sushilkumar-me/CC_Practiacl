def precedence(op):
    if op in "+-":return 1
    if op in "*/":return 2
    if op in "^":return 3
def infix_postf(exp):
    s = []
    output= ""
    for ch in exp:
        if ch.isalnum(): output += ch
        elif ch == "(":
            s.append(ch)
        elif ch == ")":
            while s and s[-1] != "(":
                output += s.pop()
            s.pop()
        else:
            while s and precedence(ch) <= precedence(s[-1]):
                output += s.pop()
            s.append(ch)
    while s:
        output += s.pop()
    return output
exp = "a-b-c*d"
print(infix_postf(exp))

