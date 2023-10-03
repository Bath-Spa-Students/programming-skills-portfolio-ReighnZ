# The sys module is imported, giving access to a number of system-specific parameters and functions.
# The information about the Python version is retrieved via the sys.version property.
# The Python version you are using is then shown in a message that is printed to the console.

import sys
python_version = sys.version
print(f"You are using Python {python_version}")
