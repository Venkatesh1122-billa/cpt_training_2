import seaborn as sns 
import pandas as pd  
import matplotlib.pyplot as plt  

sns.set_style('whitegrid')
data = {'hours': [2,4,6,8,10,3,5,7,9,1],
        'score': [50,60,70,65,75,80,90,55,85,45],
        'pass': [0,0,1,1,1,0,1,1,1,0]}
df = pd.DataFrame(data)
plt.figure(figsize = (8,4))
sns.scatterplot(x = 'hours', y = 'score', hue = 'pass', style = 'pass', data = df, palette = 'coolwarm')
plt.suptitle("pairplot for pass/fail", y = 1.02)
plt.show()

sns.pairplot(df, hue = 'pass', palette = 'hot', diag_kind = 'hist')
plt.suptitle("Pairplot for pass/fail")
plt.show()

plt.figure(figsize= (6,4))
sns.boxplot(x = 'pass', y = 'score', data = df, palette = 'viridis')
plt.title("Box Plot")
plt.xlabel('Pass (1) / Fail (0)')
plt.show()