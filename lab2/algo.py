def SimpleMatrixMultiply(m1: list[list[int]], m2: list[list[int]]):
    if len(m1[0]) != len(m2):
        raise ValueError("Matrices cannot be multiplied")

    result = [[0] * len(m2[0]) for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result

def VinogradMatrixMultiply(m1: list[list[int]], m2: list[list[int]]):
    if (len(m1) == 0 or len(m2) == 0):
        raise ValueError("Empty matrix")

    if len(m1[0]) != len(m2):
        raise ValueError("Matrices cannot be multiplied")

    M = len(m1)
    N = len(m1[0]) # == len(m2)
    Q = len(m2[0])
    result = [[0] * Q for _ in range(M)]

    mulH = [0] * (M)
    for i in range(M):
        for j in range(N // 2):
            mulH[i] = mulH[i] + m1[i][2*j] * m1[i][2*j + 1]

    mulV = [0] * (Q)
    for i in range(Q):
        for j in range(N // 2):
            mulV[i] = mulV[i] + m2[2*j][i] * m2[2*j + 1][i]

    for i in range(M):
        for j in range(Q):
            result[i][j] = -mulH[i] -mulV[j]
            for k in range(N // 2):
                result[i][j] = result[i][j] + (m1[i][2*k]+m2[2*k + 1][j]) * (m1[i][2*k + 1]+m2[2*k][j])

    if (N % 2 != 0):
        for i in range(M):
            for j in range(Q):
                result[i][j] = result[i][j] + m1[i][-1] * m2[-1][j]

    return result

def OptimizedVinogradMatrixMultiply(m1: list[list[int]], m2: list[list[int]]):
    if (len(m1) == 0 or len(m2) == 0):
        raise ValueError("Empty matrix")

    if len(m1[0]) != len(m2):
        raise ValueError("Matrices cannot be multiplied")

    M = len(m1)
    N = len(m1[0]) # == len(m2)
    Q = len(m2[0])
    result = [[0] * Q for _ in range(M)]

    mulH = [0] * (M)
    for i in range(M):
        mulH[i] = m1[i][0] * m1[i][1]
        for j in range(2, N - 1, 2):
            mulH[i] += m1[i][j] * m1[i][j + 1]

    mulV = [0] * (Q)
    for i in range(Q):
        mulV[i] = m2[0][i] * m2[1][i]
        for j in range(2, N - 1, 2):
            mulV[i] += m2[j][i] * m2[j + 1][i]

    for i in range(M):
        for j in range(Q):
            result[i][j] = -mulH[i] -mulV[j] + (m1[i][0]+m2[1][j]) * (m1[i][1]+m2[0][j])
            for k in range(2, N - 1, 2):
                result[i][j] += (m1[i][k]+m2[k + 1][j]) * (m1[i][k + 1]+m2[k][j])

    if (N % 2 != 0):
        for i in range(M):
            for j in range(Q):
                result[i][j]  += m1[i][-1] * m2[-1][j]

    return result



if __name__ == '__main__':
    mat1 = [
        [1, 2, 3, 2],
        [4, 5, 6, 4],
        [7, 8, 9, 2],
        [1, 32, 12, 43]
    ]

    mat2 = [
        [16, 24, 23, 15],
        [23, 56, 12, 43],
        [12, 54, 65, 21],
        [1, 32, 12, 43]
    ]

    res1 = SimpleMatrixMultiply(mat1, mat2)
    res2 = VinogradMatrixMultiply(mat1, mat2)
    res3 = OptimizedVinogradMatrixMultiply(mat1, mat2)

    for i in range(len(res1)):
        print(*res1[i])
    print()
    for i in range(len(res2)):
        print(*res2[i])

    print()
    for i in range(len(res3)):
        print(*res3[i])
