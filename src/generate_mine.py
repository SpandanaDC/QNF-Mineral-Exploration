import pandas as pd
import numpy as np
import os

# 1. Create a 100x100 grid of land (Total 10,000 points)
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
X, Y = np.meshgrid(x, y)

# FIX: We flatten X and Y separately to avoid the NameError
X_flat = X.flatten()
Y_flat = Y.flatten()

# 2. Hide a "Mineral Deposit" at X=50, Y=50, Depth=30 [cite: 178]
dist = np.sqrt((X_flat - 50)**2 + (Y_flat - 50)**2 + 30**2)

# 3. Create the "Signals" (Gravity, Magnetic, Seismic) [cite: 178]
gravity = 100 / dist + np.random.normal(0, 0.1, 10000) 
magnetic = 500 / (dist**1.5) + np.random.normal(0, 5, 10000)
seismic = 5.0 + (10 / dist) + np.random.normal(0, 0.05, 10000)

# 4. Create the Labels (The "Answer Key")
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

# 6. Make sure the 'data' folder exists before saving
if not os.path.exists('data'):
    os.makedirs('data')

# 7. Save the data
df.to_csv('data/simulated_mine_data.csv', index=False)
print("SUCCESS: Digital Mine Generated in /data folder!")
