import re
from collections import Counter

 # Defines our regular expression for searching ZOP
 pattern = "[A-Z]{3}[\s]{1}[A-Z][\w\d\s\\',\-\*]*[.\!]"
 word_dict = {}

def zen_of_python(file):
     with open(file) as inputfile:
         content = inputfile.read()
         match = re.findall(pattern, content)
         for matches in match:
             clean_lines = matches[4:]
             print(clean_lines)
         for matches in match:
             clean_lines = matches[4:]
             words = clean_lines.split(' ')
             for word in words:
                 word = word.lower()
                 if word in word_dict:
                     word_dict[word] = word_dict[word] + 1
                 else:
                     word_dict[word] = 1

