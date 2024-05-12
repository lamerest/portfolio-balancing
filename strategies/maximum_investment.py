import numpy as np
from utils import deduct_balancing_fee, find_index_of_max

class DynamicMaximumStrategy:
    def distribute(investments_amount, initial_APYs):
        investments = [0.0] * len(initial_APYs)

        investments[0] = investments_amount
        
        distribution = DynamicMaximumStrategy.balance(investments, initial_APYs)
        
        return distribution
    

    def balance(investments, APYs):
        total_value = sum(investments)

        total_value = deduct_balancing_fee(total_value)

        new_investments = [0] * len(APYs)
        
        idx = find_index_of_max(APYs)
            
        new_investments[idx] = total_value

        return new_investments