# -*- coding: utf-8 -*-
"""Prac8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z99iGcXizWyxU0OVsCBueP-aLCH9NHfG

### **Titanic Vizualization**
"""

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')

df.head()

df.info()

"""## **Line Plot**"""

sns.lineplot(x=df['age'].value_counts(), y='age', data=df)

"""## **Bar Plot**"""

sns.countplot(x ='class', data = df)

sns.countplot(x ='sex', data = df)

sns.countplot(x ='alone', data = df)

"""## **Histogram**"""

sns.histplot( x='age', data=df)

sns.histplot( x='fare', data=df)

sns.histplot( x='fare', data=df , bins=50, kde=True)

"""## **Pie Chart**"""

df['sex'].value_counts().plot(kind="pie", autopct="%.2f")

df['alive'].value_counts().plot(kind="pie", autopct="%.2f")

df['class'].value_counts().plot(kind="pie", autopct="%.2f")

df['alone'].value_counts().plot(kind="pie", autopct="%.2f")

"""## **Scatter Plot**"""

sns.scatterplot(x='fare', y='age', data=df)

sns.scatterplot(x='fare', y='age', hue='sex',data=df)

"""## **Box Plot**"""

sns.boxplot( y='fare', data=df)

sns.boxplot( y='age', data=df)