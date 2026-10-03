import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

numeric_df = iris.drop(columns=['species'])
correlation_matrix = numeric_df.corr()

sns.set_theme(style="white")
sns.heatmap(
    correlation_matrix, 
    annot=True,      
    cmap='coolwarm',  
    fmt='.2f'         
)

plt.title('Correlation Heatmap of Iris Dataset Features')

plt.show()