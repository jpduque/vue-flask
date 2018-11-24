class InvalidOperation(RuntimeError):
    pass


class ConfigurationError(Exception):
    pass


class NotFoundException(RuntimeError):
    pass

class ArgumentNullException(RuntimeError):
    def __init__(self, param_name):
        super().__init__("Parameter cannot be null or empty: `%s`" % param_name)


class InvalidArgument(Exception):
    pass

class IntegrityError(Exception):
    pass

class WaitException(Exception):
    """Exception risen when the user should wait to perform an operation"""


class NotFoundException(RuntimeError):
    pass