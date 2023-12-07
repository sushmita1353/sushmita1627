import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate x values
x = np.linspace(-10, 10, 400)

# Get the current working directory
current_directory = os.getcwd()

# Provide the full path to the CSV file
file_path = os.path.join(current_directory, "se.csv")

# Check if the file exists
if os.path.exists(file_path):
    # Read coefficients (a, b, c) from the CSV file
    coefficients_df = pd.read_csv(file_path)

    # Plot each set of coefficients 
    for index, row in coefficients_df.iterrows():
        a = row['a'] 
        b = row['b']  
        c = row['c'] 

        # Calculate y values for the quadratic function
        y = a * x**2 + b * x + c

        # Plot the function 
        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

    # Add title, labels, legend, and grid 
    plt.title('Plot of Quadratic Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Display the plot 
    plt.show()
    
    f=pd.read_csv("se.csv")
    for i in f.iterrows():
      print(i)
