import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "C:\\Users\\Nagbhushan_Pai\\Desktop\\DeskTOP\\Arasu work\\batch_reactor\\Test_Signal_Data.csv"
data = pd.read_csv(file_path)

# If there's a 'Time' or 'Sampling time' column, use it as x-axis
time_column = None
for col in data.columns:
    if 'time' in col.lower():
        time_column = col
        break

# Plot each signal
plt.figure(figsize=(12, 6))
for col in data.columns:
    if col != time_column:
        plt.plot(data[time_column] if time_column else data.index, data[col], label=col)

plt.xlabel(time_column if time_column else 'Index')
plt.ylabel('Signal Value')
plt.title('Test Signal Data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
