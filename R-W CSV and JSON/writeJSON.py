# define object for encoding
users = [{"name": "Jim Rudenberg", "profession":"Golf course maintenance staff", "age":55}, {"name": "Gloria Rudenberg", "profession":"human resources analyst", "age":50}]
print("list of users to write to file:\n        ",users)
import json
f = open("jsonData.json", "w")
json.dump(users, f)
f.close()