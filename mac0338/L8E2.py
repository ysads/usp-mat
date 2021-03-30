def divide(A, B, n):
    if n == -1:
        return 0

    if A[n] == B[n]:
        return 1

    return divide(A, B, n)
