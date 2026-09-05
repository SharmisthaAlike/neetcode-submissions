class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in grps:
                grps[key]=[]
            grps[key].append(s)
        return list(grps.values())