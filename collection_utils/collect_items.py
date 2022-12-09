#  these functions collect fields from a list of dictionaries

# collect multiple fields
# data is the list of dictionaries
# field_names is a list of the names of the fields to be collected

def collect_multiple_fields(data, field_names):
    return [dict([(k, x[k]) for k in x.keys() if k in field_names]) for x in data]


# collect a single field
# data is the list of dictionaries
# field_name is the name of the field to be collected

def collect_single_field(data, field_name):
    return [item[field_name] for item in data]
