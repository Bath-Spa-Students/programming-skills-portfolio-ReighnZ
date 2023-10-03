# The datetime module is imported, offering classes and functions for managing dates and times.
# To get the current date and time it uses the datetime.datetime.now() function.
# Using the strftime method, it formats the current date and time as a string. It is structured as "Year-Month-Day Hour:Minute:Second" in this instance.
# The formatted date and time are then printed to the console.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))