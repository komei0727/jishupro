import csv
from spline import Spline
import numpy as np
import matplotlib.pyplot as plt

with open('data/あ_original_2.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    l_int = [[int(v) for v in row] for row in l]

l_int = np.array(l_int)
X = []
Y = []

for i in range(int((len(l_int)-1)/3)):
    x = l_int[:,0][i*3:(i+1)*3+1]
    y = l_int[:,1][i*3:(i+1)*3+1]
    if (x[0]<x[1] and x[1]<x[2] and x[2]<x[3]) or (x[0]>x[1] and x[1]>x[2] and x[2]>x[3]):
        spline = Spline(x,y)
        x_c, y_c = spline.calc()
    else:
        spline = Spline(y,x)
        y_c, x_c = spline.calc()
    if i == 0:
        X.append(x_c[0])
        Y.append(100-y_c[0])
    for j in range(len(x_c)-1):
        X.append(x_c[j+1])
        Y.append(100-y_c[j+1])
if len(l_int)%3 == 2:
    x1 = l_int[:,0][-2]
    x2 = l_int[:,0][-1]
    x = [x1, (2*x1+x2)/3, (x1+2*x2)/3, x2]
    y1 = l_int[:,1][-2]
    y2 = l_int[:,1][-1]
    y = [y1, (2*y1+y2)/3, (y1+2*y2)/3, y2]
    if x1==x2:
        spline = Spline(y,x)
        y_c, x_c = spline.calc()
    else:
        spline = Spline(x,y)
        x_c, y_c = spline.calc()
    for j in range(len(x_c)-1):
        X.append(x_c[j+1])
        Y.append(100-y_c[j+1])
if len(l_int)%3 == 0:
    x1 = l_int[:,0][-3]
    x2 = l_int[:,0][-2]
    x3 = l_int[:,0][-1]
    y1 = l_int[:,1][-3]
    y2 = l_int[:,1][-2]
    y3 = l_int[:,1][-1]
    d1 = (x2-x1)**2 + (y2-y1)**2
    d2 = (x3-x2)**2 + (y3-y2)**2
    if d1 > d2:
        x = [x1, (x1+x2)/2, x2, x3]
        y = [y1, (y1+y2)/2, y2, y3]
    else:
        x = [x1, x2, (x2+x3)/2, x3]
        y = [y1, y2, (y2+y3)/2, y3]
    if (x[0]<x[1] and x[1]<x[2] and x[2]<x[3]) or (x[0]>x[1] and x[1]>x[2] and x[2]>x[3]):
        spline = Spline(x,y)
        x_c, y_c = spline.calc()
    else:
        spline = Spline(y,x)
        y_c, x_c = spline.calc()
    for j in range(len(x_c)-1):
        X.append(x_c[j+1])
        Y.append(100-y_c[j+1])


with open('data/あ_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(np.array([X,Y]).T)
