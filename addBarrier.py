# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(U1Gate(3.1517661355750732), qargs=[qr[2]], cargs=[])
qc.append(RYGate(0.028506061128108957), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(5.287141902734077), qargs=[qr[5], qr[7]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RZZGate(2.3020829194208456), qargs=[qr[2], qr[6]], cargs=[])
qc.append(CSXGate(), qargs=[qr[9], qr[5]], cargs=[])
qc.append(DCXGate(), qargs=[qr[8], qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[9], qr[6], qr[5]], cargs=[])
qc.append(RZZGate(3.4635223140180296), qargs=[qr[8], qr[5]], cargs=[])
qc.append(U1Gate(2.9267362927620018), qargs=[qr[2]], cargs=[])
qc.append(DCXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.barrier()
qc.append(YGate(), qargs=[qr[3]], cargs=[])
qc.append(CYGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[6], qr[5], qr[0], qr[1]], cargs=[])
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
backend_37c916a420344534948fd6cf5b6571c2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_37c916a420344534948fd6cf5b6571c2, shots=5542).result().get_counts(qc)
RESULT = counts
