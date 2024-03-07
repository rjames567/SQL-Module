class Error(Exception):
    """Base class for all exceptions within the module."""

    def __init__(self,
                 error_code: str,
                 error_message: str
                 ):
        self._message = f"SQL Error [{error_code}]: {error_message}"

    def __repr__(self):
        return self._message

    def __str__(self):
        return self._message


class DataError(Error):
    pass


class DatabaseError(Error):
    pass


class IntegrityError(Error):
    pass


class InternalError(Error):
    pass


class ProgrammingError(Error):
    pass


class Warning(Error):
    pass
