def solution(my_string, is_prefix):
    if my_string.startswith(f'{is_prefix}') == True:
        return 1
    else:
        return 0