import re

# text = "I love text. Text text text text text."
# pattern = r'text' # this will  output false in the re.match because the start of the two do not match
# # pattern = "I love text. Text text text text text." # The output of this is true because the starts of the two match
# regex = re.compile(pattern) # the .compile is better for reuse.
# match = regex.search(text)
# print(match)
#  we can see that it only returns the first 'text because the re.search is used to look for the first match

# if re.match(text, pattern):
#     print(True)
# else:
#     print(False)

text = 'The big red cat ate the fat rat.'
pattern = r'[A-Za-z]{3}' 
regex = re.compile(pattern)
print(regex.findall(text))