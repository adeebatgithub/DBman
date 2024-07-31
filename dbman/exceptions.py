

class TableNotFoundError(Exception):
    """
    Raise Exception when database not found in the given path
    """
    pass


class TableNameError(Exception):
    """
    Raise Exception when the table name is not allowed
    """
    pass


class ColumnNotFoundError(Exception):
    """
    Raise Exception when the given column name not found while accessing database through column name
    """
    pass


class ColumnNameError(Exception):
    """
    Raise Exception if the name of column is not allowed
    """
    pass


class DataNotFoundError(Exception):                         
    """
    Raise Exception when the query data is empty
    """
    pass
