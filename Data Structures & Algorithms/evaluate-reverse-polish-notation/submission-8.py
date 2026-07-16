class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = 0
        stk = []
        for op in tokens:
            if op == "+":
                stk.append(int(stk.pop()) + int(stk.pop()))
            elif op == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(int(b - a))
            elif op == "*":
                stk.append(int(stk.pop() * stk.pop()))
            elif op == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(op))
        return int(stk[0])