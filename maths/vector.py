from typing import Union, List
from math import pi, acos
from abc import ABC, abstractmethod

from errors import VectorArgumentError, NumTypeArgumentError


class Vector(ABC):
    _ACCEPTED_TYPES = (int, float)

    def __init__(self):
        self._type = type(self)

    @abstractmethod
    def __repr__(self) -> str:
        pass

    def __add__(self, other: "Vector") -> "Vector":
        """Add another Vector and return a new Vector"""
        if not isinstance(other, type(self)):
            raise VectorArgumentError(invalid_type=type(other))
        return self._type([a + b for a, b in zip(self.as_tuple(), other.as_tuple())])

    @abstractmethod
    def __iadd__(self, other: "Vector") -> "self":
        """Add another Vector and return self"""
        pass

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract another Vector and return a new Vector"""
        if not isinstance(other, self._type):
            raise VectorArgumentError(expected_type=self._type, invalid_type=type(other))
        return self._type([a - b for a, b in zip(self.as_tuple(), other.as_tuple())])

    @abstractmethod
    def __isub__(self, other: "Vector") -> "self":
        """Subtract another Vector and return self."""
        pass

    def __mul__(self, other: Union[int, float]) -> "Vector":
        """Multiply by a number and return a new Vector."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return self._type([a * other for a in self.as_tuple()])

    @abstractmethod
    def __imul__(self, other: Union[int, float]) -> "self":
        """Multiply by a number and return self."""
        pass

    def __truediv__(self, other: Union[int, float]) -> "Vector":
        """Divide by a number and return a new Vector."""
        if not isinstance(other, self._ACCEPTED_TYPES):
            raise NumTypeArgumentError(invalid_type=type(other))
        return self._type([a / other for a in self.as_tuple()])

    @abstractmethod
    def __itruediv__(self, other: Union[int, float]) -> "self":
        """Divide by a number and return self."""
        pass

    @property
    @abstractmethod
    def magnitude(self) -> float:
        """Return the length of the Vector.

        Note:
            To compute the magnitude (length) of a vector:
            1. Compute each component to the power of 2
            2. Add the products together
            3. Compute the sqrt of the result.
        """
        pass

    @abstractmethod
    def as_tuple(self) -> List[float]:
        """Return this Vector2's components as a X, Y, Z tuple."""
        pass

    @abstractmethod
    def dot(self, other: "Vector") -> float:
        """Return the dot product between this Vector2 and another Vector2.

        Args:
            other: Vector2 to compute dot against.

        Note:
            To compute the dot multiply each component by the other component
            and add all the components together.
        """
        pass

    @abstractmethod
    def normalize(self) -> None:
        """Normalize this Vector."""
        pass

    @abstractmethod
    def normalized(self) -> "Vector":
        """Normalized Vector of class.

        Note:
            To normalize a vector multiply each component by the vectors magnitude.
        """
        pass

    def angle_to(self, other: "Vector", precision: int = 6) -> float:
        """Return the angle from this Vector to incoming Vector in degrees.

        Args:
            other: Vector to measure angle to.
            precision: how many decimals to round to when determining acos.

        Note:
            The angle between the two vectors is
            acos(V1.dot(V2)/(V1.magnitude * V2.magnitude)).
            This returns the angle in radians so it is then converted to an angle.
        """
        acos_ = acos(self.dot(other) / (self.magnitude * other.magnitude))
        angle = acos_ * 180 / pi
        return round(angle, precision)

    def distance_to(self, other: "Vector") -> float:
        """Returns the magnitude between this Vector2 and incoming Vector2.

        Args:
            other: Vector to measure distance to.

        Note:
            Distance from this Vector2 to incoming Vector2.
        """
        if not isinstance(other, self._type):
            raise VectorArgumentError(expected_type=self._type, invalid_type=type(other))
        new = self - other
        return new.magnitude
