"""Examples of imports."""

from lessons import helpers

# Import using an alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful, THE_ANSWER


print(helpers.powerful(2, 4))
print(hp.THE_ANSWER)
print(f"imports.py: {__name__}")
print(powerful(2, 10))
print(THE_ANSWER)
