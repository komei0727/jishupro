#! /usr/bin/python
# -*- coding: utf-8 -*-
import math
import numpy as np

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


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    #input
    x=[0,1,2,3]
    y=[2.7,6,5,6.5]

    # 3d spline interporation
    spline=Spline(x,y)
    X, Y = spline.calc()

    plt.plot(X,Y,"xb")
    plt.plot(X,Y,"-r")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
