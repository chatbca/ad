def strassen_matrix_multiply(A, B):
    if len(A) != 2 or len(B) != 2:
        raise ValueError("Both input matrices must be 2x2 matrices")


    A11, A12, A21, A22 = A[0][0], A[0][1], A[1][0], A[1][1]
    B11, B12, B21, B22= B[0][0], B[0][1], B[1][0], B[1][1]
    P=(A11+A22)*(B11+B22)
    Q=B11*(A21+A22)
    R=A11*(B12-B22)
    S=A22*(B21-B11)
    T=B22*(A11+A12)
    U=(A21-A22)*(B11+B12)
    V=(B21+B22)*(A12-A22)

    C11=P+S-T+V
    C12=R+T
    C21=Q+S
    C22=P+R-Q+V

    result=[
    [C11,C12],
    [C21,C22]
    ]
    return result
print("Enter the values for the first 2x2 matrix (space-separated values):")
matrix_A = [[int(x) for x in input().split()] for _ in range(2)]
print("Enter the values for the second 2x2 matrix (space-separated values):")
matrix_B = [[int(x) for x in input().split()] for _ in range(2)]
result = strassen_matrix_multiply(matrix_A, matrix_B)
print("\nResultant Matrix:")
for row in result:
    print(row)
