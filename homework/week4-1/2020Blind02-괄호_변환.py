def correct_str(u):
    stack = list()
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                del stack[-1]
    if len(stack) == 0:
        return True
    return False

def reverse_bracket(u):
    rev = ''
    for c in u:
        if c == '(':
            rev += ')'
        else:
            rev += '('
    return rev
            
def solution(p):
    if len(p) == 0:
        return p
    
    # 2
    left, right, pos = 0, 0, 0
    while True:
        if p[pos] == '(':
            left += 1
        else:
            right += 1
        pos += 1
        
        if left == right:
            break
    
    u, v = p[:pos], p[pos:]
    
    # 3
    if correct_str(u):
        return u + solution(v)
    
    # 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        answer += reverse_bracket(u[1:-1])
        return answer
