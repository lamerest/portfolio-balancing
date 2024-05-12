import numpy as np
from generate import generate_apy, generate_initial_apy
from strategies.minimum_investment import DynamicMinimumStrategy
from strategies.dynamic_proportional_distr import DynamicProportionalDistributionStrategy
from strategies.maximum_investment import DynamicMaximumStrategy
from utils import accrue_yield
from variables import AMOUNT_OF_TESTS, DURATION_OF_INVESTMENT, FREQUENCY_OF_CHANGE_APY, INITIAL_VALUE, REBALANCE_FREQUENCY
from strategies.dynamic_convergent_series_distr import DynamicBalancingStrategy
from strategies.static_investment import StaticUnevenDistributionStrategy, StaticUniformDistributionStrategy
from result import show_results

#Set the random seed
# np.random.seed(42)
    

def main():
    strategies = {
        # "profit_static_uneven": StaticUnevenDistributionStrategy,
        "profit_static_uniform": StaticUniformDistributionStrategy,
        "profit_dynamic": DynamicBalancingStrategy,
        "profit_max": DynamicMaximumStrategy,
        # "profit_dynamic_proportional_distribution": DynamicProportionalDistributionStrategy,
        # "profit_min": DynamicMinimumStrategy
    }

    results = {}

    for i in range(AMOUNT_OF_TESTS):
        project_investments_by_strategy = {}

        (investment_results, APYs) = test_strategies(strategies, INITIAL_VALUE, project_investments_by_strategy)
        
        # Calculate results
        for strategy in strategies:
            if strategy not in results.keys():
                results[strategy] = []

            results[strategy].append((investment_results[strategy] - INITIAL_VALUE) / INITIAL_VALUE)

    show_results(results)


def test_strategies(strategies, initial_value, project_investments_by_strategy):
    APYs = []
    initial_apy = generate_initial_apy()
    APYs.append(initial_apy)

    # initial distribution for every strategy

    for strategy in strategies:
        Impl = strategies[strategy]
        project_investments = Impl.distribute(initial_value, initial_apy)
        project_investments_by_strategy[strategy] = project_investments

    apy = initial_apy


    for day in range(DURATION_OF_INVESTMENT):
        APYs.append(simulate_day(day, strategies, apy, project_investments_by_strategy))

    results = {}

    for strategy in strategies:
        results[strategy] = np.sum(project_investments_by_strategy[strategy])

    return (results, APYs)


def simulate_day(day, strategies, apy, project_investments_by_strategy):
    # accrue yield
    accrue_yields(apy, project_investments_by_strategy)

    # generate new APYs
    apy = generate_new_APYs(day, apy)

    # balance
    balance_strategies(day, strategies, apy, project_investments_by_strategy)
    return apy


def accrue_yields(apy, project_investments_by_strategy):
    for strategy in project_investments_by_strategy:
        investments = project_investments_by_strategy[strategy]
        investments = accrue_yield(investments, apy)


def generate_new_APYs(day, apy):
    if day % FREQUENCY_OF_CHANGE_APY == 0 and day != 0 :
        return generate_apy(apy)
    
    return apy


def balance_strategies(day, strategies, apy, project_investments_by_strategy):
    if day % REBALANCE_FREQUENCY == 0 or day != 0:
        return
    
    for strategy in strategies:
        strategies[strategy]
        Impl = strategies[strategy]
        investments = project_investments_by_strategy[strategy]
        investments = Impl.balance(investments, apy)


if __name__ == "__main__":
    main()