def solution(s):
    cnt_l = 0
    cnt_r = 0
    
    for c in s:
        if c == '(':
            cnt_l += 1
        elif c == ')':
            cnt_r +=1
            if cnt_l<cnt_r:
                return False
                
    if cnt_l!=cnt_r:
        return False
    
    return True