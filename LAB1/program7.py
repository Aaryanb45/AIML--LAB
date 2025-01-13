text="Helllo welcome to AIML"
length_string=len(text)
print(f"length of the string:{length_string}")
uppr_str=text.upper()
print(f"Upper case string:{uppr_str}")
lowr_str=text.lower()
print(f"Lower case string:{lowr_str}")

substring="Python"
is_substring_present = substring in text
print(f" Is '{substring}' present in the string: {is_substring_present}")

word_list = text.split()
print(f"List of words in the string: {word_list}")
