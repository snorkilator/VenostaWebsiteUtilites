f = open("jsonData.json", "r")
rawString = f.read()
f.close()
print("JSON raw string:\n       " + rawString)

import json
li = json.loads(rawString)
print("second object from json array:\n     ", li[1])