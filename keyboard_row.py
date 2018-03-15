"""
Given a List of words, return the words that can be typed using letters
of alphabet on only one row's of American keyboard like the image below.

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lines = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        answer = []
        for word in words:
            w = set(word.lower())
            for line in lines:
                if w.issubset(line):
                    answer.append(word)
        return answer
