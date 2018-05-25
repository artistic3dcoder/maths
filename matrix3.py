
"""Matrix3 class."""
import math


class Matrix3(object):
    """Provides a row centric Matrix3 object with common Matrix3 operations.

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
               3: "tuples/list should contain three components each.",
               4: "int value required for row and column lookup.",
               5: "row and column lookup values can only be 0, 1, 2.",
               6: "row setter argument must be a list or tuple type."}

    def __init__(self, *values):
        if len(values) == 1 and type(values[0]) in self._VALID_TYPES:
            self._row_1 = [float(values[0]), 0.0, 0.0]
            self._row_2 = [0.0, float(values[0]), 0.0]
            self._row_3 = [0.0, 0.0, float(values[0])]
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
                self._row_1 = [float(values[0][0]), float(values[0][1]), float(values[0][2])]
                self._row_2 = [float(values[1][0]), float(values[1][1]), float(values[1][2])]
                self._row_3 = [float(values[2][0]), float(values[2][1]), float(values[2][2])]
            elif all([type(values[0]) in self._VALID_TYPES,
                      type(values[1]) in self._VALID_TYPES,
                      type(values[2]) in self._VALID_TYPES]):
                self._row_1 = [float(values[0]), 0.0, 0.0]
                self._row_2 = [0.0, float(values[1]), 0.0]
                self._row_3 = [0.0, 0.0, float(values[2])]
        elif len(values) == 9:
            result = [type(x) in self._VALID_TYPES for x in values]
            if not all(result):
                raise TypeError(self._ERRORS[2])
            self._row_1 = [float(values[0]), float(values[1]), float(values[2])]
            self._row_2 = [float(values[3]), float(values[4]), float(values[5])]
            self._row_3 = [float(values[6]), float(values[7]), float(values[8])]
        else:
            raise TypeError(self._ERRORS[2])

        self._matrix_data = [self._row_1, self._row_2, self._row_3]

    def __repr__(self):
        return "Matrix3: [{0}, {1}, {2}]".format(self._row_1, self._row_2, self._row_3)

    @property
    def row_1(self):
        """list: three floats making up first row."""
        return self._row_1

    @row_1.setter
    def row_1(self, value):
        if type(value) in self._VALID_ARRAY:
            if not all([type(x) in self._VALID_TYPES for x in value]):
                raise TypeError(self._ERRORS[2])
            self._row_1 = [float(x) for x in value]
            self._matrix_data[0] = self._row_1
        else:
            raise TypeError(self._ERRORS[6])

    @property
    def row_2(self):
        """list: three floats making up second row."""
        return self._row_2

    @row_2.setter
    def row_2(self, value):
        if type(value) in self._VALID_ARRAY:
            if not all([type(x) in self._VALID_TYPES for x in value]):
                raise TypeError(self._ERRORS[2])
            self._row_2 = [float(x) for x in value]
            self._matrix_data[1] = self._row_2
        else:
            raise TypeError(self._ERRORS[6])

    @property
    def row_3(self):
        """list: three floats making up third row."""
        return self._row_3

    @row_3.setter
    def row_3(self, value):
        if type(value) in self._VALID_Array:
            if not all([type(x) in self._VALID_TYPES for x in value]):
                raise TypeError(self._ERRORS[2])
            self._row_3 = [float(x) for x in value]
            self._matrix_data[2] = self._row_3
        else:
            raise TypeError(self._ERRORS[6])

    def adjugate_matrix(self, determinant, transposed_cofactor):
        """Compute the adjugate (inverse) of the transposed cofactor matrix3.

        This is the same as the inverse method except this method requires
        a determinant and cofactor matrix3 passed in.

        inv = 1/determinant * adj(transpose(cofactor))

        Args:
            determinant (float): determinant of matrix3
            transposed_cofactor (Matrix3): transposed cofactor matrix

        Returns:
            Matrix3: Adjugate Matrix3
        """
        if transposed_cofactor.__class__.__name__ != "Matrix3":
            raise TypeError(self._ERRORS[0])

        r1 = transposed_cofactor.row_1
        r2 = transposed_cofactor.row_2
        r3 = transposed_cofactor.row_3

        r1[0] /= determinant
        r1[1] /= determinant
        r1[2] /= determinant

        r2[0] /= determinant
        r2[1] /= determinant
        r2[2] /= determinant

        r3[0] /= determinant
        r3[1] /= determinant
        r3[2] /= determinant

        return Matrix3(r1, r2, r3)

    def as_list(self):
        """Return this matrix3 as a flattened list.

        Returns:
            list: xyz components
        """
        data = []
        for row in self._matrix_data:
            for column in row:
                data.append(column)
        return data

    def as_list_of_lists(self):
        """Return this matrix3 as a list.

        Returns:
            list of lists: xyz components
        """
        return self._matrix_data

    def cofactor_matrix(self, matrix3=None):
        """Compute the cofactor matrix.

        |a b c|   |+ - +|   |+a -b +c|
        |d e f| = |- + -| = |-d +e -f|
        |g h i|   |+ - +|   |+g -h +i|

        Args:
            matrix3 (Matrix3): optional matrix3 to compute cofactor for.
                               defaults to self.

        Returns:
            Matrix3: cofactored
        """
        if matrix3 and not matrix3.__class__.__name__ == "Matrix3":
            raise TypeError(self._ERRORS[0])
        r1 = matrix3.row_1 if matrix3 else self._row_1
        r2 = matrix3.row_2 if matrix3 else self._row_2
        r3 = matrix3.row_3 if matrix3 else self._row_3

        return Matrix3(1 * r1[0], -1 * r1[1], 1 * r1[2],
                       -1 * r2[0], 1 * r2[1], -1 * r2[2],
                       1 * r3[0], -1 * r3[1], 1 * r3[2])

    def column(self, row, column):
        """Return a given value from a row and column. Indexing start at 0.

        Args:
            row (int): row column lives in 0-2
            column(int): column to retrieve 0-2

        Returns:
            float: row / column value
        """
        if type(row) is not int or type(column) is not int:
            raise TypeError(self._ERRORS[4])
        if row > 2 or row < 0 or column > 2 or column < 0:
            raise ValueError(self._ERRORS[5])
        return self._matrix_data[row][column]

    def determinant(self):
        """Return the determinant of the matrix.

        Give a matrix3
        |a b c|
        |d e f|
        |g h i|
        The determinant is found using:
        det(m) = a(ei - fh) - b(di - fg) + c(dh - eg)

        Returns:
            float: determinant of the matrix
        """
        d1 = self._row_1[0] * (self._row_2[1] * self._row_3[2] - self._row_2[2] * self._row_3[1])
        d2 = self._row_1[1] * (self._row_2[0] * self._row_3[2] - self._row_2[2] * self._row_3[0])
        d3 = self._row_1[2] * (self._row_2[0] * self._row_3[1] - self._row_2[1] * self._row_3[0])
        return d1 - d2 + d3

    def inverse(self):
        """Return the inverse of this Matrix3.

        iM = 1/determinant * adj(trans(cofactor))

        Returns:
            Matrix3: inverse Matrix3
        """
        # find the determinant of the matrix
        determinant = self.determinant()
        # find the matrix of minors of the matrix
        matrix_of_minors = self.matrix_of_minors()
        # find the cofactor of the matrix of minors
        cofactor_matrix = self.cofactor_matrix(matrix_of_minors)
        # find the transpose of the cofactor matrix
        transpose_cofactor_matrix = self.transpose(cofactor_matrix)
        # find the adjugate (inverse) matrix
        inverse_matrix = self.adjugate_matrix(determinant, transpose_cofactor_matrix)

        return inverse_matrix

    def matrix_of_minors(self, matrix3=None):
        """Return the matrix of minors of this Matrix3

        construct matrix of minors

        |a b c|   ||ef| |df| |de||   |(e*i-h*i) (d*i-g*f) (d*h-g*e)|
        |d e f| = ||hi| |gi| |gh|| = |(b*i-h*c) (a*i-g*c) (a*h-g*b)|
        |g h i|   |              |   |(b*f-e*c) (a*f-d*c) (a*e-d*b)|
                  ||bc| |ac| |ab||
                  ||hi| |gi| |gh||
                  |              |
                  ||bc| |ac| |ab||
                  ||ef| |df| |de||

        Args:
            matrix3 (Matrix3): optional matrix3 to derive matrix of minors from.
                               defaults to self.
        Returns:
            Matrix3: Matrix3 Of Minors
        """
        if matrix3 and not matrix3.__class__.__name__ == "Matrix3":
            raise TypeError(self._ERRORS[0])
        r1 = matrix3.row_1 if matrix3 else self._row_1
        r2 = matrix3.row_2 if matrix3 else self._row_2
        r3 = matrix3.row_3 if matrix3 else self._row_3

        m1 = r2[1] * r3[2] - r3[1] * r2[2]
        m2 = r2[0] * r3[2] - r3[0] * r2[2]
        m3 = r2[0] * r3[1] - r3[0] * r2[1]

        m4 = r1[1] * r3[2] - r3[1] * r1[2]
        m5 = r1[0] * r3[2] - r3[0] * r1[2]
        m6 = r1[0] * r3[1] - r3[0] * r1[1]

        m7 = r1[1] * r2[2] - r2[1] * r1[2]
        m8 = r1[0] * r2[2] - r2[0] * r1[2]
        m9 = r1[0] * r2[1] - r2[0] * r1[1]

        return Matrix3(m1, m2, m3, m4, m5, m6, m7, m8, m9)
    
    def rotation_matrix(self, rotation, rotation_order="zyx"):
        """Convert a rotation to a rotation matrix.

        Args:
            rotation (tuple): rotation XYZ
            rotation_order (str): order of rotation 'xyz', 'zyx'
                                  defaults to 'zyx'

        Returns:
            rotation matrix
        """
        x = math.radians(rotation[0])
        y = math.radians(rotation[1])
        z = math.radians(rotation[2])

        cos = math.cos
        sin = math.sin
        if rotation_order == 'zyx':
            index_0 = cos(y) * cos(z)
            index_1 = cos(z) * sin(x) * sin(y) - cos(x) * sin(z)
            index_2 = cos(x) * cos(z) * sin(y) + sin(x) * sin(z)

            index_3 = cos(y) * sin(z)
            index_4 = cos(x) * cos(z) + sin(x) * sin(y) * sin(z)
            index_5 = -cos(z) * sin(x) + cos(x) * sin(y) * sin(z)

            index_6 = -sin(y)
            index_7 = -cos(y) * sin(x)
            index_8 = cos(x) * cos(y)
        elif rotation_order == 'xyz':
            index_0 = cos(y) * cos(z)
            index_1 = -cos(z) * sin(z)
            index_2 = sin(y)

            index_3 = cos(x) * sin(z) + sin(x) * sin(y) * cos(z)
            index_4 = cos(x) * cos(z) - sin(x) * sin(y) * sin(z)
            index_5 = -sin(x) * cos(y)

            index_6 = sin(x) * sin(z) - cos(x) * sin(y) * cos(z)
            index_7 = sin(x) * cos(z) + cos(x) * sin(y) * sin(z)
            index_8 = cos(x) * cos(y)

        rot_mat = ((index_0, index_1, index_2),
                   (index_3, index_4, index_5),
                   (index_6, index_7, index_8))

        return rot_mat
    def transpose(self, matrix3=None):
        """Calculate a transposed matrix3.

        |a b c|   |a d c|
        |d e f| = |b e f|
        |g h i|   |c f i|

        Args:
            matrix3: optional Matrix3 to transpose,
                     defaults to self
        Returns:
            Matrix3: transposed matrix3
        """
        if matrix3 and not matrix3.__class__.__name__ == "Matrix3":
            raise TypeError(self._ERRORS[0])
        r1 = matrix3.row_1 if matrix3 else self._row_1
        r2 = matrix3.row_2 if matrix3 else self._row_2
        r3 = matrix3.row_3 if matrix3 else self._row_3

        return Matrix3(r1[0], r2[0], r3[0], r1[1], r2[1], r3[1], r1[2], r2[2], r3[2])

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
