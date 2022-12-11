# TOTO add next functions
# search

def search_phone(input_phone_number: str, input_array: list):
    for record_line in input_array:
        if input_phone_number in record_line[2]:
            return record_line
