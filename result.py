import numpy as np
import matplotlib.pyplot as plt
from utils import format_percent

def show_results(results):
    plt.xlabel('Test')
    plt.ylabel('Profit')

    for result in results.items():
        plt.plot(result[1], label=result[0])
        mean = result[1][0]
        print(f'Mean profit "{result[0]}": {format_percent(mean)}%')

    plt.title('Profit by test')
    plt.legend()
    plt.show()

def plot_APYs(APYs):
    plt.xlabel('Test')
    plt.ylabel('Project APY')
    
    plt.plot(APYs)

    plt.title('Profit by test')
    plt.legend()
    plt.show()