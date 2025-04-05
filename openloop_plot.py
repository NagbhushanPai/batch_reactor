import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_excel("C:\\Users\\Nagbhushan_Pai\\Desktop\\DeskTOP\\Arasu work\\batch_reactor\\Opeloop_HFc_TrTj.xlsx")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(data['Sampling time'], data['Reactor Temperature'], color='red', label='Reactor Temperature')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Reactor Temperature vs Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
