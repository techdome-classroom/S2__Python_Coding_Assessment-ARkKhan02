class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to store opening brackets
        stack = []
        
        # Hash map to match closing brackets with their corresponding opening ones
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop from stack if it's not empty; otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched properly
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))      # Output: False







    



  

