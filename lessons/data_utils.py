"""Some helpful utility functions for working with CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Opens a file
    file_handle = open(filename, "r", encoding="utf8")

    # Read the file
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line -- looping through each row CSV file
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free it's resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented-table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result
