#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self, arr):
        stack = []
        max_area = 0
        index = 0
        while index < len(arr):
            if not stack or arr[index] >= arr[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                area = arr[top_of_stack] * width
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = arr[top_of_stack] * width
            max_area = max(max_area, area)
        return max_area


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends
