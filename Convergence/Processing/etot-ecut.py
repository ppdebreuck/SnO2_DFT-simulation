
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../etot-ecut/Conv_etot-e*.out'))
energies = []
ecut = []
found = 0
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "total energy" in line and 'Ry' in line:
			energy = re.findall("\d+\.\d+",line)
			print f
			print energy
			energies.append(float(energy[0]))
			found = 1
			break
	if found==0:
		continue
	for line in open(f).readlines():
		line = line.rstrip()
		if "kinetic-energy cutoff" in line:
			print line
			e = re.findall("\d+\.\d+",line)
			ecut.append(float(e[0]))
			break

energies =  [x*-0.5 for x in energies]	#in Hartree
upper = [energies[-1]+(0.005*6) for x in ecut]
lower = [energies[-1]-(0.005*6) for x in ecut]

print energies
print ecut
plt.plot(ecut,energies,'o-',ecut,lower,'--',ecut,upper,'--')
plt.xlabel('kinetic energy cutoff (Ry)')
plt.ylabel('Total energy (Ha)')
plt.title('Energy - ecut convergence')
plt.savefig('etot-ecut.png')
plt.show()

