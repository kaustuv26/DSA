class Solution:
    def reverse(self, s):
        # Create an empty stack
        stack = []
        
        # Push all characters of the string onto the stack
        for char in s:
            stack.append(char)
        
        # Pop characters from the stack and build the reversed string
        reversed_str = ''
        while stack:
            reversed_str += stack.pop()
        
        return reversed_str

# Calling the function 
if __name__ == "__main__":
    t = int(input())
    sol = Solution()

    for _ in range(t):
        s = input()
        print(sol.reverse(s))
        print("~")
