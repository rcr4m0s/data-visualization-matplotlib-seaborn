import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.set_theme(style='whitegrid')

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Total Bill Distribution by Day and Sex')


plt.subplot(1, 2, 2)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Total Bill vs Tip by Meal Time')

plt.tight_layout()

plt.show()