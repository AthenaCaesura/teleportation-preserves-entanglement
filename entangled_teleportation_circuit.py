# Do the necessary imports
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.result import marginal_counts
from qiskit.quantum_info import random_statevector


def create_bell_pair(qc, a, b):
    """Creates a bell pair in qc using qubits a & b"""
    qc.h(a)  # Put qubit a into state |+>
    qc.cx(a, b)  # CNOT with a as control and b as target


def alice_gates(qc, psi, a):
    qc.cx(psi, a)
    qc.h(psi)


def measure_and_send(qc, a, b):
    """Measures qubits a & b and 'sends' the results to Bob"""
    qc.barrier()
    qc.measure(a, 0)
    qc.measure(b, 1)


# This function takes a QuantumCircuit (qc), integer (qubit)
# and ClassicalRegisters (crz & crx) to decide which gates to apply
def bob_gates(qc, qubit, crz, crx):
    # Here we use c_if to control our gates with a classical
    # bit instead of a qubit
    qc.x(qubit).c_if(crx, 1)  # Apply gates if the registers
    qc.z(qubit).c_if(crz, 1)  # are in the state '1'


sim = Aer.get_backend("aer_simulator")

## SETUP
qr = QuantumRegister(5, name="q")  # Protocol uses 3 qubits
crz = ClassicalRegister(1, name="crz")  # and 2 classical registers
crx = ClassicalRegister(1, name="crx")
qc = QuantumCircuit(qr, crz, crx)

## STEP 0
qc.h(0)  # Put qubit a into state |+>
qc.cx(0, 1)
qc.cx(0, 2)
qc.barrier()

## STEP 1
# Begin the teleportation protocol with a bell pair
create_bell_pair(qc, 3, 4)
qc.barrier()

## STEP 2
# Send q1 to Alice and q2 to Bob
alice_gates(qc, 2, 3)

## STEP 3
# Alice then sends her classical bits to Bob
measure_and_send(qc, 2, 3)

## STEP 4
# Bob decodes qubits
bob_gates(qc, 4, crz, crx)
qc.barrier()

# Need to add a new ClassicalRegister
# to see the result
cr_result = ClassicalRegister(3)
qc.add_register(cr_result)
qc.measure(0, 2)
qc.measure(1, 3)
qc.measure(4, 4)
qc.draw()


# Display the circuit
qc.draw(filename="my_circuit.png")


t_qc = transpile(qc, sim)
t_qc.save_statevector()
counts = sim.run(t_qc).result().get_counts()
print(counts)
