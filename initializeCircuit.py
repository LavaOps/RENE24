# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
from qiskit.circuit.random.utils import random_circuit
qc = random_circuit(num_qubits=2, depth=18)
qc.initialize(0, qc.qubits)
qr = qc.qubits[:2]
qc.add_register(cr)
qc.append(RYGate(1.4989100685639651), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(0.047135640611006696,4.573317371103322,2.9393889649742833), qargs=[qr[0]], cargs=[])
subcircuit.append(RYYGate(5.287141902734077), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CPhaseGate(6.133652579044361), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(UGate(0.18815069577548796,2.4225957286719844,1.2614322385819892), qargs=[qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CUGate(4.427689832982673, 3.9781792031418557, 3.1517661355750732, 3.613202415480831), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU3Gate(0.028506061128108957, 3.271874281879507, 1.4378744405597133), qargs=[qr[0], qr[1]], cargs=[])
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
backend_51d8d31725b64b72b7352b339b60518c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_51d8d31725b64b72b7352b339b60518c, shots=346).result().get_counts(qc)
RESULT = counts
