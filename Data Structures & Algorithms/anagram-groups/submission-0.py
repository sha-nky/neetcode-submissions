class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            track = [0] * 26
            for char in s:
                track[ord(char) - ord('a')] += 1
            
            result[str(track)].append(s)
        
        return list(result.values())
