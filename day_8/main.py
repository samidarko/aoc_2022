def get_matrix():
    matrix = []
    lines = [line.strip() for line in open("input.txt").readlines()]
    for line in lines:
        matrix.append([int(tree_height) for tree_height in line])

    return matrix


def get_column(matrix, col_index):
    return [matrix[row_index][col_index] for row_index in range(len(matrix))]


def main():
    matrix = get_matrix()
    total_visible = 0
    for row_index, row in enumerate(matrix):
        for col_index, tree_height in enumerate(row):
            if (
                    row_index == 0
                    or row_index == len(matrix) - 1
                    or col_index == 0
                    or col_index == len(matrix) - 1
            ):
                # all the trees around the edge of the grid are visible
                total_visible += 1
                continue

            if all([item < tree_height for item in row[:col_index]]):
                total_visible += 1
                continue

            if all([item < tree_height for item in row[col_index + 1:]]):
                total_visible += 1
                continue

            column = get_column(matrix, col_index)
            if all([item < tree_height for item in column[:row_index]]):
                total_visible += 1
                continue

            if all([item < tree_height for item in column[row_index + 1:]]):
                total_visible += 1
                continue
    print(total_visible)


if __name__ == "__main__":
    main()
