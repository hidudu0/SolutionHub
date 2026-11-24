import math

def solution(fees, records):
    base_t, base_fee, unit_t, unit_fee = fees
    answer = []
    inside = {}
    total = {}
    
    for r in records:
        t, n, i = r.split()
        h,m = map(int, t.split(':'))
        tm = h *60 + m
        if i == 'IN':
            inside[n] = tm
        else:
            total[n] = total.get(n,0) + tm - inside.pop(n)
    
    for n, tm in inside.items():
        total[n] = total.get(n,0) + 23*60+59 - tm
        
    for n in sorted(total):
        if total[n] < base_t:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((total[n] - base_t)/unit_t)*unit_fee
        answer.append(fee)
        
    return answer