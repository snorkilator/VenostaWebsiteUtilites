from collection_utils.collect_items import *
from collection_utils.select_items import *
from collection_utils.sort_items import *


from file_io.examples import example_read_json

# read 1000 users from a JSON file
# this will be used in the following examples
data = example_read_json()

# example 1
# collect unique area codes using collect_single_field


def collect_unique_area_codes():
    phone_numbers = collect_single_field(data, 'phone_number')
    area_codes = [phone_number.split('-')[0] for phone_number in phone_numbers]
    # set will contain a single instance of each area_code
    # list will convert the set back into a list
    unique_area_codes = list(set(area_codes))
    # sort the area_codes
    unique_area_codes.sort()
    return unique_area_codes


# example 2
# collect first_name, last_name abd phone_number from data using collect_multiple_fields

def collect_selected_fields():
    return collect_multiple_fields(data, ['first_name', 'last_name', 'phone_number'])


# example 3
# select all of the teachers from the data using select_matching_values

def select_teachers():
    return select_matching_values(data, {'role_or_concerns': 'Teacher'})
