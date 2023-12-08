import matplotlib.pyplot as plt
import numpy as np

def quadratic_temperature_model(time,a,b,c):
  #Quadratic equation: T(t)=at^2+bt+c
  temperature=a*(time**2)+b*time+c
  return temperature

#List of coefficients sets(a,b,c)
coefficients_list={
    (0.06,4.5,40),
    (0.04,7,16),
    (0.05,4,26),
}
#Generate time values from 0 to 50 with step1
time_values=np.arange(0,51,1)

#Plotting the results for each set of coefficients
for i, (a,b,c) in enumerate(coefficients_list):
  temperature_values=quadratic_temperature_model(time_values,a,b,c)
  label=f'Set(i+1): a={a}, b={b}, c={c}'
  plt.plot(time_values,temperature_values,label=label)

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Quadratic temp model with multiple sets of coefficets')
plt.legend()
plt.grid(True)
plt.show()
