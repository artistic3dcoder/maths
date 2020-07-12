"""3d Vector class."""
from typing import Union, List
from collections import Iterable
from math import pi, acos, sqrt, pow

from maths.errors import Vector3ArgumentError, NumTypeArgumentError, Vector3ComponentArgumentError


class Vector3(object):
    """Provides a Vector3 object with common Vector3 operations.

    Notes:
        - Argument values should be either floats or ints, ints will be converted to floats.
        - Providing no values will result in the Vector3 being filled with no values.
          Example :Vector3() would result in a Vector3 with the values [0.0, 0.0, 0.0]
        - Providing a single value in x only will result in the Vector3 being filled with those values.
          Example: Vector3(10) would result in a Vector3 with values [10.0, 10.0, 10.0]

    """
    _ACCEPTED_TYPES = (int, float)

    def __init__(self, x=None, y=None, z=None):

        if x is None and y is None and z is None:
            self._x = self._y = self._z = 0.0
        elif x and y is None and z is None:
            if isinstance(x, Iterable) and len(x) == 3:
                for v in x:
                    if not isinstance(v, self._ACCEPTED_TYPES):
                        raise Vector3ComponentArgumentError(invalid_type=",".join((type(z).__name__ for z in x)))
                self._x, self._y, self._z = float(x[0]), float(x[1]), float(x[2])
            else:
                if not isinstance(x, self._ACCEPTED_TYPES):
                    raise Vector3ComponentArgumentError(invalid_type=type(x).__name__)
                self._x = self._y = self._z = float(x)
        else:
            if x and not isinstance(x, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(x).__name__)
            if y and not isinstance(y, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(y).__name__)
            if z and not isinstance(z, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(z).__name__)
            self._x = float(x) if x else 0.0
            self._y = float(y) if y else 0.0
            self._z = float(z) if z else 0.0

    def __repr__(self) -> str:
        return "Vector3: [{0}, {1}, {2}]".format(self._x, self._y, self._z)

    def __add__(self, other: "Vector3") -> "Vector3":
        """Add another Vector3 and return a new Vector3"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        return Vector3([a + b for a, b in zip(self.as_tuple(), other.as_tuple())])

    def __iadd__(self, other: "Vector3") -> "self":
        """Add another Vector3 and return self"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a + b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __sub__(self, other: "Vector3") -> "Vector3":
        """Subtract another Vector3 and return a new Vector3"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        return Vector3([a - b for a, b in zip(self.as_tuple(), other.as_tuple())])

    def __isub__(self, other: "Vector3") -> "self":
        """Subtract another Vector3 and return self."""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a - b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __mul__(self, other: Union[int, float]) -> "Vector3":
        """Multiply by a number and return a new Vector3."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return Vector3([a * other for a in self.as_tuple()])

    def __imul__(self, other: Union[int, float]) -> "self":
        """Multiply by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a * other for a in self.as_tuple()]
        return self

    def __truediv__(self, other: Union[int, float]) -> "Vector3":
        """Divide by a number and return a new Vector3."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return Vector3([a / other for a in self.as_tuple()])

    def __itruediv__(self, other: Union[int, float]) -> "self":
        """Divide by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a / other for a in self.as_tuple()]
        return self

    @property
    def x(self) -> float:
        """X component of Vector3."""
        return self._x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._x = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
    def y(self) -> float:
        """Y component of Vector3."""
        return self._y

    @y.setter
    def y(self, value: Union[int, float]) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._y = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
    def z(self) -> float:
        """Z component of Vector3."""
        return self._z

    @z.setter
    def z(self, value: Union[int, float]) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._z = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    def angle_to(self, other: "Vector3", precision: int = 6) -> float:
        """Return the angle from this Vector3 to incoming Vector3 in degrees.

        Args:
            other: Vector3 to measure angle to.
            precision: how many decimals to round to when determining acos.

        Note:
            The angle between the two vectors is
            acos(V1.dot(V2)/(V1.magnitude * V2.magnitude)).
            This returns the angle in radians so it is then converted to an angle.
        """
        acos_ = acos(self.dot(other) / (self.magnitude() * other.magnitude()))
        angle = acos_ * 180 / pi
        return round(angle, precision)

    def as_tuple(self) -> List[float]:
        """Return this Vector3's components as a X, Y, Z tuple."""
        return self._x, self._y, self._z

    def cross(self, other: "Vector3") -> "Vector3":
        """Return the cross product between this Vector3 and an incoming Vector3.

        Args:
            other: Vector3 to cross with.

        Note:
            given: a = [x1, y1, z1]
                   b = [x2, y2, z2]
            a x b = (a.y * b.z - a.z * b.y,
                     a.z * b.x - a.x * b.z,
                     a.x * b.y - a.y * b.x)
        """
        x = self._y * other.z - self._z * other.y
        y = self._z * other.x - self._x * other.z
        z = self._x * other.y - self._y * other.x
        return Vector3(x, y, z)

    def dot(self, other: "Vector3") -> float:
        """Return the dot product between this Vector3 and another Vector3.

        Args:
            other: Vector3 to compute dot against.

        Note:
            To compute the dot multiply each component by the other component
            and add all the components together.

            given: a = [x1, y1, z1]
                   b = [x2, y2, z2]
            dot = x1 * x2 + y1 * y2 + z1 * z2
        """
        return self._x * other.x + self._y * other.y + self._z * other.z

    def magnitude(self) -> float:
        """Return the length of the Vector.

        Note:
            To compute the magnitude (length) of a vector:
            1. Compute each component to the power of 2
            2. Add the products together
            3. Compute the sqrt of the result.


            Given: a = [x, y, z]

            mag =  square_root (a.x*a.x + a.y*a.y + a.z*a.z)

        """
        return sqrt(pow(self._x, 2) + pow(self._y, 2) + pow(self._z, 2))

    def normalize(self) -> None:
        """Normalize this Vector3."""
        m = self.magnitude()
        self._x = self._x / m
        self._y = self._y / m
        self._z = self._z / m

    def normalized(self) -> "Vector3":
        """Normalized Vector3 of class.

        Note:
            To normalize a vector multiply each component by the vectors magnitude.

            give a = [x, y, z]
            mag = square_root (a.x*a.x + a.y*a.y + a.z*a.z)
            normalized_a = [a.x/mag, a.y/mag, a.z/mag]
        """
        m = self.magnitude()
        return Vector3(self._x/m, self._y/m, self._z/m)

    def distance_to(self, other: "Vector3") -> float:
        """Returns the magnitude between this Vector3 and incoming Vector3.

        Args:
            other: Vector3 to measure distance to.

        Note:
            Distance from this Vector3 to incoming Vector3.
        """
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        new = self - other
        return new.magnitude()
