import re
from collections import Counter

 # Defines our regular expression for searching ZOP
 pattern = "[A-Z]{3}[\s]{1}[A-Z][\w\d\s\\',\-\*]*[.\!]"
 word_dict = {}

