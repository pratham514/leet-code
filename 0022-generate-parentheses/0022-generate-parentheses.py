class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_count: int, close_count: int, current_str: list):
            # Base Case: Valid combination complete
            if open_count == n and close_count == n:
                result.append("".join(current_str))
                return

            # Add open parenthesis if allowed
            if open_count < n:
                current_str.append("(")
                backtrack(open_count + 1, close_count, current_str)
                current_str.pop()  # Backtrack

            # Add close parenthesis if allowed
            if close_count < open_count:
                current_str.append(")")
                backtrack(open_count, close_count + 1, current_str)
                current_str.pop()  # Backtrack

        backtrack(0, 0, [])
        return result
        