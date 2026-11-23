def solution(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c)
        elif c == ')':
            if not st:
                return False
            st.pop()
    return not st