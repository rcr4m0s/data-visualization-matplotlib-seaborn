import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

sns.set_theme(style='ticks')

sns.scatterplot(
    data=iris,
    x='sepal_length',
    y='petal_length',
    hue='species',
    style='species',
    s=70
)

plt.title("Sepal Length vs Petal Length by Species")

plt.show()