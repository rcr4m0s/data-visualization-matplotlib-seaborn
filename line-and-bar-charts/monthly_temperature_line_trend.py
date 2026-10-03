import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp_celsius = [24, 25, 27, 29, 31, 30, 29, 28, 28, 27, 26, 25]

plt.plot(months, temp_celsius, color='orange', marker='o')

plt.title('Temperature trends from January to December')
plt.xlabel('Months')
plt.ylabel('Temperature (C)')
plt.grid(True)

plt.show()