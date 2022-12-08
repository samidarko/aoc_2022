from dataclasses import dataclass
from typing import List, Union

lines = [line.strip() for line in open("input.txt").readlines()]


@dataclass
class File:
    name: str
    size: int

    @staticmethod
    def is_directory() -> bool:
        return False

    @staticmethod
    def is_file() -> bool:
        return True

    def get_size(self) -> int:
        # make it a property
        return self.size


@dataclass
class Directory:
    name: str
    files: List[Union["Directory", File]]

    @staticmethod
    def is_directory() -> bool:
        return True

    @staticmethod
    def is_file() -> bool:
        return False

    def __getitem__(self, name):
        for file in self.files:
            if file.name == name:
                return file
        raise KeyError(name)

    def mkdir(self, name) -> "Directory":
        """create dire if not exists"""
        for file in self.files:
            if file.name == name:
                return file
        directory = Directory(name, [])
        self.files.append(directory)
        return directory

    def mkfile(self, name: str, size: int) -> File:
        file = File(name, size)
        self.files.append(file)
        return file

    def ls(self):
        return [file.name for file in self.files]

    def get_size(self) -> int:
        # make it a property
        return sum([file.get_size() for file in self.files])


def create_file_system() -> Directory:
    fs = Directory("/", [])

    directory_stack = [fs]

    for line in lines:
        current_directory = directory_stack[-1]
        if line[0] == "$":
            command = line[2:]
            if command == "cd ..":
                directory_stack.pop()
                continue
            if command.startswith("cd "):
                directory_name = command[3:]
                directory = current_directory.mkdir(directory_name)
                directory_stack.append(directory)

            continue

        if line.startswith("dir "):
            directory_name = line[4:]
            _ = current_directory.mkdir(directory_name)

        if line[0].isdigit():  # precarious assumption
            size, name = line.split()
            _ = current_directory.mkfile(name, int(size))

    return fs


def part_one(directory: Directory):
    total = 0
    size = directory.get_size()
    if size <= 100000:
        total += size
    for file_name in directory.ls():
        file = directory[file_name]
        if file.is_directory():
            total += part_one(file)

    return total


def part_two(directory: Directory, minimum: int):
    result = 0
    size = directory.get_size()
    if size >= minimum:
        result = size
    for file_name in directory.ls():
        file = directory[file_name]
        if file.is_directory():
            size = part_two(file, minimum)
            if size >= minimum:
                result = min(result, size)

    return result


def main():
    fs = create_file_system()
    total = part_one(fs)
    assert total == 1583951
    print(total)

    minimum_space_to_free = 30000000 - (70000000 - fs.get_size())

    minimum_size_directory = part_two(fs, minimum_space_to_free)
    assert minimum_size_directory == 214171

    print(minimum_size_directory)


if __name__ == "__main__":
    main()
