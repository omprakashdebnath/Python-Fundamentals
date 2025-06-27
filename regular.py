import re

line = "cats are smarterthan dogs"
match0bj = re.match(r"cats", line)
print(match0bj.start(), match0bj.end())
print("match0bj.group() : ", match0bj.group())

import re

line = "Cats are smarter than dogs"
matchObj = re.search(r"than", line)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())
