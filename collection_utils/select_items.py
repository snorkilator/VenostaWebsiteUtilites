#  these functions select items from a list of dictionaries

# match_dictionary_values returns true
# if the values in dict_1 match the values in dict_2
def match_dictionary_values(dict_1, dict_2):
    for k in dict_2.keys():
        if dict_1[k] != dict_2[k]:
            return False 
    return True

# select based on a dictionary of match values
# data is the list of dictionaries
# match_values is dictionary of key/value pairs

def select_matching_values(data, match_values):
    return [item for item in data if match_dictionary_values(item, match_values)]
