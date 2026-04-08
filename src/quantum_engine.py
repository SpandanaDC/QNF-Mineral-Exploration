import qiskit
from qiskit import QuantumCircuit
import numpy as np

# This function is the "Quantum Filter" for your mineral data
def transform_features_quantum(gravity, mag, seismic):
    # 1. We use 3 Qubits (one for each of your 3 signals)
    qc = QuantumCircuit(3)
    
    # 2. Encoding: We turn the numbers (0.1, 0.5, etc.) into angles
    # This is how the quantum computer "reads" your CSV data
    qc.rx(gravity * np.pi, 0)
    qc.ry(mag * np.pi, 1)
    qc.rz(seismic * np.pi, 2)
    
    # 3. Entanglement: Linking the qubits so they talk to each other
    # This finds hidden patterns between Gravity and Magnetism
    qc.cx(0, 1)
    qc.cx(1, 2)
    
    return qc

# --- Testing Part ---
# Let's pretend we have one row of data: Gravity=0.5, Mag=0.8, Seis=0.2
test_circuit = transform_features_quantum(0.5, 0.8, 0.2)

# This line draws the circuit in your terminal so you can see it!
print("Tanu, here is your Quantum Circuit:")
print(test_circuit.draw())
