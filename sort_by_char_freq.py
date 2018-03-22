"""
Given a string, sort it in decreasing order based on the frequency of characters.
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        h_map = {}
        answer = ""
        """
        parent = (index)//2
        child = index*2 +1 or +2
        """
        for char in s:
            if char not in h_map:
                h_map[char] = 1
            else:
                h_map[char] +=1
        sorted_h_map = sorted(h_map.items(), key= lambda kv:kv[1], reverse = True )
        for key, item in sorted_h_map:
            answer += key*item
        return answer
