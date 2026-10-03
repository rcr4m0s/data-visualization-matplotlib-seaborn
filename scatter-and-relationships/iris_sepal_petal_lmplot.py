import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

sns.set_theme(style='darkgrid')

sns.lmplot(
    data=iris,
    x='sepal_length',
    y='petal_length',
    hue='species',
    markers=['o', 'x', 's']
)

plt.title("Sepal vs Petal by Species")

plt.show()