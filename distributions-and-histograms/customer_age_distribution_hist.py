import matplotlib.pyplot as plt

ages = [18, 19, 21, 22, 23, 23, 24, 25, 29, 30, 31, 35, 40, 42, 50]

plt.hist(ages, bins=5, color='purple', edgecolor='black')

plt.title('Customer Age Distribution')
plt.xlabel('Age Groups')
plt.ylabel('Number of Customers')

plt.show()

