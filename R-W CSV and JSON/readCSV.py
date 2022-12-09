f = open('csvData.csv', newline='')
# print("JSON raw string:\n       " + rawString)

import csv
iterrator =  csv.reader(f)
for row in iterrator:
        print("New Row: ")
        print('! '.join(row))
f.close()