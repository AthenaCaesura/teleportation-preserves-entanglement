# Teleportation Preserves Entanglement

Here I discuss the outputs of `teleportation_circuit.py` where I demonstrate that entanglement is preserved in the teleportation process. This project was completed as part of proof of the correctness of the ruby slippers compiler.

## Circuit Sequence
Here I describe what is happening in the circuit in term of the barriers that are placed. See `circuit_description.png` for reference.

### Before Barrier 1
Here we have a simple circuit for setting up a 3 qubit GHZ state in Alice's posession in qubits 0, 1, and 2. We will teleport qubit 2 to qubit 4 and see that it retains it's entanglement with qubits 0 and 1.

### After Barrier 1
Prepare bell state which will be used to teleport qubit 2 to qubit 4.

### After Barrier 2
Clifford part of teleportation circuit. This is was Ruby Slippers implements.

### After Barrier 3
Measurements and conditional gates to complete teleportation circuit.
These are absent in Ruby Slippers as ruby slippers ignores pauli gates in the graph state.

### After Barrier 4
Measureing qubits 0, 1, and 4 to see if they are still entangled.

## Interpreting the Output

Here I have grouped the 3 entangled qubits into the last classical register. So they are also grouped in the final output.

This makes it easy to see that they are entangled because they are all 0 or all 1. This can be seen in this example output:

```
{'000 1 1': 113, '111 1 1': 127, '000 0 1': 136, '111 0 0': 123, '111 1 0': 137, '000 0 0': 133, '111 0 1': 121, '000 1 0': 134}
```

The first three qubits always equal each other and are grouped. Notice that the other qubits are uncorrelated with each other. Indicating the teleportation was successful.

## Usage

Simply  run the following commands from the man directory of this repository:

```
pip install -r requirements.txt
python teleportation_circuit.py
```

## Ackowledgement

I would like to Acknowledge qiskit for providing the code for quantum teleportation online.