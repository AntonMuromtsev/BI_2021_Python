import numpy as np


def matrix_multiplication(m1, m2):
    result = []
    nrow_m1 = m1.shape[0]
    ncol_m2 = m2.shape[1]
    for i in range(nrow_m1):
        for j in range(ncol_m2):
            dot = m1[i, :] * m2[:, j]
            result.append(dot.sum())
    result = np.array(result).reshape(nrow_m1, ncol_m2)
    return result


def multiplication_check(matrix_list: list) -> bool:
    ncol = matrix_list[0].shape[1]
    for i in range(1, len(matrix_list)):
        nrow = matrix_list[i].shape[0]
        if nrow == ncol:
            ncol = matrix_list[i].shape[1]
        else:
            return False
    return True


def multiply_matrices(matrix_list: list):
    if multiplication_check(matrix_list) is False:
        return None
    step = matrix_multiplication(matrix_list[0], matrix_list[1])
    for i in range(2, len(matrix_list)):
        step = matrix_multiplication(step, matrix_list[i])
    return step


def compute_multidimensional_distance(arr1, arr2):
    coord = arr2 - arr1
    coord_sq = coord ** 2
    dist_sq = coord_sq.sum()
    return dist_sq ** 0.5


def compute_2d_distance(arr1, arr2):
    return compute_multidimensional_distance(arr1, arr2)


def compute_pair_distances(matrix):
    nrow = matrix.shape[0]
    dist_matrix = np.zeros(nrow ** 2).reshape(nrow, nrow)
    for i in range(nrow):
        for j in range(nrow):
            coord = (matrix[i, ] - matrix[j, ]) ** 2
            dist = (coord.sum()) ** 0.5
            dist_matrix[i, j] = dist
    return dist_matrix


if __name__ == "__main__":

    matrix_1 = np.array([2, 5, 1, 5, 4, 5, 7, 3, 2]).reshape(3, 3)
    matrix_2 = np.array([1, 5, 8, 7, 9, 2, 6, 1, 3]).reshape(3, 3)
    result_matrix = np.array([43, 56, 29, 63, 66, 63, 40, 64, 68]).reshape(3, 3)
    if np.array_equal(matrix_multiplication(matrix_1, matrix_2), result_matrix):
        print("matrix_multiplication: test passed")
    else:
        print("TROUBLE with matrix_multiplication")

    list_of_matrix = [np.ones(2).reshape(2, 1), np.ones(2).reshape(1, 2), np.ones(4).reshape(2, 2),
                      np.ones(8).reshape(2, 4), np.ones(8).reshape(4, 2)]
    if multiplication_check(list_of_matrix) is True:
        print("multiplication_check: test passed")
    else:
        print("TROUBLE with multiplication_check")

    list_of_matrix_2 = [np.array([5, 2, 3, 6]).reshape(2, 2),
                        np.array([2, 1, 2, 3, 4, 5, 6, 3]).reshape(2, 4),
                        np.array([9, 4, 1, 0, 2, 7, 4, 6]).reshape(4, 2)]
    if np.array_equal(np.matmul(np.matmul(list_of_matrix_2[0], list_of_matrix_2[1]), list_of_matrix_2[2]),
                      multiply_matrices(list_of_matrix_2)):
        print("multiply_matrices: test passed")
    else:
        print("TROUBLE with multiply_matrices")

    array_1 = np.array([2, 3])
    array_2 = np.array([7, 8])
    distance_1 = ((7 - 2) ** 2 + (8 - 3) ** 2) ** 0.5
    if distance_1 == compute_2d_distance(array_1, array_2):
        print("compute_2d_distance: test passed")
    else:
        print("TROUBLE with compute_2d_distance")

    array_3 = np.array([8, 9, 14])
    array_4 = np.array([8, 10, 11])
    distance_2 = ((8 - 8) ** 2 + (10 - 9) ** 2 + (11 - 14) ** 2) ** 0.5
    if distance_2 == compute_multidimensional_distance(array_3, array_4):
        print("compute_multidimensional_distance: test passed")
    else:
        print("TROUBLE with compute_multidimensional_distance")

    matrix_3 = np.array([8, 9, 14, 8, 10, 11, 10, 11, 10, 9, 11, 12, 9, 8, 10]).reshape(5, 3)
    distant_matrix = np.array([0.000000, 3.162278, 4.898979, 3.000000, 4.242641, 3.162278, 0.000000, 2.449490,
                               1.732051, 2.449490, 4.898979, 2.449490, 0.000000, 2.236068, 3.162278, 3.000000,
                               1.732051, 2.236068, 0.000000, 3.605551, 4.242641, 2.449490, 3.162278, 3.605551,
                               0.000000]).reshape(5, 5)
    if np.array_equal(np.round_(distant_matrix, decimals=3), np.round_(compute_pair_distances(matrix_3), decimals=3)):
        print("compute_pair_distances: test passed")
    else:
        print("TROUBLE with compute_pair_distances")
