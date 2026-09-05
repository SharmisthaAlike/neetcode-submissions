class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            key = tuple(count)
            if key not in grps:
                grps[key]=[]

            grps[key].append(s)
        return list(grps.values())