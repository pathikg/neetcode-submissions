class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for element in num:
            while k > 0 and stack and int(stack[-1]) > int(element):
                k -= 1
                stack.pop()
            stack.append(element)
        stack = stack[:len(stack) - k]


        return ''.join(stack).lstrip('0') or '0'