"""3d Vector class"""
import math


class Vector3(object):

    def __init__(self, *args):
        """Return a new Vector3 from a sequence of  floats."""
        if len(args) == 1 and type(args) in [list, tuple]:
            if len(args[0]) == 3:
                for item in args[0]:
                    if type(item) not in (float, int):
                        raise TypeError(self._get_error_code(2))
                self._x, self._y, self._z = args[0]
            else:
                raise TypeError(self._get_error_code(2))
        elif len(args) == 3:
            for item in args:
                if type(item) not in (float, int):
                    raise TypeError(self._get_error_code(2))
            self._x = args[0]
            self._y = args[1]
            self._z = args[2]
        else:
            raise TypeError(self._get_error_code(2))

    def __repr__(self):
        return "Vector3: [{0}, {1}, {2}]".format(self._x, self._y, self._z)

    def __add__(self, other):
        if not self._type_check(other):
            raise TypeError(self._get_error_code(0))
        new = [a + b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return Vector3(new)

    def __iadd__(self, other):
        if not self._type_check(other):
            raise TypeError(self._get_error_code(0))
        self._x, self._y, self._z = [a + b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __sub__(self, other):
        if not self._type_check(other):
            raise TypeError(self._get_error_code(0))
        new = [a - b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return Vector3(new)

    def __isub__(self, other):
        if not self._type_check(other):
            raise TypeError(self._get_error_code(0))
        self._x, self._y, self._z = [a - b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __mul__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._get_error_code(1))
        new = [a * other for a in self.as_tuple()]
        return Vector3(new)

    def __imul__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._get_error_code(1))
        self._x, self._y, self._z = [a * other for a in self.as_tuple()]
        return self

    def __div__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._get_error_code(1))
        new = [a / other for a in self.as_tuple()]
        return Vector3(new)

    def __idiv__(self, other):
        if not self._type_check_double(other):
            raise TypeError(self._get_error_code(1))
        self._x, self._y, self._z = [a / other for a in self.as_tuple()]
        return self

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if type(value) in (float, int):
            self._x = value
        else:
            raise TypeError("float or int value required.")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if type(value) in (float, int):
            self._y = value
        else:
            raise TypeError("float or int value required.")

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if type(value) in (float, int):
            self._z = value
        else:
            raise TypeError("float or int value required.")

    def angle_to(self, vector3):
        """Return the angle from this Vector3 to incoming Vector3

        The angle between the two vectors we  is
        acos(V1.dot(V2)/(V1.magnitude * V2.magnitude)).
        This returns the angle in radians so it is then converted to an angle.


        Returns:
            float: angle between two vectors
        """

        dot = self.dot(vector3)
        mag = self.magnitude() * vector3.magnitude()
        acos = math.acos(dot/mag)
        angle = acos * 180 / math.pi
        return angle

    def as_tuple(self):
        """Return this Vector3 as a list"""
        return self._x, self._y, self._z

    def cross(self, vector3):
        """Return the cross product between this Vector3 and an incoming Vector3

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
            raise TypeError(self._get_error_code(0))
        new = self - vector3
        return new.magnitude()

    @staticmethod
    def _type_check(data):
        """Check that this type coming in is of type Vector3"""
        if type(data) != Vector3:
            return False
        return True

    @staticmethod
    def _type_check_double(data):
        """Check that this type coming in is of type float"""
        if type(data) not in (float, int):
            return False
        return True

    @staticmethod
    def _get_error_code(code):
        if code == 0:
            return "argument must be of type Vector3"
        if code == 1:
            return "argument must be of type float or int"
        if code == 2:
            return "Input value should be a tuple or list containing with three float values."
