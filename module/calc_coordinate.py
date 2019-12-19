import csv
import numpy as np
import math

class Spline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a, self.b, self.c, self.d, self.h = [], [], [], [], []
        self.a = [iy for iy in y]

        self.h = [(x[i+1]-x[i]) for i in range(len(x)-1)]

        A = np.array([[self.h[1], 2*(self.h[0]+self.h[1])], [2*(self.h[1]+self.h[2]), self.h[1]]])
        b = np.array([[3*(self.a[2]-self.a[1])/self.h[1] - 3*(self.a[1]-self.a[0])/self.h[0], 3*(self.a[3]-self.a[2])/self.h[2] - 3*(self.a[2]-self.a[1])/self.h[1]]])
        c = np.dot(np.linalg.inv(A), b.T)

        self.c = [0, c[1][0], c[0][0], 0]

        self.b = [((self.a[i+1]-self.a[i])/self.h[i] - self.h[i]*(self.c[i+1]+self.c[i]*2)/3) for i in range(len(x)-1)]
        self.d = [((self.c[i+1]-self.c[i])/self.h[i]/3) for i in range(len(x)-1)]

    def calc(self):
        p = []
        q = []
        for i in range(3):
            r = np.sqrt((self.x[i+1]-self.x[i])**2 + (self.y[i+1]-self.y[i])**2)
            dx = np.linspace(self.x[i], self.x[i+1], int(r*10))
            dy = self.a[i] + self.b[i]*(dx-self.x[i]) + self.c[i]*(dx-self.x[i])**2 + self.d[i]*(dx-self.x[i])**3
            if i == 0:
                for j in range(len(dx)):
                    p.append(dx[j])
                    q.append(dy[j])
            else:
                for j in range(len(dx[1:])):
                    p.append(dx[j+1])
                    q.append(dy[j+1])
        return p, q

def calc_coordinate(input_file, output_file):
    with open(input_file) as f:
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
            Y.append(y_c[j+1])


    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(np.array([X,Y]).T)
