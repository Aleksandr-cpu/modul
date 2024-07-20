
def get_matrix(n,m,value):
    matrix =[]
    for i in range(n):
        i = []
        matrix.append(i)
        for j in range(m) :
            i.append(value)
    return matrix

print(get_matrix(6,10,10))