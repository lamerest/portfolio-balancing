import numpy as np

from variables import AMOUNT_OF_PROJECTS, PRICE_OF_REBALANCE

def sort_downsize(arr):
    return np.sort(arr)[::-1]

def accrue_yield(investments, apy):
    for project_id in range(AMOUNT_OF_PROJECTS):
        investments[project_id] = investments[project_id] * (1 + apy[project_id] / 365)

    return investments


def format_percent(number: float | int) -> str:
    return "%.2f" % (number * 100)


def deduct_balancing_fee(investments_value):
    return investments_value * (1 - PRICE_OF_REBALANCE)


def find_index_of_max(list):
    sorted_list = np.sort(list)[::-1]
    element = sorted_list[0]
    index = np.where(list == element)
    return index[0][0]

def find_index_of_min(list):
    sorted_list = np.sort(list)
    element = sorted_list[0]
    index = np.where(list == element)
    return index[0][0]