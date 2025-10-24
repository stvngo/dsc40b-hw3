def swap_sum(A, B):
    # A, B: sorted lists of integers
    SA, SB = sum(A), sum(B)
    num = SA - SB + 10
    if num % 2 != 0:
        return None     
    delta = num // 2

    i, j = 0, 0
    n, m = len(A), len(B)

    while i < n and j < m:
        target = A[i] - delta
        if B[j] == target:
            return (i, j)
        elif B[j] < target:
            j += 1    
        else:
            i += 1   

    return None
