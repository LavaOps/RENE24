# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[2]], cargs=[])
qc.append(CU3Gate(4.963536913425521, 1.5227424436621908, 1.4955230437850562), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U1Gate(3.1517661355750732), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[3]], cargs=[])
qc.append(RYGate(0.028506061128108957), qargs=[qr[0]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[0], qr[2], qr[3]], cargs=[])
qc.append(RZZGate(4.1384051590167115), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RZZGate(5.287141902734077), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(U1Gate(0.1294232471722401), qargs=[qr[3]], cargs=[])
qc.append(RYGate(1.2614322385819892), qargs=[qr[2]], cargs=[])
qc.append(CU3Gate(0.25346731569515724, 0.03496821068258682, 2.3020829194208456), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RZGate(6.198623519374403), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(U1Gate(0.8804227877135313), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(0.0551823887917359), qargs=[qr[0], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CUGate(5.534445945097914, 1.302850355636436, 0.9929905885956432, 5.767029794145674), qargs=[qr[3], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(C3XGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QPY_CONVERSION

from qiskit import qpy
with open('tmp.qpy', 'wb') as fd:
	qpy.dump(qc, fd)
with open('tmp.qpy', 'rb') as fd:
	qc = qpy.load(fd)[0]# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_83a681ec7f4e44a08c8cc891e3a9889d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_83a681ec7f4e44a08c8cc891e3a9889d, shots=692).result().get_counts(qc)
RESULT = counts
