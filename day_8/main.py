def get_matrix():
    matrix = []
    lines = [line.strip() for line in open("input.txt").readlines()]
    for line in lines:
        matrix.append([int(tree_height) for tree_height in line])

    return matrix
