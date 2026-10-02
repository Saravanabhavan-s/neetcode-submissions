class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s1=Counter(s)
        s2=Counter(t)
        x=sorted(s1.items())
        y=sorted(s2.items())
        return (x==y)