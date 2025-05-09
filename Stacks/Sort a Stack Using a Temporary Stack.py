class Solution:
    def sorted(self, stack):
        tmpStack = []
        while stack:
            # Pop from the original stack
            tmp = stack.pop()
            
            # While temporary stack is not empty and top is less than tmp
            while tmpStack and tmpStack[-1] < tmp:
                # Move elements back to original stack
                stack.append(tmpStack.pop())
            
            # Push tmp to temporary stack
            tmpStack.append(tmp)
        
        # Copy the sorted elements back to the original stack (in descending order)
        while tmpStack:
            stack.append(tmpStack.pop())

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        # Print from top to bottom (largest to smallest)
        while arr:
            print(arr.pop(), end=" ")
        print()
# } Driver Code Ends
