from file_io.read_data import *
from file_io.write_data import *

# change these as needed
example_csv_file_in = '../../data/fake_users.csv'
example_csv_file_out = '../../data/fake_users2.csv'
example_json_file_in = '../../data/fake_users.json'
example_json_file_out = '../../data/fake_users2.json'


# test reading a CSV file
def test_read_csv():
    return read_data(example_csv_file_in)


# test reading a JSON file
def test_read_json():
    return read_data(example_json_file_in)


# test writing CSV data to a file
def test_write_csv():
    data = read_data(example_csv_file_in)
    write_data(example_csv_file_out, data)


# test writing JSON data to a file
def test_write_json():
    data = read_data(example_json_file_in)
    write_data(example_json_file_out, data)
