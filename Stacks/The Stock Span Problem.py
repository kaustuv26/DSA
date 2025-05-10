def calculate_span(arr):
    n = len(arr)
    stack = []
    span = [0] * n
    span[0] = 1  # Span of first day is always 1
    stack.append(0)  # Push index of first day

    for i in range(1, n):
        # Pop elements from stack while stack is not empty and top of stack is less than or equal to arr[i]
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # If stack becomes empty, then price at i is greater than all previous prices
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)  # Push this element to stack

    return span

# Example usage
arr = [100, 80, 60, 70, 60, 75, 85]
print(calculate_span(arr))  # Output: [1, 1, 1, 2, 1, 4, 6]
