def precedence(op):
    if op in "+-": return 1 
    if op in "*/": return 2 
    if op in "^": return 3
    return 0 

def postfix(exp): 
    stack = [] 
    output = ""  
    for ch in exp: 
        if ch.isalnum(): 
            output += ch 
        elif ch == "(": 
            stack.append(ch) 
        elif ch == ")": 
            while stack and stack[-1] != "(": 
                output += stack.pop() 
            stack.pop() 
        else: 
            while stack and precedence(ch) <= precedence(stack[-1]): 
                output += stack.pop() 
            stack.append(ch)
    while stack: 
        output += stack.pop() 
    return output

exp = "A+B*C"
print(postfix(exp))