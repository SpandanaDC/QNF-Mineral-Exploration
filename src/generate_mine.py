import pandas as pd
import numpy as np

# 1. Create a 100x100 grid (10,000 points)
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
X, Y = np.meshgrid(x, y)
X_flat, Y_flat = X.flatten(), Y_flat.flatten()

# 2. Hide a "Mineral Deposit" at X=50, Y=50, Depth=30
# This creates the "Ground Truth" for Phase 1 
dist = np.sqrt((X_flat - 50)**2 + (Y_flat - 50)**2 + 30**2)

# 3. Create the "Signals" (Physics formulas) [cite: 173, 178]
gravity = 100 / dist + np.random.normal(0, 0.1, 10000) 
magnetic = 500 / (dist**1.5) + np.random.normal(0, 5, 10000)
seismic = 5.0 + (10 / dist) + np.random.normal(0, 0.05, 10000)

# 4. Create the Labels (The Answer Key) [cite: 174, 181]
target = (dist < 15).astype(int)

# 5. Build the table
df = pd.DataFrame({
    'X': X_flat, 
    'Y': Y_flat, 
    'Gravity': gravity, 
    'Magnetic': magnetic, 
    'Seismic': seismic,
    'Label': target
})

# 6. Save the data to our data folder [cite: 155]
df.to_csv('data/simulated_mine_data.csv', index=False)
print("Digital Mine Generated!")
