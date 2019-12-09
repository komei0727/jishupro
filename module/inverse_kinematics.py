import csv
import numpy as np

with open('data/あ_2.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    l_float = [[float(v)/10 for v in row] for row in l]
l_float = np.array(l_float)

b = np.array([[8, 0], [-8, 0]])
l = np.array([40, 40])
m = np.array([50, 50])
X = []
for i in range(len(l_float)):
    x = l_float[i] + [-50, 55]
    p = 2 * l * (x[0] - b[:,0])
    q = 2 * l * (x[1] - b[:,1])
    r = (x[0] - b[:,0])**2 + (x[1] - b[:,1])**2 + l**2 - m**2
    cos = [(p*r + q*np.sqrt(p**2 + q**2 -r**2))/(p**2 + q**2), (p*r - q*np.sqrt(p**2 + q**2 -r**2))/(p**2 + q**2)]
    sin = [(q*r - p*np.sqrt(p**2 + q**2 -r**2))/(p**2 + q**2), (q*r + p*np.sqrt(p**2 + q**2 -r**2))/(p**2 + q**2)]
    thete1 = [np.arccos(cos[0][0]) * 360 / (2*np.pi), np.arccos(cos[1][0]) * 360 / (2*np.pi)]
    thete2 = [np.arccos(cos[0][1]) * 360 / (2*np.pi), np.arccos(cos[1][1]) * 360 / (2*np.pi)]
    X.append([thete1[0],thete2[1]])

with open('angle_data/あ_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(X)
