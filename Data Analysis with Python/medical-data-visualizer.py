import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('medical_examination.csv')

def grab_columns(data):
    cols = []
    for col in data.columns:
        cols.append(col)

    print(cols)
    return cols


def bmi_calc(data):
    # Task 1 Calculate BMI and assign binary
    # BMI = Weight / (Height^2)
    # BMI = kg / m^2

    data['bmi'] = (data['weight'])/((data["height"]/100)**2)
    data['overweight'] = 0

    data["overweight"] = np.where(data["bmi"]>25,1,0)
    list = []
    for i in data["overweight"]:
        list.append(i)
    return list

def normalize_data(data):
    # Normalize all values >0 to be 1
    data["cholesterol"] = np.where(data["cholesterol"] > 1, 1, 0)

    data["gluc"] = np.where(data["gluc"] > 1, 1, 0)

    data["smoke"] = np.where(data["smoke"] > 0, 1, 0)

    data["alco"] = np.where(data["alco"] > 0, 1, 0)

    data["active"] = np.where(data["active"] > 0, 1, 0)

# Add column for overweight classification
df["overweight"] = bmi_calc(df)

# Normalize Values to binary
normalize_data(df)
print(df)


# Plotting Steps
df_2 = df[["cardio","cholesterol","gluc","smoke","alco","active","overweight"]]
print(df_2)

df_3 = pd.melt(df_2, id_vars=["cardio"], value_vars=["cholesterol","gluc","smoke","alco","active","overweight"])
# print(df_3)

df_4 = df_3.value_counts(dropna=False,sort=False)
df_4.name = "counts"
# print(df_4)

df_5 = df_3.value_counts(dropna=False,sort=False).rename_axis(['cardio','variable','value']).reset_index(name='counts')
print(df_5)

df_5_0 = df_5[(df_5["cardio"]==0)]
df_5_1 = df_5[(df_5["cardio"]==1)]


plot_a = sns.catplot(x="variable", y="counts", hue="value", data=df_5_0, kind="bar")
plot_b = sns.catplot(x="variable", y="counts", hue="value", data=df_5_1, kind="bar")
plt.show()
