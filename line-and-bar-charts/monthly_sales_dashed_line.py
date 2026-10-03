import matplotlib.pyplot as plt

# 1. Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [12000, 15000, 14000, 19000, 22000]

# 2. Plotting
plt.plot(months, sales, color='blue', marker='o', linestyle='--')

# 3. Customization
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (PHP)')
plt.grid(True)

# 4. Render
plt.show()