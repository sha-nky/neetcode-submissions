class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track = [0] * 26
        for char in s:
            track[ord(char)-ord('a')] += 1
        
        for char in t:
            track[ord(char)-ord('a')] -= 1
        
        for num in track:
            if num != 0:
                return False
        
        return True
