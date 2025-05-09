# Python3 Program to convert postfix to prefix

class Solution:
    # function to check if character is operator or not
    def isOperator(self, x):
        return x in ["+", "-", "/", "*"]
    
    # Convert postfix to Prefix expression
    def postToPre(self, post_exp):
        s = []
        
        # length of expression
        length = len(post_exp)
        
        # reading from left to right
        for i in range(length):
            # check if symbol is operator
            if self.isOperator(post_exp[i]):
                # pop two operands from stack
                op1 = s.pop()
                op2 = s.pop()
                
                # concat the operands and operator (prefix form)
                temp = post_exp[i] + op2 + op1
                
                # Push string temp back to stack
                s.append(temp)
            else:
                # push the operand to the stack
                s.append(post_exp[i])
        
        # The final item in stack is the prefix expression
        return s[-1] if s else ""

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        postfix = input().strip()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
# } Driver Code Ends
