# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(U1Gate(3.1517661355750732), qargs=[qr[2]], cargs=[])
qc.append(RYGate(0.028506061128108957), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(5.287141902734077), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RZZGate(2.3020829194208456), qargs=[qr[2], qr[5]], cargs=[])
qc.append(U1Gate(0.8804227877135313), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[10]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[10]], cargs=[])
qc.append(C3XGate(), qargs=[qr[5], qr[6], qr[8], qr[9]], cargs=[])
qc.append(U1Gate(2.9267362927620018), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_e388bf = QuantumRegister(1, name='qr_e388bf')
qc.add_register(qr_e388bf)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit.providers.fake_provider import FakeWashingtonV2
from qiskit_aer import AerSimulator
backend = FakeWashingtonV2()
simulator = AerSimulator()
from qiskit import transpile
qc = transpile(qc, backend=backend, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

counts = simulator.run(qc, shots=7838).result().get_counts(qc)
RESULT = counts
