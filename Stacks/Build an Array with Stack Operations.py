class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        operations = []
        current = 1  # The current number in the stream
        index = 0     # The current index in the target array
        
        while index < len(target) and current <= n:
            operations.append("Push")
            if current == target[index]:
                index += 1
            else:
                operations.append("Pop")
            current += 1
        
        return operations
