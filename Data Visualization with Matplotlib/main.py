import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.arange(1, 6)
y1 = np.random.randint(1, 10, size=5)
y2 = np.random.randint(1, 10, size=5)
values = [15, 30, 10, 25]
categories = ["Category 1", "Category 2", "Category 3", "Category 4"]

# Create a bar plot
plt.subplot(2, 3, 1)
plt.bar(x, y1, label="Bar 1", color="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bar Plot")
plt.legend()

# Create a histogram
plt.subplot(2, 3, 2)
plt.hist(y1, bins=5, color="red", alpha=0.5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")

# Create a pie plot
plt.subplot(2, 3, 3)
plt.pie(values, labels=categories, autopct="%1.1f%%", colors=["red", "blue", "green", "yellow"])
plt.title("Pie Plot")

# Create an area plot
plt.subplot(2, 3, 4)
plt.fill_between(x, y1, color="orange", alpha=0.5)
plt.fill_between(x, y1, y2, color="purple", alpha=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Area Plot")

# Create a scatter plot
plt.subplot(2, 3, 5)
plt.scatter(x, y1, label="Group 1", color="green", marker="o")
plt.scatter(x, y2, label="Group 2", color="blue", marker="s")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
