def calculate(s: str) -> int:
    def update(op, num):
        if op == '+':
            return num
        elif op == '-':
            return -num

    stack = []
    num = 0
    sign = '+'
    res = 0
    i = 0

    while i < len(s):
        char = s[i]

        if char.isdigit():
            num = num * 10 + int(char)

        elif char in '+-':
            res += update(sign, num)
            num = 0
            sign = char

        elif char == '(':
            # Push current result and sign to stack
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = '+'

        elif char == ')':
            res += update(sign, num)
            num = 0
            prev_sign = stack.pop()
            prev_res = stack.pop()
            res = prev_res + update(prev_sign, res)

        i += 1

    res += update(sign, num)
    return res

print(calculate("1 + 1"))               # Output: 2
print(calculate(" 2-1 + 2 "))           # Output: 3
print(calculate("(1+(4+5+2)-3)+(6+8)")) # Output: 23
print(calculate("-1 + 2"))             # Output: 1
print(calculate("-(3+(2-1))"))         # Output: -4
