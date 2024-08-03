## Stack

- if '( { [ ' stack.push()

- if ') } ] ' => 짝이면 stack.pop() 그렇지 않으면 return F

```
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{" :
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False

    return not stack
```
