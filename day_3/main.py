import string

data = open("input.txt").readlines()

priorities_sum = 0

for line in data:
    middle = len(line)//2
    compartment_a, compartment_b = line[:middle], line[middle:]
    common_items = set(compartment_a).intersection(set(compartment_b))
    assert len(common_items) == 1
    priorities_sum += string.ascii_letters.index(list(common_items)[0]) + 1

print(priorities_sum)