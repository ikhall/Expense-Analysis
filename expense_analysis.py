# import csv
import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np

rawData = pd.read_csv('General Ledger Report (59).csv')

to_drop = ['Txn No', 'Curr', 'Balance (USD)']
rawData.drop(to_drop, inplace=True, axis=1)
df = pd.DataFrame(rawData)
pd.to_numeric(df['Txn Amt'])
pd.to_numeric(df['Debit (USD)'])
pd.to_numeric(df['Credit (USD)'])
df['Debit (USD)'].fillna(0, inplace=True)
df['Credit (USD)'].fillna(0, inplace=True)
# pd.to_datetime(df['Posted Dt.'])

df2 = df[df['JNL'].notna()]


print(df.info())
print(df2.head(100))















# print(df.loc[1])
# print(type(df['Posted Dt.'][5]))
# for i in df['Posted Dt.']:
#     print(i)
# sumOne = df.loc[(df['Account'] == 61000) & (df['Txn Amt'] > 0),'Debit (USD)'].sum()
# print('Sum of 61000: ', sumOne)