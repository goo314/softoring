import bisect

def solution(words, queries):
    answer = []
    word_list = [list() for _ in range(100000+1)]
    rev_list = [list() for _ in range(100000+1)]
    
    for w in words:
        len_w = len(w)
        
        word_list[len_w].append(w)
        rev_list[len_w].append(w[::-1])
        
    for i in range(100000+1):
        if len(word_list[i]) != 0:
            word_list[i].sort()
            rev_list[i].sort()
    
    for q in queries:
        len_q = len(q)

        if q[0] != '?':
            left = bisect.bisect_left(word_list[len_q], q)

            idx = q.index('?')
            next_q = q[:idx-1] 
            next_q += chr(ord(q[q.index('?')-1])+1)
            next_q += q[idx:]
            right = bisect.bisect_right(word_list[len_q], next_q)
            
            answer.append(right - left)
            
        else:
            q = q[::-1]
            left = bisect.bisect_left(rev_list[len_q], q)

            idx = q.index('?')
            next_q = q[:idx-1] 
            next_q += chr(ord(q[q.index('?')-1])+1)
            next_q += q[idx:]
            right = bisect.bisect_right(rev_list[len_q], next_q)
            
            answer.append(right - left)
    
    return answer
