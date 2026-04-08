import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. New inputs: Quantum-enhanced Gravity and Magnetic signals
gravity = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'gravity')
magnetic = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'magnetic')
prospectivity = ctrl.Consequent(np.arange(0, 101, 1), 'prospectivity')

# 2. Define ranges: "Poor", "Average", "Good"
gravity.automf(3)
magnetic.automf(3)

# 3. Define Prospectivity (Chance of finding mineral): Low, Medium, High
prospectivity['low'] = fuzz.trimf(prospectivity.universe, [0, 0, 50])
prospectivity['medium'] = fuzz.trimf(prospectivity.universe, [0, 50, 100])
prospectivity['high'] = fuzz.trimf(prospectivity.universe, [50, 100, 100])

# 4. THE BRAIN: Define the Geological Rules
rule1 = ctrl.Rule(gravity['good'] & magnetic['good'], prospectivity['high'])
rule2 = ctrl.Rule(gravity['average'] | magnetic['average'], prospectivity['medium'])
rule3 = ctrl.Rule(gravity['poor'] & magnetic['poor'], prospectivity['low'])

# 5. Build the Controller
mining_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
mining_sim = ctrl.ControlSystemSimulation(mining_ctrl)

print("Step 2 Complete: Fuzzy Logic Rules are live!")
