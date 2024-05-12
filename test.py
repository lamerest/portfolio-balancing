import numpy as np
from rebalance.v1.strategies.dynamic_convergent_series_distr import DynamicBalancingStrategy


investments = DynamicBalancingStrategy.balance([1, 2, 3], [0.30, 0.20, 0.10])

print(investments)
print('Sum', sum(investments))