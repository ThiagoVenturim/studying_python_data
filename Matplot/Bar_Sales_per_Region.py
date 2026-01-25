from matplotlib import pyplot as plt

regions = ['New England','Mid-Atlantic', 'Midwest']
sales = [882703, 532648, 714406]

plt.bar(regions,sales )
plt.title('Sales per Region')
plt.ylabel("Sales")
plt.xlabel("Label")
plt.show()