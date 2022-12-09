# define object for encoding
users = [{"name": "Jim Rudenberg", "profession":"Golf course maintenance staff", "age":55}, {"name": "Gloria Rudenberg", "profession":"human resources analyst", "age":50}]
print("list of users to write to file:\n        ",users)
import csv
f = open("csvData.csv", "w")
w = csv.writer(f)
w.writerow(["goodbye", "see you later", "have a good one"])
w.writerow(["hello","good day", "good evening", "good morning"])
f.close()