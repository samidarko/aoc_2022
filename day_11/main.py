from typing import List
from dataclasses import dataclass


@dataclass
class Monkey:
    items: List[int]
    operator: str
    operand: int
    modulo: int
    on_true: int
    on_false: int
    total_inspected: int = 0
    relief: int = 1

    def add_item(self, item):
        self.items.append(item)

    def inspect(self):
        inspected_items = []
        for item in self.items:
            self.total_inspected += 1
            match self.operator:
                case "**":
                    item = item * item
                case "*":
                    item = item * self.operand
                case "+":
                    item = item + self.operand
            item = item // self.relief
            monkey = self.on_true if item % self.modulo == 0 else self.on_false
            inspected_items.append((monkey, item))
        self.items = []
        return inspected_items


def get_monkeys(filename: str, relief: int) -> List[Monkey]:
    monkeys = []
    for notes in open(filename).read().split("\n\n"):
        lines = notes.split("\n")
        items = lines[1].replace("  Starting items: ", "").replace(",", "").split()
        items = [int(item) for item in items]
        operator = "*" if "*" in lines[2] else "+"
        if lines[2].split(" ")[-1] == "old":
            operator = "**"
            operand = 0
        else:
            operand = int(lines[2].split(" ")[-1])
        modulo = int(lines[3].split()[-1])
        on_true = int(lines[4].split()[-1])
        on_false = int(lines[5].split()[-1])
        monkey = Monkey(
            items=items, operator=operator, operand=operand, modulo=modulo,
            on_true=on_true, on_false=on_false, relief=relief)
        monkeys.append(monkey)
    return monkeys


def part_one():
    monkeys = get_monkeys("input.txt", 3)
    for _ in range(20):
        # round
        for sender_monkey in range(len(monkeys)):
            for receiver_monkey, inspected_item in monkeys[sender_monkey].inspect():
                monkeys[receiver_monkey].add_item(inspected_item)

    return monkeys


def part_two():
    monkeys = get_monkeys("test_input.txt", 1)
    for i in range(1000):
        # round
        for sender_monkey in range(len(monkeys)):
            for receiver_monkey, inspected_item in monkeys[sender_monkey].inspect():
                monkeys[receiver_monkey].add_item(inspected_item)

    return monkeys


def main():
    monkeys = part_one()
    two_most_active = list(
        reversed(sorted([monkey.total_inspected for monkey in monkeys])))[:2]
    monkey_business_level = two_most_active[0] * two_most_active[1]
    assert monkey_business_level == 113220
    print(monkey_business_level)
    # part_two()


if __name__ == "__main__":
    main()
