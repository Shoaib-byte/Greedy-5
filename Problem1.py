#time complexity o(m+n)
#space complexity o(1)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pl = len(p)
        sl = len(s)
        sp = 0
        pp = 0
        sStar = -1
        pStar = -1

        while sp < sl:
            if pp < pl and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < pl and p[pp] == '*':
                sStar = sp
                pStar = pp
                pp += 1 #asssume 0 character match
            elif pStar == -1:
                return False
            else:
                sStar += 1
                sp = sStar
                pp = pStar + 1
        
        while pp < pl:
            if p[pp] == '*':
                pp += 1
            else:
                return False
        
        return True

