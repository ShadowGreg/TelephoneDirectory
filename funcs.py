# TOTO add next functions
# search

def search_phone(input_phone_number: str, input_array: list) -> list:
    output_records = []
    for record_line in input_array:
        if input_phone_number in record_line[2]:
            output_records.append(record_line)
    return output_records
