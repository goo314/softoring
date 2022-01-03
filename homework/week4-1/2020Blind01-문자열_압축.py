def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)):
        subs = [s[:i]]
        nums = [1]
        j = i
        while j <= len(s)-i:
            sub = s[j:j+i]
            if sub == subs[-1]:
                nums[-1] += 1
            else:
                subs.append(sub)
                nums.append(1)
            j += i
        tmp = 0
        for x in nums:
            tmp += len(str(x))
        tmp += len(subs)*i +len(s[j:]) - nums.count(1)
        
        if tmp < answer:
            answer = tmp
    return answer
