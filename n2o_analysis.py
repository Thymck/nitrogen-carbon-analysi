import pandas as pd
import matplotlib.pyplot as plt

# Load Data


df = pd.read_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/2025/nitrogen-carbon-analysi/turkey_n2o_agriculture.csv", 
                 quotechar='"', 
                 skiprows=1,  # skip the first row that is not the header
                 on_bad_lines='skip')  # skip lines with wrong number of fields



print(df.head())

total_non_null = df.count().sum()
print(total_non_null)

print(df.shape)  # (rows, columns)

print(df.isnull().sum().sum())

missing_counts = df.isnull().sum()
missing_percent = (missing_counts / len(df)) * 100
print(pd.DataFrame({'Missing Count': missing_counts, 'Missing %': missing_percent}))


#to drop
df = df.drop(columns=["Unnamed: 2"])
