def matrice2x3():
    return[[0 for j in range(0, 3) for i in range(0, 2)]]


A = matrice2x3()
print("A=", A)


M = [[0 for j in range(0, 4)] for i in range(0, 3)]
M[0][0] = 4
M[1][2] = 8
print(M)

#############################################################
# voici deux methodes pour faire la somme de deux matrices  #
#############################################################


# Methode 1 avec la fonction zip
mat1 = [[20, -5, 11], [10, -1, 5]]
mat2 = [[2, 5, 1], [0, 1, 2]]


def sumMat(mat1, mat2):
    mat3 = []
    for list1, list2 in zip(mat1, mat2):
        mat3.append([list1[i]+list2[i] for i in range(len(list1))])
    return mat3


print(sumMat(mat1, mat2))

# Methode 2 avec une boucle imbriquee
M1 = [[20, -5, 11], [10, -1, 5]]
M2 = [[2, 5, 1], [0, 1, 2]]


def sumMat2(M1, M2):
    n = len(M1)     # Recuperer le nombre des lignes de la matrice M1
    m = len(M1[0])  # Recuperer le nombre des colonnes de la matrice M1

    # Creer une matrice nxm pleine de zero
    M = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            M[i][j] = M1[i][j]+M2[i][j]  # M(i,j)=M1(i,j)+M2(i,j)

    return M


print(sumMat2(M1, M2))
