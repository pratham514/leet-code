class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_result = 0
        
        for char in s:
            xor_result ^= ord(char)
            
        for char in t:
            xor_result ^= ord(char)
            
        return chr(xor_result)