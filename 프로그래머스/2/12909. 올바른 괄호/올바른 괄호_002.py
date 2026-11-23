def solution(s):
    left = []
    right = []
    
    for i, c in enumerate(s):
        if c == '(':
            left.append(i)
        if c == ')':
            right.append((i))
            
    if len(left)!=len(right):
        return False
    
    for l, r in zip(left,right):
        if l > r :
            return False
    
    return True