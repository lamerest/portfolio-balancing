import numpy as np
from variables import INITIAL_VARIANCE, MEAN_APY, AMOUNT_OF_PROJECTS, VARIANCE_APY

def generate_initial_apy():
    result = np.random.normal(MEAN_APY, INITIAL_VARIANCE, AMOUNT_OF_PROJECTS)

    for i in range(len(result)):
        result[i] /= 100
        if result[i] < 0:
            result[i] = 0
            
    return result

#Create array of APY of projects
def generate_apy(apy):
    new_apy = apy.copy()
    
    variance = VARIANCE_APY / 100

    for i in range(len(new_apy)):
        new_apy[i] = np.random.normal(new_apy[i], variance)

        #if the new APY is negative, regenerate it until it is positive
        counter = 0
        while new_apy[i] < 0:
            new_apy[i] = np.random.normal(new_apy[i] + counter * 0.01, variance)
            counter += 1
        

    return new_apy