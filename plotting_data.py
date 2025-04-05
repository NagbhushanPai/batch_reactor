import matplotlib.pyplot as plt
import pandas as pd
import ast

data = pd.read_csv('data.csv')

def parse_action(x):
    if isinstance(x, str) and x.startswith("[") and x.endswith("]"):
        return ast.literal_eval(x)[0]
    return float(x)

data['Action'] = data['Action'].apply(parse_action)

# Plot or process data as needed
  

# Plot
plt.figure(figsize=(10, 6))
plt.plot(data['Reactor Temperature'], label='Reactor Temperature', linewidth=2)
plt.plot(data['Setpoint'], label='Setpoint', linestyle='--', linewidth=2)
plt.plot(data['Action'], label='Action', linestyle=':', linewidth=2)

plt.xlabel('Time Steps')
plt.ylabel('Temperature / Action')
plt.title('Reactor Temperature Tracking')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("plot_output.png")  # Save the plot
plt.show()
