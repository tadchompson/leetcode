 """
Python

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


 class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')':'(', '}':'{', ']':'[' }
        stack = []
        if len(s) <= 1:
            return False
        for item in s:
            if item in dict.values():
                stack.append(item)
            elif item in dict.keys():
                if stack == [] or dict[item] != stack.pop():
                    return False
            else:
                return False
        return stack == []