def print_matrix(m):
    for row in m:
        for element in row:
            print(element, end=' ')
        print() # konec řádky


def unit_matrix(N):
    matrix = []

    for i in range(N):
        matrix.append([])
        for j in range(N):
            matrix[i].append(0)
    for i in range(N):
        matrix[i][i] = 1
    return matrix



m = unit_matrix(3)
print_matrix(m)
print()
print_matrix(unit_matrix(6))
