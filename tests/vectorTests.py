from vectors import Vector
import unittest

class TestVectors(unittest.TestCase):

    def test_create(self):
        v1 = Vector.Vector([1,2])
        v2 = Vector.Vector([1,2])
        v3 = Vector.Vector([-11, 2])
        self.assertEqual(v1, v2)
        self.assertNotEqual(v2,v3)

    def test_add(self):
        v1 = Vector.Vector([1,2])
        v2 = Vector.Vector([1,2])
        v3 = v1 + v2
        v4 = Vector.Vector([2,4])
        self.assertEqual(v3,v4)

    def test_subtract(self):
        v1 = Vector.Vector([4, 2])
        v2 = Vector.Vector([2, 1])
        v3 = v1 - v2
        v4 = Vector.Vector([2, 1])
        self.assertEqual(v3, v4)

    def test_scalarMultiple(self):
        v1 = Vector.Vector([4, 2])
        s1 = 3
        v3 = v1.scalarMultiply(s1)
        v4 = Vector.Vector([12, 6])
        self.assertEqual(v3, v4)

if __name__ == '__main__':
    unittest.main()