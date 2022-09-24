import math

class Vector:
    def __init__(self, elements = []):
        self.elements = list(elements)
        self.current = 0
    #numerical operators    
    def __add__(self, other):
         return Vector([x + y for x, y in zip(self.elements, other.elements)])
    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.elements, other.elements)])
    def __mul__(self, n): #dot product
       if type(n) == Vector:
           return sum([x*y for x, y in zip(self.elements, n.elements)])
       else:
            return Vector([n*x for x in self.elements])
    def __rmul__(self, n):
        return Vector([n*x for x in self.elements])
    def __pow__(self, n):
        return sum([x**n for x in self.elements])
    def __and__(self, other): #cross product
        a = self.elements
        b = other.elements
        
        return Vector([
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
        ])
    def __truediv__(self, n):
        if n == 0:
            raise ZeroDivisionError('division by zero')
        else:
            return Vector([x/n for x in self.elements])
    def __abs__(self):
        return sum([x*x for x in self.elements])**(0.5)
    def __pos__(self): # +A
        return Vector([x for x in self.elements])
    def __neg__(self): # -A
        return Vector([-x for x in self.elements])
    
    def __eq__(self, other):
        return self.elements == other.elements
    
    #sequins-type operators
    def __len__(self):
        return len(self.elements)
    def __contain__(self, item):
        return item in self.elements
    def __getitem__(self, key):
        return self.elements[key]
    def __setitem__(self, key, value):
        self.elements[key] = value
    def __delitem__(self, key):
        del self.elements[key]
    def append(self, value):
        self.elements.append(value)
    

    #vector functions
    def proj(self, other):
        return other*(self*other/(other*other))
    #iterator
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < len(self.elements):
            self.current += 1
            return self.elements[self.current - 1]
        else:
            raise StopIteration

    #print vector
    def __str__(self):
        return f'<{str(self.elements)[1:-1]}>'
    def __repr__(self):
        return f'Vector({self.elements})'
        
def unit(vector):
    return vector/abs(vector)

def zero(n = 3):
    result = Vector([0])
    for _ in range(n-1):
        result.append(0)
    return result

def sum(*args):
    result = zero(len(args[0]))
    for i in [arg for arg in args]:
        result += i
    return result

def sin(x):
    if type(x) == Vector:
        return Vector(map(math.sin, x))
    else:
        return math.sin(x)

def cos(x):
    if type(x) == Vector:
        return Vector(map(math.cos, x))
    else:
        return math.cos(x)

def tan(x):
    if type(x) == Vector:
        return Vector(map(math.tan, x))
    else:
        return math.tan(x)

def funcForVec(func):
    def applyToElement(*vecs):
        result = Vector()
        
        for i, _ in enumerate(vecs[0]):
            tmp_list = []
            for vec in vecs:
                tmp_list.append(vec[i])
            result.append(func(*tmp_list))
        
        return result
    return applyToElement

        
if __name__ == '__main__':
    
    a = Vector([3, 0])
    b = Vector([1, 2])
    c = Vector([0, 5])
    
    x, y = a

    print(x, y)
    
    @funcForVec
    def func1(x, y, z):
        return x + y - z

    print(func1(a, b, c))
    
    
    
        