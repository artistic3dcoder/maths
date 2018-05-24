"""Matrix3 class."""
import math


class Matrix3(object):
    """Provides a Matrix3 object with common Matrix3 operations.

    Args:
        *values (float, int, tuple, list): default values for vector initialization.
                                           If no value is supplied vector will be initialized to
                                           ((1.0, 0.0, 0.0),
                                            (0.0, 1.0, 0.0),
                                            (0.0, 0.0, 1.0))
                                           Ints will be converted to floats

    """
    _VALID_ARRAY = (list, tuple)
    _VALID_TYPES = (int, float)
    _ERRORS = {0: "argument must be of type Matrix3.",
               1: "argument must be of type float or int.",
               2: "tuple/list values should be float or int values.",
               3: "tuples/list should contain three components each."}

    def __init__(self, *values):
        if len(values) == 1 and type(values[0]) in self._VALID_TYPES:
            self._x = [float(values[0]), 0.0, 0.0]
            self._y = [0.0, float(values[0]), 0.0]
            self._z = [0.0, 0.0, float(values[0])]
        elif len(values) == 3:
            if all([type(values[0]) in self._VALID_ARRAY,
                    type(values[1]) in self._VALID_ARRAY,
                    type(values[2]) in self._VALID_ARRAY]):
                size_x = len(values[0]) == 3
                size_y = len(values[1]) == 3
                size_z = len(values[2]) == 3
                if not all([size_x, size_y, size_z]):
                    raise TypeError(self._ERRORS[3])
                is_x = [x in self._VALID_TYPES for x in values[0]]
                is_y = [y in self._VALID_TYPES for y in values[1]]
                is_z = [z in self._VALID_TYPES for z in values[2]]
                if not all([is_x, is_y, is_z]):
                    raise TypeError(self._ERRORS[2])
                self._x = [float(values[0][0]), float(values[0][1]), float(values[0][2])]
                self._y = [float(values[1][0]), float(values[1][1]), float(values[1][2])]
                self._z = [float(values[2][0]), float(values[2][1]), float(values[2][2])]
            elif all([type(values[0]) in self._VALID_TYPES,
                      type(values[1]) in self._VALID_TYPES,
                      type(values[2]) in self._VALID_TYPES]):
                self._x = [float(values[0]), 0.0, 0.0]
                self._y = [0.0, float(values[1]), 0.0]
                self._z = [0.0, 0.0, float(values[2])]
        elif len(values) == 9:
            result = [x in self._VALID_TYPES for x in values]
            if not all(result):
                raise TypeError(self._ERRORS[2])
            self._x = [float(values[0]), float(values[1]), float(values[2])]
            self._y = [float(values[3]), float(values[4]), float(values[5])]
            self._z = [float(values[6]), float(values[7]), float(values[8])]
        else:
            raise TypeError(self._ERRORS[2])

    def __repr__(self):
        return "Matrix3: [{0}, {1}, {2}]".format(self._x, self._y, self._z)

    @property
    def x(self):
        """float: x column."""
        return self._x

    @x.setter
    def x(self, value):
        if type(value) in self._VALID_TYPES:
            self._x = value
        else:
            raise TypeError(self._ERRORS[1])

    @property
    def y(self):
        """float: y column."""
        return self._y

    @y.setter
    def y(self, value):
        if type(value) in self._VALID_TYPES:
            self._y = value
        else:
            raise TypeError(self._ERRORS[1])

    @property
    def z(self):
        """float: z column."""
        return self._z

    @z.setter
    def z(self, value):
        if type(value) in self._VALID_TYPES:
            self._z = value
        else:
            raise TypeError(self._ERRORS[1])

    def as_list(self):
        """Return this matrix3 as a list.

        Returns:
            list: xyz components
        """
        return [self._x, self._y, self._z]

    @staticmethod
    def _type_check(data):
        """Check that this type coming in is of type Matrix3"""
        if data.__class__.__name__ != "Matrix3":
            return False
        return True

    def _type_check_double(self, data):
        """Check that this type coming in is of type float"""
        if type(data) not in self._VALID_TYPES:
            return False
        return True
