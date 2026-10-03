import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.set_theme(style="whitegrid")

sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex'
)

plt.title('Total Bill Distribution by Day and Gender')

plt.show()