def solution(sequence, k):
    answer = [0, len(sequence)]  
    l = 0
    total = 0
    for r in range(len(sequence)):
        total += sequence[r]          
        while total > k:
            total -= sequence[l]        
            l += 1
        if total == k and r-l < answer[1]-answer[0]:   
            answer = [l, r]
    return answer