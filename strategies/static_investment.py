class StaticUnevenDistributionStrategy:
    def distribute(investments_amount, initial_APYs):
        distribution = []

        for i in range(len(initial_APYs)):
            # 50%, 25%, 12.5%, ...
            distribution.append(investments_amount * (1/2)**(i+1))

            # For last project copy previous amount to invest leftovers
            if i == len(initial_APYs) - 1:
                distribution.append(distribution[i-1])
        
        return distribution
    

    # No balancing = static
    def balance(investments, APYs):
        return investments
    

class StaticUniformDistributionStrategy:
    def distribute(investments_amount, initial_APYs):
        projects_amount = len(initial_APYs)

        distribution = []

        for i in range(len(initial_APYs)):
            distribution.append(investments_amount / projects_amount)
        
        return distribution
    
    # No balancing = static
    def balance(investments, APYs):
        return investments