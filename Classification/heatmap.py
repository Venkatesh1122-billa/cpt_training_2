import seaborn as sns 
import pandas as pd  
import matplotlib.pyplot as plt  

sns.set_style('whitegrid')
data = {'hours': [2,4,6,8,10,3,5,7,9,1],
        'score': [50,60,70,65,75,80,90,55,85,45],
        'pass': [0,0,1,1,1,0,1,1,1,0]}
df = pd.DataFrame(data)


correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot = True, cmap = 'cool', vmin = -1, vmax = 1)
plt.show()