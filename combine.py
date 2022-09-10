from astropy.cosmology import FlatLambdaCDM
cos737 = FlatLambdaCDM(H0=70, Om0=0.3)
from astropy.table import Table
import astropy.units as u
import os
from scipy import stats
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
import pickle as pkl
import numpy as np
import sys
from math import gamma
from tqdm import tqdm
from scipy.special import gammaincc
import glob
import pandas as pd


csv_files = sorted([i for i in glob.iglob('data/2022-06/*.csv', recursive=True)])
combined_csv = pd.concat([pd.read_csv(i) for i in csv_files], ignore_index=True)
combined_csv.to_csv( "combined_2022-06.csv", index=False)

#index_arr = [int(i.split(' ')[0]) for i in combined_csv['observe_time']]

data = Table.read('combined_2022-06.csv')


keys = []
keys_date = ['2022-06-'+str(i).rjust(2,'0') for i in range(1,31)]
keys_time = []
for hrs in range(24):
    for mins in range(0,60,10):
        comb_str = str(hrs).rjust(2, '0')+':'+str(mins).rjust(2, '0')+':00+00:00'
        keys_time.append(comb_str)
for d in keys_date:
    for t in keys_time:
        keys.append(d+' '+t)

# deal with redundant data
index_excess  = [i for i in range(len(data)) if data['observe_time'][i] not in keys]
if len(index_excess) > 0:
    data.remove_rows(index_excess)

# deal with missing data
index_missing = [i for i in range(len(keys)) if keys[i] not in data['observe_time']]
keys_missing = [keys[i] for i in index_missing]

keys_fill = []
for i in index_missing:
    key_missing = keys[i]
    if ':00:00+00:00' in key_missing:
        if keys[i-1] in data['observe_time']:
            key_fill = keys[i-1]
            index_replace = list(data['observe_time']).index(key_fill)
            value_fill = data[index_replace]
            value_fill['observe_time'] = key_missing
        elif keys[i+1] in data['observe_time']:
            key_fill = keys[i+1]
            index_replace = list(data['observe_time']).index(key_fill)
            value_fill = data[index_replace]
            value_fill['observe_time'] = key_missing
        else:
            value_fill = [key_missing, [np.nan]* (len(data.columns)-1)]
        data.add_row(value_fill) 


data.sort('observe_time')
data.write('data_2022-06.csv')






