import numpy as np


def testFunction():
    print("Hello")
    a = np.random.rand(2,3)
    b = np.random.rand(3,2)
    print("a = ", a)
    print("b = ", b)
    c = a.dot(b)
    print("result = ", c)


if __name__ == "__main__":
    testFunction()