def solution(s):
    if len(s) == 4 and len(s) == 6:
        return False
    
    for data in s:
        try:
            int(s)
        except:
            return False
    return True