"""Error types for maths package."""


class InvalidArgumentError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class VectorArgumentError(InvalidArgumentError):
    """Error raised when a Vector3 type argument is expected."""
    def __init__(self, expected_type, invalid_type):
        err = f"\n\tArgument must be of type {expected_type}. Got: {invalid_type}"
        super().__init__(err, err)


class VectorComponentArgumentError(InvalidArgumentError):
    """Error raised when a Vector3 type components are not a float or int."""
    def __init__(self, invalid_type):
        err = f"\n\tVector arguments should be either floats, ints, or None.\n\tGot: {invalid_type}"
        super().__init__(err, err)


class NumTypeArgumentError(InvalidArgumentError):
    """Error raised when a num type argument is expected."""
    def __init__(self, invalid_type):
        err = f"\n\tArgument must be of type float or int. Got: {invalid_type}"
        super().__init__(err, err)
