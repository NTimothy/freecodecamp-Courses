# Puzzle Prompt https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def check(problems):
    # Creates 3 lists containing operands and operators
    operand_1 = []
    operand_2 = []
    operator = []
    for i in problems:
        x = i.split(" ")
        try:
            operand_1.append(x[0])
            operand_2.append(x[2])
            operator.append(x[1])
        except IndexError:
            # Checks if operands are separated from the operator with a space
            return "Error: Numbers must be separated by a single space."

    _count = 0
    # Limits to addition/subtraction operations
    for op in operator:
        if op == "+" or op == "-":
            _count += 1
        else:
            return "Error: Operator must be '+' or '-'."

    # Limits max number of problems (5)
    if _count > 5:
        return "Error: Too many problems."

    # Limit characters in 1st operand to only digits
    for num in operand_1:
        try:
            _num = int(num)
            if abs(_num) > 9999:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."

    # Limit characters in 2nd operand to only digits
    for num in operand_2:
        try:
            _num = int(num)
            if abs(_num) > 9999:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."
    return [operand_1, operand_2, operator]


def arithmetic_arranger(problems, solved):
    ans = []
    # Solves and arranges problems if passes checks or returns error if found
    _check = check(problems)
    if not isinstance(_check, str):
        op1 = _check[0]
        op2 = _check[1]
        op = _check[2]
        if solved:
            ans = []
            for _op in range(len(op)):
                if op[_op] == "+":
                    _total = int(op1[_op]) + int(op2[_op])
                    ans.append(_total)
                elif op[_op] == "-":
                    _total = int(op1[_op]) - int(op2[_op])
                    ans.append(_total)
    else:
        return _check

    _num = len(op)
    i = 0
    _topline = ""
    _botline = ""
    _barline = ""
    _ansline = ""
    while i < _num:
        _space = 4*' '
        if i == _num-1:
            _space = ''
        _totalspace = max(len(op1[i]), len(op2[i])) + 2
        _emptyspace1 = _totalspace - len(op1[i])
        _emptyspace2 = _totalspace - len(op2[i]) - 1
        _topline += f"{_emptyspace1*' '}{op1[i]}{_space}"
        _botline += f"{op[i]}{_emptyspace2*' '}{op2[i]}{_space}"

        _bar = _totalspace*'-'
        _barline += f"{_bar}{_space}"

        if solved:
            _ansspace = _totalspace - len(str(ans[i]))
            _ansline += f"{_ansspace*' '}{ans[i]}{_space}"

        i += 1
    if solved:
        print(f"{_topline}\n{_botline}\n{_barline}\n{_ansline}")
    else:
        print(f"{_topline}\n{_botline}\n{_barline}")


test_input = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(test_input, True)


