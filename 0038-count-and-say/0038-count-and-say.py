class Solution:
    def countAndSay(self, n: int) -> str:
        
        s = "1"
        
        for _ in range(n - 1):
            next_s = []
            count = 1
            
            for j in range(len(s)):
                
                if j + 1 < len(s) and s[j] == s[j + 1]:
                    count += 1
                else:
                    
                    next_s.append(str(count))
                    next_s.append(s[j])
                    count = 1  
                    
            s = "".join(next_s)
            
        return s