class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        
        if total_gas < total_cost:
            return -1
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0
        
        return start_station
        
