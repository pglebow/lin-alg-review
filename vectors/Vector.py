class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        try:
            if not other or self.dimension != other.dimension:
                raise ValueError
            return Vector(coordinates=[x + y for x, y in zip(self.coordinates, other.coordinates)])

        except ValueError:
            raise ValueError('The vectors must not be empty and have the same dimension to add them')

    def __sub__(self, other):
        try:
            if not other or self.dimension != other.dimension:
                raise ValueError
            return Vector(coordinates=[x - y for x, y in zip(self.coordinates, other.coordinates)])

        except ValueError:
            raise ValueError('The vectors must not be empty and have the same dimension to subtract them')

    def scalarMultiply(self, scalar):
        return Vector(coordinates=tuple(x * scalar for x in self.coordinates))


