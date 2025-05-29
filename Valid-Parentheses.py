class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "{":"}",
            "(":")",
            "[":"]"
        }
       
        stack = []
        for p in s:
            if p not in parens:
                if len(stack) > 0:
                    close = stack.pop()
                    if parens[close] != p:
                        return False
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0        