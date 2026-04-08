import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('data/simulated_mine_data.csv')

# 2. Prepare the Heatmap data
# We are plotting the 'Gravity' as a proxy for the mineral location
grid_size = int(np.sqrt(len(df)))
z = df['Gravity'].values.reshape((grid_size, grid_size))

# 3. Create the Plot
plt.figure(figsize=(8, 6))
plt.imshow(z, extent=[0, 100, 0, 100], origin='lower', cmap='hot')
plt.colorbar(label='Mineral Prospectivity (Signal Strength)')
plt.title('Final Mineral Prospectivity Map (QNF-MEN)')
plt.xlabel('X Coordinate (km)')
plt.ylabel('Y Coordinate (km)')

# 4. Mark the "Hot Spot"
plt.scatter(50, 50, color='cyan', marker='x', s=100, label='Target Zone')
plt.legend()

# 5. Save and Show
plt.savefig('data/final_heatmap.png')
print("Step 4 Complete: Heatmap saved as 'data/final_heatmap.png'!")
plt.show()
