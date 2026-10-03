import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
sales = [45000, 28000, 35000, 12000, 18000]

plt.bar(categories, sales, color='skyblue', edgecolor='black')

plt.title('Sales by category')
plt.xlabel('Category')
plt.ylabel('Total Sales (PHP)')

plt.show()