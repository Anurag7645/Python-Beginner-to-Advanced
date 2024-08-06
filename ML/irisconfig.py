import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import LassoCV

df = pd.read_csv(r"D:\study\python\Python-Beginner-to-Advanced\ML\Iris.csv")
print(df)

df.info()

numerical_summary = df.describe().transpose()
print(numerical_summary)
palette = sns.color_palette("viridis", as_cmap=True)
numerical_summary.style.background_gradient(cmap=palette)
sns.heatmap(numerical_summary, cmap=palette)
plt.show()