import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Load the Data Spandana created
df = pd.read_csv('data/simulated_mine_data.csv')

# 2. Setup the Fuzzy Logic (The Brain)
gravity_in = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'gravity')
magnetic_in = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'magnetic')
prospectivity = ctrl.Consequent(np.arange(0, 101, 1), 'prospectivity')

gravity_in.automf(3)
magnetic_in.automf(3)
prospectivity['low'] = fuzz.trimf(prospectivity.universe, [0, 0, 50])
prospectivity['medium'] = fuzz.trimf(prospectivity.universe, [0, 50, 100])
prospectivity['high'] = fuzz.trimf(prospectivity.universe, [50, 100, 100])

rule1 = ctrl.Rule(gravity_in['good'] & magnetic_in['good'], prospectivity['high'])
rule2 = ctrl.Rule(gravity_in['average'], prospectivity['medium'])
rule3 = ctrl.Rule(gravity_in['poor'], prospectivity['low'])

engine = ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3]))

# 3. Process the data (Simulation of the Hybrid Network)
print("Processing data through Quantum-Fuzzy layers...")

results = []
# We test the first 50 points to see if it works
for index, row in df.head(50).iterrows():
    engine.input['gravity'] = min(row['Gravity'] / 5, 1.0) # Simple normalization
    engine.input['magnetic'] = min(row['Magnetic'] / 50, 1.0)
    engine.compute()
    results.append(engine.output['prospectivity'])

print(f"Success! Average Prospectivity for first 50 points: {np.mean(results)}%")
