while True:
    try:
        A, B = list(map(int, input().split()))
        result = A + B
        print(result)
    except:
        break