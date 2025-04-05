import pandas as pd
import matplotlib.pyplot as plt

# Read only the Setpoint column, skipping the first non-numeric row
file_path = "C:\\Users\\Nagbhushan_Pai\\Desktop\\DeskTOP\\Arasu work\\batch_reactor\\Trajectory2.csv"
data = pd.read_csv(file_path, skiprows=1, header=None, names=['Setpoint'])

# Plot Setpoint
plt.figure(figsize=(10, 5))
plt.plot(data['Setpoint'], label='Setpoint', linestyle='--', color='blue')
plt.xlabel('Time Steps')
plt.ylabel('Temperature (°C)')
plt.title('Setpoint vs Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
