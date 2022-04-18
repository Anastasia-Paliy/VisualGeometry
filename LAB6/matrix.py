from math import sqrt, sin, cos
from vector import Vector3

class Matrix3x3():
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'({self.a},\n {self.b},\n {self.c})'

    def I():
        return Matrix3x3(Vector3(1, 0, 0),
                         Vector3(0, 1, 0),
                         Vector3(0, 0, 1))

    def xR(self, r):
        return Matrix3x3(self.a.xR(r),
                         self.b.xR(r),
                         self.c.xR(r))

    def plusM(self, m):
        return Matrix3x3(self.a.plusV(m.a),
                         self.b.plusV(m.b),
                         self.c.plusV(m.c))

    def minusM(self, m):
        return Matrix3x3(self.a.minusV(m.a),
                         self.b.minusV(m.b),
                         self.c.minusV(m.c))

    def xV(self, v):
        return Vector3(self.a.dotV(v),
                       self.b.dotV(v),
                       self.c.dotV(v))
    
    def transpose(self):
        return Matrix3x3(Vector3(self.a.x, self.b.x, self.c.x),
                         Vector3(self.a.y, self.b.y, self.c.y),
                         Vector3(self.a.z, self.b.z, self.c.z))

    def xM(self, m):
        m = m.transpose()
        matrix = Matrix3x3(self.xV(m.a),
                           self.xV(m.b),
                           self.xV(m.c))
        return matrix.transpose()

    def MRot(v, phi):
        S = Matrix3x3(Vector3(0, v.z, -v.y),
                      Vector3(-v.z, 0, v.x),
                      Vector3(v.y, -v.x, 0))

        return Matrix3x3.I().plusM(S.xR(sin(phi))).plusM(S.xM(S).xR(1 - cos(phi)))
    
    
"""
v = Vector3(1, 2, 3)
m = Matrix3x3(Vector3(1, 2, 3),
              Vector3(0, 1, 0),
              Vector3(4, 5, 1))
print(m)
print(Matrix3x3.I())
print(m.xR(1/2))
print(m.plusM(Matrix3x3(Vector3(-1, -2, 3), Vector3(0, 1, 0), Vector3(-4, 5, 1))))
print(m.xV(Vector3(-4, 5, 1)))
print(m.transpose())
print(m.xM(Matrix3x3(Vector3(-1, -2, 3), Vector3(0, 1, 0), Vector3(-4, 5, 1))))
print(Matrix3x3.MRot(Vector3(1, 0, 0), 3.1415926))
"""
      
