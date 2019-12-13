import numpy as np
import math
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram

from qiskit.aqua.components.initial_states import Custom
from qiskit import ClassicalRegister, Aer, execute


vector = np.array([1, 2, 3, 4, 5])
length = vector.shape[0]
if int(math.log2(length)) != length:
    pad_length = 2**(int(math.log2(length))+1)
    vector = np.pad(vector, (0, pad_length - length))
length = vector.shape[0]
print(vector)

def circuit(vec):
    qbits =  int(math.log2(length))
    cct = Custom(qbits, state_vector=vec)
    return cct.construct_circuit('circuit'), qbits


if __name__ == "__main__":

    simulator = Aer.get_backend('qasm_simulator')

    cr, qbits = circuit(vector)
    cr.add_register(ClassicalRegister(qbits))
    cr.measure(list(range(qbits)), list(range(qbits)))

    counts = execute(cr, backend=simulator, shots=1024).result().get_counts(cr)
  
    plot_histogram(counts)
    cr.draw(output = 'mpl')

    plt.show()

    # 
    # print(dir(cr))