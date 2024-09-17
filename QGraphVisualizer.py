import numpy as np
import matplotlib.pyplot as plt

print("Welcome to the quadratic graph visualizer. This will visualize the graph of the form: ax**2 + bx + c")

# Step 1: Get the coefficients and range from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Step 2: Generate x values
range1 = int(input("Enter the starting value for x: "))
range2 = int(input("Enter the ending value for x: "))
points = int(input("Enter the number of points to plot: "))
x_values = np.linspace(range1, range2, points)

# Step 3: Define the quadratic function
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Compute y values using the quadratic function
y_values = quadratic_function(x_values, a, b, c)

# Step 4: Plot the graph
plt.plot(x_values, y_values, label=f'$y = {a}x^2 + {b}x + {c}$', color='b')

# Optional: Customize the plot
plt.title("Quadratic Function Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True)
plt.legend()

# Step 5: Show the plot
plt.show()
