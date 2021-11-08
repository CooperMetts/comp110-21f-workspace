"""Utility functions."""

from csv import DictReader

__author__ = "730336784"

# Define your functions below


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
    # the 'row' in this for...in... loop is referring to the dictonaries in table? So it's essentially saying for each dictionary in the list named table, right? 
    for row in table:
        # 'item' establishes a new variable of type str and it is assigned the value of the specific dictonary (or row) at the value of column (which is a parameter of this function)
        # ex: item: str = row['date'] -> item: str = '10/16' (this would be for loop & row one) THEN item: str = '10/17' (this would be for loop & row two) and so on for this patern
        item: str = row[column]
        # this adds item to the 'result' list or the new list we're making 
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented-table to a column-oriented table."""
    # making new dictonary that will be the column-oriented returned dictonary   
    result: dict[str, list[str]] = {}

    # this states what the first row is, where row-table[0] refers to the first dictonary in the list(which list is passed into the row_table parameter) 
    first_row: dict[str, str] = row_table[0]
    # column in this for...in... loop is refering to the left-hand side or the keys of the dict first-row (first row being the first dictonary of the list row-table — a parameter in this function), and then looping through each of those keys
    for column in first_row:
        # the 'result[column]' part of this line takes the keys of the first dictonary in row_table(parameter of this function) and assigns them to be the keys of the new column-oriented results dictonary
        # we use column_values on the right side of the '=' that function gets us all the values in a column, and the for...in... loop we called the column_values function in loops through all the columns in the first row (aka the first dictionary) 
        result[column] = column_values(row_table, column)
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]: 
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `Y` (a parameter) rows of data for each column.."""
    # establish empty dictionary 
    trimmed_dictionary: dict[str, list[str]] = {}

    # this is saying for value in whatever dict is passed to the parameter x
    for column in x: 
        # list for storing the frist N  values in the column 
        empty_one: list[str] = []
        # this is a counter variable
        i: int = 0
        # see notes for help --> it's linked in the google doc but also in your google jam 
        if len(x[column]) < y:
            y = len(x[column])
        # this is saying while the counter variable is less than the value given to the parameter y to ... 
        while i < y: 
            # see notes for explanation   
            empty_one.append(x[column][i])
            i = i + 1
        trimmed_dictionary[column] = empty_one
    return trimmed_dictionary


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]: 
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns.v."""
    # establishes the new dictonary
    new_dictionary: dict[str, list[str]] = {}
    # this is saying for item (item being the element in the index-element pair of parameter b (a list) in the parameter b (a list) do ...)
    for item in b: 
        # this is assigning the key of the key-value pair in the new dictionary (named new_dictionary) to be whatever element from the index-element pairings in parameter the for...in... loop is on to be the key of new_dictionary
        # this 'a[item]' is assigning the value of the key-value pair of new_dictionary at new_dictionary[item] to be the list of values in the a parameter (a dictionary) at whatever key (refered to as item in the for...in... loop) the for...in... loop is on 
        new_dictionary[item] = a[item]
    return new_dictionary


def concat(c: dict[str, list[str]], d: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined.."""
    new_one: dict[str, list[str]] = {}
    # this is saying for each key (column) in the key-value pair of whatever dict is passed to c
    for column in c:
        # 'new_dictionary[column]' assigns the key-values of 'new-dictionary' to whatever key (or column) of the dict — parameter c — the for...in... loop is currently on
        # 'c[column]' assigns the value of new_dictonary[at whatever key] to be the value of the dict c[at whatever key (or column) the for...in... loop is currently on]
        new_one[column] = c[column] 
    # this is saying for key (column) in the key-value pair of whatever dict is passed to d 
    for column in d: 
        # this checks to see if the key in whatever dict is passed to th parameter d is already in the new dict we are creating (new_one)
        if column in new_one:
            # this is saying if the key is already in new_one, then the key's corresponding value should be the values of c[column] and d[column]
            new_one[column] = c[column] + d[column]
        else: 
            # this is saying if the key is not already in new_one to add it to new_one and set its value to the value of the dict d[at whatever key (or column) the for...in... loop is currently on]
            new_one[column] = d[column]
    return new_one


# r being combo and s being ease
def yes_understanding(r: dict[str, list[str]], s: dict[str, list[int]], key_1: str, key_2: str, key_3: str) -> list[int]: 
    yes_ease: list[int] = []
    i: int = 0 
    count: int = 1
    while i < len(r[key_1]):
        if r[key_1][i] == "Yes" or r[key_2][i] == "Yes" and (s[key_3][i] == "5" or s[key_3][i] == "6" or s[key_3][i] == "7"):
            yes_ease.append(count)
            count = count + 1
            i = i + 1
        else: 
            i = i + 1
    return yes_ease


def no_understanding(e: dict[str, list[str]], f: dict[str, list[str]], key_1: str, key_2: str, key_3: str) -> list[int]:
    no_ease: list[int] = []
    i: int = 0 
    count: int = 1
    while i < len(e[key_1]):
        if e[key_1][i] == "No" and e[key_2][i] == "No" and (f[key_3][i] == "5" or f[key_3][i] == "6" or f[key_3][i] == "7"):
            no_ease.append(count)
            count = count + 1
            i = i + 1
        else: 
            i = i + 1
    return no_ease

def count(responses: list[str]) -> dict[str, int]: 
    occurences: dict[str, int] = {}
    for response in responses: 
        if response in occurences: 
            occurences[response] = occurences[response] + 1
        else: 
            occurences[response] = 1
    return occurences

def no_count(responses_principles: dict[str, list[str]], responses_a: dict[str, list[str]], key_1: str, key_2: str) -> list[int]: 
    occurences: list[int] = []
    i: int = 0
    count: int = 1
    while i < len(responses_a[key_2]):
        if responses_principles[key_1][i] == "No" and responses_a[key_2][i] == "No":
            occurences.append(count)
            count = count + 1
            i = i + 1
        else: 
            i = i + 1
    return occurences

def yes_count(responses_principles: dict[str, list[str]], responses_a: dict[str, list[str]], key_1: str, key_2: str) -> list[int]: 
    occurences: list[int] = []
    i: int = 0
    count: int = 1
    while i < len(responses_a[key_2]):
        if responses_principles[key_1][i] == "Yes" or responses_a[key_2][i] == "Yes":
            occurences.append(count)
            count = count + 1
            i = i + 1
        else: 
            i = i + 1
    return occurences
    
    
    
