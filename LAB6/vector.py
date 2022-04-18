from math import sqrt


class Vector3():
    
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __str__(self):
        return f'({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'
        
    def len(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def norm(self):
        l = self.len()
        if l != 0:
            new = Vector3(self.x / l, self.y / l, self.z / l)
        else:
            new = self
        return(new)

    def xR(self, r):
        return Vector3(self.x * r, self.y * r, self.z * r)

    def plusV(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def minusV(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotV(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def xV(self, v):
        return Vector3(self.y * v.z - self.z * v.y,
                       self.z * v.x - self.x * v.z,
                       self.x * v.y - self.y * v.x)

    
    
"""
v = Vector3(1, 2, 3)
print(v)
print(v.len())
print(v.norm())
print(v.xR(3))
print(v.plusV(Vector3(-9, -8, -7.0)))
print(v.minusV(Vector3(-9, -8, -7.0)))
print(v.dotV(Vector3(-1, -3, 2)))
print(v.xV(Vector3(-1, -3, 2)))
        
"""       
        
    
