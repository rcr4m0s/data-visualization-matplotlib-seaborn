import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

sns.set_theme(style='ticks')

sns.pairplot(
    data=iris,
    hue='species',
    palette='Set2'
)

plt.show()