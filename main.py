from quantum_data import QuantumData

DIR = 'MalariaDrugImagesGHS'

data = QuantumData(DIR, 'qasm_simulator', False)
d = data.transform(True)

print(len(d))
print(d[0])