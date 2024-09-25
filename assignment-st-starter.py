# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# show the title

st.title("Titanic App by Yuxi Guo")

# read csv and show the dataframe

df = pd.read_csv('train.csv')

st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

# 创建图形和三个子图
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 绘制每个客舱等级的票价箱线图
for i, pclass in enumerate(sorted(df['Pclass'].unique())):
    df[df['Pclass'] == pclass].boxplot(column='Fare', ax=axes[i])
    axes[i].set_xlabel(f'PClass = {pclass}')
    axes[i].set_ylabel('Fare' if i == 0 else '')

plt.tight_layout()

# 在 Streamlit 应用中显示图表
st.pyplot(fig)

