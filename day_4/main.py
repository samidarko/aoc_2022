data = [line.strip() for line in open("input.txt").readlines()]

def get_sections_set(line: str) -> tuple[set, set]:
    sections_a, sections_b = line.split(',')
    a_start, a_end = [int(_id) for _id in sections_a.split('-')]
    b_start, b_end = [int(_id) for _id in sections_b.split('-')]
    return set(range(a_start, a_end+1)), set(range(b_start, b_end+1))

fully_overlapping_assignment = 0
overlapping_assignment = 0

for line in data:
    set_a, set_b = get_sections_set(line)
    intersection = set_b.intersection(set_a)
    if intersection:
        overlapping_assignment += 1
    # I used the code below in part 1 but after doing part 2, I reused intersection
    # if set_a.issubset(set_b) or set_b.issubset(set_a):
    #     fully_overlapping_assignment += 1
    # also I could compare the sets together but that's probably O(n)
    # if set_a == intersection or set_b == intersection:
    #     fully_overlapping_assignment += 1
    # I can just compare sized with len() being O(1)
    if len(set_a) == len(intersection) or len(set_b) == len(intersection):
        fully_overlapping_assignment += 1

print(fully_overlapping_assignment)
assert fully_overlapping_assignment == 651

print(overlapping_assignment)
assert overlapping_assignment == 956
