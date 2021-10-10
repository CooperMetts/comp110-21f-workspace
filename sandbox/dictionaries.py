"""Demonstrations of dictonary capabilities."""

# Declaring the type of a dictionary 
schools: dict[str, int]

# Intialize to an empty dictonary
schools = dict()

# set a key value pairing in the dictionary

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictonary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictonary by its key
schools.pop("Duke")

# Test for existence of a key
# This is a boolean expression saying 'Duke' (the key) in schools (the dictonary)
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}.")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200

print(schools)

# Demonstration of dictonary literals

# Empty dictionary literal 
# This --> schools = {} is a dictionary literal and this --> dict() is a dictionary constructor 
schools = {}  # Same as dict()

# Alternatively, intiatlize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a you try to access a key that does not exist: 
print(schools["UNCC"]) 
# Gives you KeyError: "UNCC"

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
