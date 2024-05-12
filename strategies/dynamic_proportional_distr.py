import numpy as np
from utils import deduct_balancing_fee, find_index_of_max

class DynamicProportionalDistributionStrategy:
    def distribute(investments_amount, initial_APYs):
        investments = [0.0] * len(initial_APYs)

        for i in range(len(initial_APYs)):
            investments[i] = investments_amount / len(initial_APYs)
        
        distribution = DynamicProportionalDistributionStrategy.balance(investments, initial_APYs)
        
        return distribution
    

    def balance(investments, APYs):
        total_value = sum(investments)

        total_value = deduct_balancing_fee(total_value)

        new_investments = [0] * len(APYs)

        APYs_sum = sum(APYs)
        
        for i in range(len(new_investments)):
            new_investments[i] = total_value * APYs[i] / APYs_sum

        return new_investments