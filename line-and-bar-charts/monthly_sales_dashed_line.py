import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [12000, 15000, 14000, 19000, 22000]

plt.plot(months, sales, color='blue', marker='o', linestyle='--')

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (PHP)')
plt.grid(True)

plt.show()