''' It defines a person's name, "Taylor Swift," with leading and trailing whitespace using the escape sequences '\t' (tab) and '\n' (newline).

It prints the name with the surrounding whitespace to show how it looks originally.

It demonstrates three stripping functions:
'lstrip()': Removes leading whitespace (tabs and spaces in this case) from the name.
'rstrip()': Removes trailing whitespace (tabs and newline in this case) from the name.
'strip()': Removes both leading and trailing whitespace, resulting in the name without any surrounding spaces or tabs. '''

person_name = "\t Taylor Swift \n"
print("\nName with Whitespace:")
print(person_name)
print("\nUsing lstrip():", person_name.lstrip())
print("Using rstrip():", person_name.rstrip())
print("Using strip():", person_name.strip())