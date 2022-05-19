"""
link: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_parenthesis = ['(', '{', '[']
        close_parenthesis = [')', '}', ']']
        stack = []
        for parenthesis in s:
            if parenthesis in open_parenthesis:
                stack.append(parenthesis) # (,
            elif parenthesis in close_parenthesis:
                position = close_parenthesis.index(parenthesis)  # 0 = )
                if len(stack) > 0 and (open_parenthesis[position] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False



s = "(){{()}}"
solution = Solution()
print(solution.isValid(s))