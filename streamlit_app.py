import pandas as pd
import seaborn as sns


df_iris = pd.read_csv('Iris.csv')
df_iris

# Heatmap
sns.heatmap(data = df_iris.corr(), annot = True, cmap = 'copper', linewidths = 2)
plt.show()



