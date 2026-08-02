class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def backtrack(index: int, path: list):
            # Base case: completed a full combination
            if index == len(digits):
                result.append("".join(path))
                return

            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)          # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()                  # Backtrack

        backtrack(0, [])
        return result
        