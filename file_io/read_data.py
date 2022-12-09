from io import StringIO
import csv
import json


# read_data uses the file ending to determine CSV or JSON formats
# if successful, it returns a list of the rows read
# if unsuccessful, it prints an error message and returns an empty list
def read_data(file_name):
    if file_name.endswith('.csv'):
        return read_csv_file(file_name)
    elif file_name.endswith('json'):
        return read_json_file(file_name)
    else:
        print('file name "{0}" must end in .csv or .json'. format(file_name))
        return []


# reads the ascii text content of a file
# if successful, it returns the content as a string
# if unsuccessful, it prints an error message and returns None
def read_file_contents(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as e:
        print('error "{0}" reading file "{1}"'.format(e, file_name))
        return None


# reads the csv content of a file
# if successful, it returns a list of the rows read
# if unsuccessful, it prints an error message and returns an empty list
def read_csv_file(file_name):
    csv_str = read_file_contents(file_name)
    f = StringIO(csv_str)
    reader = csv.reader(f)
    try:
        return [row for row in reader]
    except Exception as e:
        print('csv format error in file "{0}"'.format(file_name))
        return []


# reads the json content of a file
# if successful, it returns a list of the rows read
# if unsuccessful, it prints an error message and returns an empty list
def read_json_file(file_name):
    json_str = read_file_contents(file_name)
    print(len(json_str))
    if json_str is None:
        return []
    try:
        return json.loads(json_str)
    except Exception as e:
        print('json format error in file "{0}"'.format(file_name))
        return []
