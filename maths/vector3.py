"""3d Vector class."""
from __future__ import annotations

from collections.abc import Iterable
from math import pi, acos, sqrt, pow
from typing import Self

from .errors import Vector3ArgumentError, NumTypeArgumentError, Vector3ComponentArgumentError


class Vector3(object):
    """Provides a Vector3 object with common Vector3 operations.

    Notes:
        - Argument values should be either floats or ints, ints will be converted to floats.
        - Providing no values will result in the Vector3 being filled with no values.
          Example : Vector3() would result in a Vector3 with the values [0.0, 0.0, 0.0]
        - Providing a single value in x only will result in the Vector3 being filled with those values.
          Example : Vector3(10) would result in a Vector3 with values [10.0, 10.0, 10.0]

    """
    __slots__ = ("_x", "_y", "_z")
    _ACCEPTED_TYPES = (int, float)

    def __init__(self,
                 x: float | int | tuple | list = None,
                 y: float | int = None,
                 z: float | int = None):
        """Initialization of Vector3 class.

        Args:
            x: X value of Vector 3.
               If a single value is passed in it will be propagated to z, y, and z.
               If a Tuple or List is passed in of length three it will be distributed to x, y, and z.
            y: Y value of Vector 3.
            z: Z value of Vector 3.

        Raises:
                Vector3ComponentArgumentError: If arguments provided when instantiating Vector are incorrect.
        """
        self._x, self._y, self._z = self._resolve_args(x=x, y=y, z=z)

    def _resolve_args(self,
                      x: float | int | tuple | list = None,
                      y: float | int = None,
                      z: float | int = None) -> tuple[float, float, float]:
        """Resolves Vector3 class args.

            Args:
                x: X value of Vector 3.
                   If a single value is passed in it will be propagated to z, y, and z.
                   If a Tuple or List is passed in of length three it will be distributed to x, y, and z.
                y: Y value of Vector 3.
                z: Z value of Vector 3.

            Raises:
                Vector3ComponentArgumentError: If arguments provided when instantiating Vector are incorrect.
        """
        if x is None and y is None and z is None:
            return 0.0, 0.0, 0.0
        elif x is not None and y is None and z is None:
            if isinstance(x, Iterable) and len(x) == 3:
                x0, x1, x2 = x  # tuple unpacking
                for v in (x0, x1, x2):
                    if v is not None and not isinstance(v, self._ACCEPTED_TYPES):
                        raise Vector3ComponentArgumentError(
                            invalid_type=",".join(type(z).__name__ for z in (x0, x1, x2)))
                return float(x0), float(x1), float(x2)
            else:
                if not isinstance(x, self._ACCEPTED_TYPES):
                    raise Vector3ComponentArgumentError(invalid_type=type(x).__name__)
                return float(x), float(x), float(x)
        else:
            if x is not None and not isinstance(x, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(x).__name__)
            if y is not None and not isinstance(y, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(y).__name__)
            if z is not None and not isinstance(z, self._ACCEPTED_TYPES):
                raise Vector3ComponentArgumentError(invalid_type=type(z).__name__)
            return (
                float(x) if x else 0.0, 
                float(y) if y else 0.0, 
                float(z) if z else 0.0
                )

    def __repr__(self) -> str:
        return f"Vector3: [{self._x}, {self._y}, {self._z}]"

    def __add__(self, other: "Vector3") -> "Vector3":
        """Add another Vector3 and return a new Vector3"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        a, b = self.as_tuple(), other.as_tuple()
        return Vector3([x + y for x, y in zip(a, b)])

    def __iadd__(self, other: "Vector3") -> Self:
        """Add another Vector3 and return self"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        a, b = self.as_tuple(), other.as_tuple()
        self._x, self._y, self._z = [x + y for x, y in zip(a,b)]
        return self

    def __sub__(self, other: "Vector3") -> "Vector3":
        """Subtract another Vector3 and return a new Vector3"""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        a, b = self.as_tuple(), other.as_tuple()
        return Vector3([x - y for x, y in zip(a,b)])

    def __isub__(self, other: "Vector3") -> "Vector3":
        """Subtract another Vector3 and return self."""
        if not isinstance(other, type(self)):
            raise Vector3ArgumentError(invalid_type=type(other))
        a, b = self.as_tuple(), other.as_tuple()
        self._x, self._y, self._z = [x - y for x, y in zip(a,b)]
        return self

    def __mul__(self, other: int | float) -> "Vector3":
        """Multiply by a number and return a new Vector3."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return Vector3([a * other for a in (self._x, self._y, self._z)])

    def __imul__(self, other: int | float) -> Self:
        """Multiply by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a * other for a in (self._x, self._y, self._z)]
        return self

    def __truediv__(self, other: int | float) -> "Vector3":
        """Divide by a number and return a new Vector3."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return Vector3([a / other for a in (self._x, self._y, self._z)])

    def __itruediv__(self, other: int | float) -> Self:
        """Divide by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y, self._z = [a / other for a in (self._x, self._y, self._z)]
        return self

    @property
    def x(self) -> float:
        """X component of Vector3."""
        return self._x

    @x.setter
    def x(self, value: int | float) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._x = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
    def y(self) -> float:
        """Y component of Vector3."""
        return self._y

    @y.setter
    def y(self, value: int | float) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._y = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
    def z(self) -> float:
        """Z component of Vector3."""
        return self._z

    @z.setter
    def z(self, value: int | float) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._z = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
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
        acos_ = acos(self.dot(other) / (self.magnitude * other.magnitude))
        angle = acos_ * 180 / pi
        return round(angle, precision)

    def as_tuple(self) -> tuple[float, float, float]:
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

    def normalize(self) -> None:
        """Normalize this Vector3."""
        m = self.magnitude
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
        m = self.magnitude
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
        return new.magnitude
