data = open("input.txt").read()

elves = data.split("\n\n")

max_load = 0
elves_load = []

for elf in elves:
    load = sum([int(load) for load in elf.split()])
    elves_load.append(load)
    max_load = max(load, max_load)

print(max_load)

print(sum(list(reversed(sorted(elves_load)))[:3]))
