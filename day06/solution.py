def part1(data):
    lines = []
    for line in data.splitlines():
        lines.append([char for char in line.split() if char])

    length = len(data.splitlines())
    count = len(lines[0])
    total = 0

    for i in range(count):
        op = lines[-1][i]
        result = int(lines[0][i])
        for j in range(1, length - 1):
            result = operate(result, int(lines[j][i]), op)

        total += result

    return total


def operate(a, b, op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        raise ValueError("Invalid operation")


def part2(data):
    lines = data.split("\n")

    # Pad lines to the same length
    maxWidth = max(len(line) for line in lines)
    paddedLines = [line.ljust(maxWidth) for line in lines]

    operatorLine = paddedLines[-1]
    dataLines = paddedLines[:-1]

    problems = []
    currentProblemCols = []

    # Process columns from right to left
    for colIdx in range(maxWidth - 1, -1, -1):
        # Gather characters in this column, e.g., [' ', ' ', '4']
        colChars = [line[colIdx] for line in dataLines]
        operatorChar = operatorLine[colIdx]

        # Check if this column is a separator (all spaces)
        isSeparator = all(c == ' ' for c in colChars) and operatorChar == ' '
        if isSeparator:
            if currentProblemCols:
                # Append the current problem columns to the problems list, e.g., [[([' ', ' ', '4'], '_'), (['4', '3', '1'], ' '), (['6', '2', '3'], '+')], ...]
                problems.append(currentProblemCols)
                currentProblemCols = []
        else:
            # Append the current column characters and operator character as a tuple, (e.g., ([' ', ' ', '4'], ' '))
            currentProblemCols.append((colChars, operatorChar))

    if currentProblemCols:
        problems.append(currentProblemCols)

    total = 0
    for problemCols in problems:
        operator = problemCols[-1][1]

        numbers = []
        # Extract numbers from the columns
        for colChars, _ in problemCols:
            digitStr = "".join(c for c in colChars if c.isdigit())
            if digitStr:
                numbers.append(int(digitStr))

        if operator == "+":
            result = sum(numbers)
        elif operator == "*":
            result = 1
            for n in numbers:
                result *= n

        total += result

    return total

with open("day06/input.txt") as f:
    data = f.read().strip()

print("part 1:", part1(data))
print("part 2:", part2(data))
