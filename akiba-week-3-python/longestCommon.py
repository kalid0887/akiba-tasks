
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for word in strs[1:]:
            i = 0

            while i < len(prefix) and i < len(word):
                if prefix[i] != word[i]:
                    break
                i += 1

            prefix = prefix[:i]

            if prefix == "":
                return ""

        return prefix
