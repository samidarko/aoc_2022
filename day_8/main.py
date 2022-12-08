def get_matrix():
    matrix = []
    lines = [line.strip() for line in open("input.txt").readlines()]
    for line in lines:
        matrix.append([int(tree_height) for tree_height in line])

    return matrix


def get_column(matrix, col_index):
    return [matrix[row_index][col_index] for row_index in range(len(matrix))]


def part_one(matrix) -> int:
    total_visible = 0
    for row_index, row in enumerate(matrix):
        for col_index, tree_height in enumerate(row):
            if (
                    row_index == 0
                    or col_index == 0
                    or row_index == len(matrix) - 1
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
    return total_visible


def get_viewing_distance(trees, tree_height: int) -> int:
    viewing_distance = 0
    for height in trees:
        viewing_distance += 1
        if height >= tree_height:
            break

    return viewing_distance


def part_two(matrix) -> int:
    max_scenic_score = 0
    for row_index, row in enumerate(matrix):
        for col_index, tree_height in enumerate(row):
            if (
                    row_index == 0
                    or col_index == 0
                    or row_index == len(matrix) - 1
                    or col_index == len(matrix) - 1
            ):
                # all the trees around the edge of the grid are visible
                continue
            left_scene, right_scene = row[:col_index], row[col_index + 1:]

            right_viewing_distance = get_viewing_distance(right_scene, tree_height)

            left_viewing_distance = get_viewing_distance(
                reversed(left_scene), tree_height)

            column = get_column(matrix, col_index)
            down_scene, up_scene = column[:row_index], column[row_index + 1:]

            down_viewing_distance = get_viewing_distance(
                reversed(down_scene), tree_height)

            up_viewing_distance = get_viewing_distance(up_scene, tree_height)

            scenic_score = (
                    left_viewing_distance
                    * right_viewing_distance
                    * down_viewing_distance
                    * up_viewing_distance
            )

            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


def main():
    matrix = get_matrix()
    total_visible = part_one(matrix)
    print(total_visible)
    assert total_visible == 1796
    scenic_score = part_two(matrix)
    assert scenic_score == 288120
    print(scenic_score)


if __name__ == "__main__":
    main()
