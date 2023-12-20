import matplotlib.pyplot as plt
'/mntt seaborn as sns
import numpy as np

# Sample data for the charts
x = np.linspace(0, 10, 30)
y = np.sin(x)

# Data for bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Data for pie chart
slices = [30, 20, 40, 10]
labels = ['Section 1', 'Section 2', 'Section 3', 'Section 4']

# Set the overall figure size
plt.figure(figsize=(12, 18))

# Add title space
plt.subplot(6, 1, 1)  # 6 rows, 1 column, position 1
plt.text(0.5, 0.5, 'Title of the Combined Image', horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')
plt.axis('off')

# Line chart using Seaborn
plt.subplot(6, 2, 3)  # 6 rows, 2 columns, position 3
sns.lineplot(x=x, y=y)
plt.title('Line Chart')

# Bar chart using Seaborn
plt.subplot(6, 2, 4)  # 6 rows, 2 columns, position 4
sns.barplot(x=categories, y=values)
plt.title('Bar Chart')

# Scatter plot using Seaborn
plt.subplot(6, 2, 5)  # 6 rows, 2 columns, position 5
sns.scatterplot(x=x, y=y)
plt.title('Scatter Plot')

# Pie chart (using Matplotlib as Seaborn doesn't support pie charts)
plt.subplot(6, 2, 6)  # 6 rows, 2 columns, position 6
plt.pie(slices, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Add text space
plt.subplot(6, 1, 6)  # 6 rows, 1 column, position 6
plt.text(0.5, 0.5, 'This is some explanatory text that goes below the charts.', horizontalalignment='center', verticalalignment='center', fontsize=12)
plt.axis('off')

# Adjust the layout
plt.tight_layout()

# Save the plot as an image
plt.savefig('/mnt/data/combined_charts.png')

# Show the plot
plt.show()

# Provide the path for download
'/mnt/data/combined_charts.png'