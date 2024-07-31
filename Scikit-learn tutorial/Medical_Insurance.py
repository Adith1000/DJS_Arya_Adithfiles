from urllib.request import urlretrieve
import pandas as pd
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

medical_df=pd.read_csv("/Users/adithshetty/Desktop/Programming Folder/Python Programming/Machine Learning Tutorials/Medical_data.csv")

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

non_smoker_df=medical_df[medical_df.smoker == 'no']

def estimate_charges(age, w, b):
    return w * age + b
target = non_smoker_df.charges

ages = non_smoker_df.age

print(non_smoker_df)
