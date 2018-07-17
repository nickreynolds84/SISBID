import pandas as pd
import numpy as np
import csv, os, random

url = 'https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv'
df = pd.read_csv(url)

karls = df[df['name'] == 'Karl']
carls = df[df['name'] == 'Carl']

all_carls = pd.concat([karls,carls], ignore_index=True)

