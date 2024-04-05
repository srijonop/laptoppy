# String methods
## Python provides a set of built-in methods thatwe can use to alter and modify the strings.

# ## upper() :
# The upper() method converts a string to upper case.
# ## Example :
str1="aKash"
print(str1.upper())

# ## lower()
# The lower() method converts a string to lower case.
# ## Example:
print(str1.lower())

# ## rstrip() : 
#the rstrip() removes any trailing characters.
# ## Example:
str2="srijon!!!!!!!!!"
print(str2.rstrip("!"))

# ## replace() : 
# The replace() method replaces all occurences of a string with another string.
# ## Example:
print(str2.replace("sr","ak"))

# ## split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items.
# ## Example:
str3="Silver Spoon"
print(str3.split(" "))
print(str3.split("  "))

# ## capitalize() : 
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
# ## Example:
str4="i am a new COdEr"
print(str4.capitalize())

# ## center() : 
# The center() method aligns the string to the center as per the parameters given by the user.
# ## Example:
print(str4.center(60))

### Example:
str5="Welcome to the Console!!!"
print(str5.center(60,"."))

# ## count() :
# The count() method returns the number of times the given value has occurred within the given string.
# ## Example:
str6="Abracadabra"
print(str6.count("b"))
print(len(str5))
  




