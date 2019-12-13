
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *

import settings

import os

from base_exceptions import BackendNotFoundExeception


class QBitsLoader():
    def __init__(self, online=False):
        self.online = online

        if self.online:
            TOKEN = os.getenv('TOKEN')
            # Loading your IBM Q account(s)
            IBMQ.save_account(TOKEN, overwrite=True)
            self.provider = IBMQ.load_account()
            self.list_backends = self.provider.backends()
        else:
            self.list_backends = Aer.backends()

    def get_backends(self):
        """Returns a list of available backends
        """
        return [backend.name() for backend in self.list_backends]

    def get_backends_with_qubits(self):
        """Returns a list of tuples with the available backends and their number of qubits
        """
        return [(backend.name(), backend.configuration().n_qubits,) for backend in self.list_backends]

    def call_backend(self, name):
        """Returns a backend to work with

        Arguments:
        name: (str) The name of the backend to work with

        Returns:
        The backend specified

        Raises:
        BackendNotFoundExeception: if the backend given does not exist
        """
        if name not in self.get_backends():
            raise BackendNotFoundExeception(f"Backend '{name}' not defined")
        else:
            if self.online:
                return self.provider.get_backend(name)
            return Aer.get_backend(name)

if __name__ == "__main__":
    q_bits_loader = QBitsLoader(True)
    
    print(q_bits_loader.get_backends())
    print(q_bits_loader.get_backends_with_qubits())
    print(q_bits_loader.call_backend('unitary_simulator'))