import numpy as np
from utils import deduct_balancing_fee, find_index_of_max

class DynamicBalancingStrategy:
    def distribute(investments_amount, initial_APYs):
        investments = [0.0] * len(initial_APYs)

        for i in range(len(initial_APYs)):
            investments[i] = investments_amount / len(initial_APYs)
        
        distribution = DynamicBalancingStrategy.balance(investments, initial_APYs)
        
        return distribution
    

    def balance(investments, APYs):        
        total_value = sum(investments)

        total_value = deduct_balancing_fee(total_value)

        new_investments = [0] * len(APYs)

        APYs_copy = APYs.copy()
        last_known_value = 0
        
        for i in range(len(APYs)):
            idx = find_index_of_max(APYs_copy)

            if i == len(APYs_copy) - 1:
                new_investments[idx] = last_known_value
                continue
            
            APYs_copy[idx] = -1
            new_investments[idx] = total_value * (1/2)**(i+1)
            last_known_value = new_investments[idx]

        return new_investments
