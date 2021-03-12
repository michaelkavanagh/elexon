class ElexonException(Exception):
    """The base Elexon Exception that all other exception classes extend."""
    pass


class NoContentException(ElexonException):
    """raised when no data was returned (status 204)"""
    pass
