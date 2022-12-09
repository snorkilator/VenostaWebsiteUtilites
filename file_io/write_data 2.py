from io import StringIO
import csv
import json


# write_data uses the file ending to determine CSV or JSON formats
# data must be list of data values
# if successful, it returns a message showing the number of rows written
# if unsuccessful, it prints an error message
def write_data(file_name, data):
    if type(data) is not list:
        print('data must be in a list')
        return 'no data written'
    if file_name.endswith('.csv'):
        return write_csv_file(file_name, data)
    elif file_name.endswith('json'):
        return write_json_file(file_name, data)
    else:
        print('file name "{0}" must end in .csv or .json'. format(file_name))
        return 'no data written'


# write_csv_file assumes file_name ends in *.csv
# data must be list of data values
# if successful, it returns a message showing the number of rows written
# if unsuccessful, it prints an error message
def write_csv_file(file_name, data):
    f = StringIO()
    try:
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            return 'wrote {0} rows to {1}'.format(len(data), file_name)
    except Exception as e:
        print('error "{0}" converting csv format "{1}"'.format(e, file_name))
        return 'no data written'


# write_json_file assumes file_name ends in *.json
# data must be list of data values
# if successful, it returns a message showing the number of rows written
# if unsuccessful, it prints an error message
def write_json_file(file_name, data):
    try:
        with open(file_name, 'w', newline='') as f:
            for row in data:
                json.dump(row, f)
                f.write('\n')
            return 'wrote {0} rows to {1}'.format(len(data), file_name)
    except Exception as e:
        print('error "{0}" converting json format "{1}"'.format(e, file_name))
        return 'no data written'
