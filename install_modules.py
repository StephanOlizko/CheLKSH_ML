#Загрузим модули из requirements.txt
import os
os.system('pip install -r requirements.txt')

#Проверим, что все модули установились
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import tqdm