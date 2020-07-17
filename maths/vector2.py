"""3d Vector class."""
from typing import Union, List, Tuple
from collections import Iterable
from math import sqrt, pow

from maths.errors import VectorArgumentError, NumTypeArgumentError, VectorComponentArgumentError
from maths.vector import Vector


class Vector2(Vector):
    """Provides a Vector2 object with common Vector2 operations.

    Notes:
        - Argument values should be either floats or ints, ints will be converted to floats.
        - Providing no values will result in the Vector2 being filled with no values.
          Example :Vector2() would result in a Vector2 with the values [0.0, 0.0]
        - Providing a single value in x only will result in the Vector2 being filled with those values.
          Example: Vector2(10) would result in a Vector2 with values [10.0, 10.0]

    """
    def __init__(self,
                 x: Union[float, int, tuple, list] = None,
                 y: Union[float, int] = None):
        """Initialization of Vector2 class.

        Args:
            x: X value of Vector2.
               If a single value is passed in it will be propagated to z, y, and z.
               If a Tuple or List is passed in of length three it will be distributed to x, y, and z.
            y: Y value of Vector2.

        Raises:
                Vector3ComponentArgumentError: If arguments provided when instantiating Vector are incorrect.
        """
        super(Vector2, self).__init__()
        self._x, self._y = self._resolve_args(x=x, y=y)

    def _resolve_args(self,
                      x: Union[float, int, tuple, list] = None,
                      y: Union[float, int] = None) -> Tuple[float, float]:
        """Resolves Vector2 class args.

            Args:
                x: X value of Vector2.
                   If a single value is passed in it will be propagated to z, y, and z.
                   If a Tuple or List is passed in of length three it will be distributed to x, y, and z.
                y: Y value of Vector2.

            Raises:
                Vector3ComponentArgumentError: If arguments provided when instantiating Vector are incorrect.
        """
        if x is None and y is None:
            return 0.0, 0.0
        elif x and y is None:
            if isinstance(x, Iterable) and len(x) == 2:
                for v in x:
                    if not isinstance(v, self._ACCEPTED_TYPES):
                        raise VectorComponentArgumentError(invalid_type=",".join((type(z).__name__ for z in x)))
                return float(x[0]), float(x[1])
            else:
                if not isinstance(x, self._ACCEPTED_TYPES):
                    raise VectorComponentArgumentError(invalid_type=type(x).__name__)
                return float(x), float(x)
        else:
            if x and not isinstance(x, self._ACCEPTED_TYPES):
                raise VectorComponentArgumentError(invalid_type=type(x).__name__)
            if y and not isinstance(y, self._ACCEPTED_TYPES):
                raise VectorComponentArgumentError(invalid_type=type(y).__name__)
            return float(x) if x else 0.0, float(y) if y else 0.0

    def __repr__(self) -> str:
        return f"Vector2: [{self._x}, {self._y}]"

    def __iadd__(self, other: "Vector2") -> "self":
        """Add another Vector2 and return self"""
        if not isinstance(other, self._type):
            raise VectorArgumentError(expected_type=self._type, invalid_type=type(other))
        self._x, self._y = [a + b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __isub__(self, other: "Vector2") -> "self":
        """Subtract another Vector2 and return self."""
        if not isinstance(other, self._type):
            raise VectorArgumentError(expected_type=self._type, invalid_type=type(other))
        self._x, self._y = [a - b for a, b in zip(self.as_tuple(), other.as_tuple())]
        return self

    def __imul__(self, other: Union[int, float]) -> "self":
        """Multiply by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y = [a * other for a in self.as_tuple()]
        return self

    def __itruediv__(self, other: Union[int, float]) -> "self":
        """Divide by a number and return self."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        self._x, self._y = [a / other for a in self.as_tuple()]
        return self

    @property
    def x(self) -> float:
        """X component of Vector2."""
        return self._x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._x = value
        else:
            raise NumTypeArgumentError(invalid_type=type(value))

    @property
    def y(self) -> float:
        """Y component of Vector2."""
        return self._y

    @y.setter
    def y(self, value: Union[int, float]) -> None:
        if isinstance(value, self._ACCEPTED_TYPES):
            self._y = value
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


            Given: a = [x, y]

            mag =  square_root (a.x*a.x + a.y*a.y)

        """
        return sqrt(pow(self._x, 2) + pow(self._y, 2))

    def as_tuple(self) -> List[float]:
        """Return this Vector2's components as a X, Y, Z tuple."""
        return self._x, self._y

    def dot(self, other: "Vector2") -> float:
        """Return the dot product between this Vector2 and another Vector2.

        Args:
            other: Vector2 to compute dot against.

        Note:
            To compute the dot multiply each component by the other component
            and add all the components together.

            given: a = [x1, y1]
                   b = [x2, y2]
            dot = x1 * x2 + y1 * y2
        """
        return self._x * other.x + self._y * other.y

    def normalize(self) -> None:
        """Normalize this Vector2."""
        m = self.magnitude
        self._x = self._x / m
        self._y = self._y / m

    def normalized(self) -> "Vector2":
        """Normalized Vector2 of class.

        Note:
            To normalize a vector multiply each component by the vectors magnitude.

            give a = [x, y]
            mag = square_root (a.x*a.x + a.y*a.y)
            normalized_a = [a.x/mag, a.y/mag, a.z/mag]
        """
        m = self.magnitude
        return Vector2(self._x/m, self._y/m)
