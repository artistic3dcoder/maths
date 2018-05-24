"""3d Vector class."""
import math


class Vector3(object):
    """Provides a Vector3 object with common Vector3 operations.

    Args:
        *values (float, int, tuple, list): default values for vector initialization.
                                           If no value is supplied vector will be initialized to 0.0, 0.0, 0.0
                                           Ints will be converted to floats

    """
    _VALID_TYPES = (int, float)
    _ERRORS = {0: "argument must be of type Vector3",
               1: "argument must be of type float or int",
               2: "Input value should be a tuple or list containing three float values"}
    
    def __init__(self, *values):
        if len(values) == 1 and type(values) in [list, tuple]:
            if len(values[0]) == 3:
                for item in values[0]:
                    if type(item) not in self._VALID_TYPES:
                        raise TypeError(self._ERRORS[2])
                self._x, self._y, self._z = float(values[0])
            else:
                raise TypeError(self._ERRORS[2])
        elif len(values) == 3:
            for item in values:
                if type(item) not in self._VALID_TYPES:
                    raise TypeError(self._ERRORS[2])
            self._x = float(values[0])
            self._y = float(values[1])
            self._z = float(values[2])
        else:
            raise TypeError(self._ERRORS[2])

    def __repr__(self):
        return "Vector3: [{0}, {1}, {2}]".format(self._x, self._y, self._z)

    def __add__(self, other):
        if not self._type_check(other):
            raise TypeError(self._ERRORS[0])
        new = [a + b for a, b in zip(self.as_list(), other.as_list())]
        return Vector3(new)

    def __iadd__(self, other):
        if not self._type_check(other):
            raise TypeError(self._ERRORS[0])
        self._x, self._y, self._z = [a + b for a, b in zip(self.as_list(), other.as_list())]
        return self

    def __sub__(self, other):
        if not self._type_check(other):
            raise TypeError(self._ERRORS[0])
        new = [a - b for a, b in zip(self.as_list(), other.as_list())]
        return Vector3(new)

    def __isub__(self, other):
        if not self._type_check(other):
            raise TypeError(self._ERRORS[0])
        self._x, self._y, self._z = [a - b for a, b in zip(self.as_list(), other.as_list())]
        return self

    def __mul__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._ERRORS[1])
        new = [a * other for a in self.as_list()]
        return Vector3(new)

    def __imul__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._ERRORS[1])
        self._x, self._y, self._z = [a * other for a in self.as_list()]
        return self

    def __div__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._ERRORS[1])
        new = [a / other for a in self.as_list()]
        return Vector3(new)

    def __idiv__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._ERRORS[1])
        self._x, self._y, self._z = [a / other for a in self.as_list()]
        return self

    @property
    def x(self):
        """float: x axis."""
        return self._x

    @x.setter
    def x(self, value):
        if type(value) in self._VALID_TYPES:
            self._x = value
        else:
            raise TypeError(self._ERRORS[1])

    @property
    def y(self):
        """float: y axis."""
        return self._y

    @y.setter
    def y(self, value):
        if type(value) in self._VALID_TYPES:
            self._y = value
        else:
            raise TypeError(self._ERRORS[1])

    @property
    def z(self):
        """float: z axis."""
        return self._z

    @z.setter
    def z(self, value):
        if type(value) in self._VALID_TYPES:
            self._z = value
        else:
            raise TypeError(self._ERRORS[1])

    def angle_to(self, vector3):
        """Return the angle from this Vector3 to incoming Vector3.

        The angle between the two vectors we  is
        acos(V1.dot(V2)/(V1.magnitude * V2.magnitude)).
        This returns the angle in radians so it is then converted to an angle.


        Returns:
            float: angle between two vectors
        """
        dot = self.dot(vector3)
        mag = self.magnitude() * vector3.magnitude()
        acos = math.acos(round(dot/mag, 6))
        angle = acos * 180 / math.pi
        return angle

    def as_list(self):
        """Return this Vector3 as a list.
        
        Returns:
            list: xyz components
        """
        return self._x, self._y, self._z

    def cross(self, vector3):
        """Return the cross product between this Vector3 and an incoming Vector3.

        a x b = (a2 * b3 - a3 * b2,
                 a3 * b1 - a1 * b3,
                 a1 * b2 - a2 * b1)

        Returns:
            Vector3: cross product vector
        """
        x = self._y * vector3.z - self._z * vector3.y
        y = self._z * vector3.x - self._x * vector3.z
        z = self._x * vector3.y - self._y * vector3.x
        return Vector3(x, y, z)

    def dot(self, vector3):
        """Return the dot product between this Vector3 and the incoming Vector3
         dot = a1 * b1 + a2 * b2 + a3 * b3

        Returns:
            float: dot product
        """
        return self._x * vector3.x + self._y * vector3.y + self._z * vector3.z

    def magnitude(self):
        """Return the length of the Vector"""
        return math.sqrt(math.pow(self._x, 2) + math.pow(self._y, 2) + math.pow(self._z, 2))

    def normalized(self):
        """Normalized Vector3 of class"""
        m = self.magnitude()
        return Vector3((self._x/m, self._y/m, self._z/m))

    def distance_to(self, vector3):
        """magnitude between this Vector3 and incoming Vector3.

        Returns:
            float: distance from this Vector3 to incoming Vector3.
        """
        if not self._type_check(vector3):
            raise TypeError(self._ERRORS[0])
        new = self - vector3
        return new.magnitude()

    @staticmethod
    def _type_check(data):
        """Check that this type coming in is of type Vector3"""
        if data.__class__.__name__ != "Vector3":
            return False
        return True

    def _type_check_double(self, data):
        """Check that this type coming in is of type float"""
        if type(data) not in self._VALID_TYPES:
            return False
        return True
