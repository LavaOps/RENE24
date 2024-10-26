# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(RZGate(4.427689832982673), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(4.879596824359527), qargs=[qr[3], qr[2]], cargs=[])
qc.append(RYGate(0.028506061128108957), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(3.7184510259047707), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RZZGate(5.287141902734077), qargs=[qr[0], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc = qc.copy()
# SECTION
# NAME: USELESS_ENTITIES

qr_9278ff = QuantumRegister(1, name='qr_9278ff')
qc.add_register(qr_9278ff)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1bb7c693470b444fadad8ca63ca799c2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1bb7c693470b444fadad8ca63ca799c2, shots=979).result().get_counts(qc)
RESULT = counts
