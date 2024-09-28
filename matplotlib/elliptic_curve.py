import numpy as np
import matplotlib.pyplot as plt

# Parameters for the elliptic curve: y^2 = x^3 + ax + b
a = -1
b = 1

# Define the function for the elliptic curve
def elliptic_curve(x, a, b):
    return np.sqrt(x**3 + a*x + b)

# Create an array of x values (range for the plot)
x = np.linspace(-2, 2, 1000)

# Calculate y values from the elliptic curve equation
y_pos = elliptic_curve(x, a, b)   # Positive branch (y^2 = ...)
y_neg = -elliptic_curve(x, a, b)  # Negative branch

# Plotting the elliptic curve
plt.plot(x, y_pos, 'r')  # Plot positive values
plt.plot(x, y_neg, 'r')  # Plot negative values

# Set graph labels and grid
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.title(f"Elliptic Curve: y^2 = x^3 + {a}x + {b}")

# Display the plot
plt.show()
