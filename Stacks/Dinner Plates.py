import heapq

class DinnerPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.available = []  # heap to keep track of available stack indices

    def push(self, val):
        while self.available:
            index = heapq.heappop(self.available)
            if index < len(self.stacks) and len(self.stacks[index]) < self.capacity:
                self.stacks[index].append(val)
                if len(self.stacks[index]) < self.capacity:
                    heapq.heappush(self.available, index)
                return
        # No available stacks, create a new one
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)
        if len(self.stacks[-1]) < self.capacity:
            heapq.heappush(self.available, len(self.stacks) - 1)

    def pop(self):
        # Remove empty stacks from the end
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        # If the stack was full before popping, add it back to available
        if len(self.stacks[-1]) == self.capacity - 1:
            heapq.heappush(self.available, len(self.stacks) - 1)
        return val

    def popAtStack(self, index):
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        # If the stack was full before popping, add it back to available
        if len(self.stacks[index]) == self.capacity - 1:
            heapq.heappush(self.available, index)
        return val
