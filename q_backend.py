
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)

import settings

import os


class QBitsLoader():
    def __init__(self, online=False):
        self.online = online

        if self.online:
            TOKEN = os.getenv('TOKEN')
            IBMQ.save_account(TOKEN, overwrite=True)
            provider = IBMQ.load_account()
            self.list_backends = provider.backends()
        else:
            self.list_backends = Aer.backends()

    def get_backends(self):
        """Returns a list of tuples with the available backends and their number of qubits
        """
        return [backend.name() for backend in self.list_backends]

    def get_backends_with_qubits(self):
        """Returns a list of tuples with the available backends and their number of qubits
        """
        return [(backend.name(), backend.configuration().n_qubits,) for backend in self.list_backends]

    def call_backend(self, name):
        if name not in self.get_backends():
            raise ValueError(f"Backend '{name}' not defined")
        else:
            return name

if __name__ == "__main__":
    q_bits_loader = QBitsLoader(False)
    
    print(q_bits_loader.get_backends())
    print(q_bits_loader.get_backends_with_qubits())
    print(q_bits_loader.call_backend('unitary_simulator'))