# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:50:25 2023

@author: Tydox
"""

import numpy as np
import pandas as pd
import time

def main():
    filePath = r"data.csv"
    df = pd.read_csv(filePath)
    df_grades = df.loc[:,"grade"]
    df_weights = df.loc[:,"weight"]

    if(len(df_grades) != len(df_weights)):
        print('Error in handling data,mismatching data legnths')
        exit 

    grades = np.array(df_grades)[:,np.newaxis]
    weights= np.array(df_weights)[:,np.newaxis]
    weightsSum = np.sum(weights,axis=0)
    GPA = ( (grades.T @ weights) / weightsSum )[0][0]

    print(f'AVG GPA: {GPA:.2f}')    
    return
    
if __name__ == "__main__":
    st = time.time()
    main()
    print(f'\nRuntime: {(time.time() - st)*1000:.04f} [ms]')



