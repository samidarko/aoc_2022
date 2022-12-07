lines = [line.strip() for line in open("input.txt").readlines()]

fs = {}

# directory is just a dict
# a file is a key with value
# every time when change of directory: keep state in stack
# so cd .. does a pop
# workdir can be found with peek()

directory_stack = []

for line in lines:
    if line[0] == "$":
        command = line[2:]
        if command == "cd ..":
            directory_stack.pop()
            continue
        if command.startswith("cd "):
            directory = command[3:]
            directory_stack.append(directory)
            fs[directory] = {}
            continue
        if command == "ls":
            continue

    current_directory = directory_stack[-1]
    if line.startswith("dir "):
        directory = line[4:]
        fs[current_directory][directory] = {}

    if line[0].isdigit():   # precarious assumption
        size, file = line.split()
        fs[current_directory][file] = int(size)
