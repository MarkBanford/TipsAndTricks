def flatten(matrix):
    flattened = []
    for row in matrix:
        for item in row:
            flattened.append(item)
    return flattened


def list_comp_flatten(matrix):
    return [
        item
        for row in matrix  # outer loop goes first
        for item in row
    ]


def negative_matrix(matrix):
    return [
        -item
        for row in matrix
        for item in row

    ]


if __name__ == '__main__':
    matrix = [[1, -2, 4], [2, 4, 6], [4, -6, 9]]

    print(flatten(matrix=matrix))
    print(list_comp_flatten(matrix=matrix))
    print(negative_matrix(matrix=matrix))
