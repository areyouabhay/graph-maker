import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.abs(x**2 - 1)

# Create an array of x values from -2 to 2
x = np.linspace(-2, 2, 400)
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = |x^2 - 1|$', color='blue')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')

# Mark key points
plt.scatter([-1, 0, 1], [0, 1, 0], color='red') # Points (-1,0), (0,1), (1,0)
plt.text(-1, 0.5, '(-1, 0)', fontsize=10, ha='center')
plt.text(0, 1.5, '(0, 1)', fontsize=10, ha='center')
plt.text(1, 0.5, '(1, 0)', fontsize=10, ha='center')

# Set limits and labels
plt.xlim(-2, 2)
plt.ylim(-0.5, 3)
plt.title(r'Graph of $f(x) = |x^2 - 1|$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

# Show the plot
plt.show()