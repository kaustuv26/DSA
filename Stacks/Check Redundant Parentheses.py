class Solution:
    def checkRedundancy(self, s):
        stack = []
        for ch in s:
            if ch == ')':
                top = stack.pop()
                redundant = True
                while top != '(':
                    if top in ['+', '-', '*', '/']:
                        redundant = False
                    top = stack.pop()
                if redundant:
                    return 1
            else:
                stack.append(ch)
        return 0


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().checkRedundancy(s))

        print("~")
# } Driver Code Ends
