
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../etot-k/Conv_etot-k*.out'))
energies = []
nkpoints = []
kpoints = []
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "total energy" in line and 'Ry' in line:
			energy = re.findall("\d+\.\d+",line)
			print f
			print energy
			energies.append(float(energy[0]))
			break
	for line in open(f).readlines():
		line = line.rstrip()
		if "number of k points=" in line:
			print line
			k = re.findall("\d+",line)
			nkpoints.append(int(k[0]))
			break
	nk = re.findall("Conv_etot-k\d\d.out",f)
	nkpoints.append(int(nk[0]))

energies =  [x*-0.5 for x in energies]	#in Hartree
upper = [energies[-1]+(0.005*6) for x in nkpoints]
lower = [energies[-1]-(0.005*6) for x in nkpoints]

print energies
print kpoints
print kpoints
plt.plot(nkpoints,energies,'o-',nkpoints,lower,'--',nkpoints,upper,'--')
#plt.ylim([399, 399.3])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Total energy (Ha)')
plt.title('Energy - kpoints convergence')
plt.savefig('etot-k.png')
plt.show()

