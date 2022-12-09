from file_io.read_data import *
from file_io.write_data import *

# change these as needed
example_csv_file_in = '../../data/fake_users.csv'
example_csv_file_out = '../../data/fake_users2.csv'
example_json_file_in = '../../data/fake_users.json'
example_json_file_out = '../../data/fake_users2.json'


# example reading a CSV file
def example_read_csv():
    return read_data(example_csv_file_in)


# example reading a JSON file
def example_read_json():
    return read_data(example_json_file_in)


# example writing CSV data to a file
def example_write_csv():
    data = read_data(example_csv_file_in)
    write_data(example_csv_file_out, data)


# example writing JSON data to a file
def example_write_json():
    data = read_data(example_json_file_in)
    write_data(example_json_file_out, data)
