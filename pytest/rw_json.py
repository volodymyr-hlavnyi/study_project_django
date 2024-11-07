import json

import json

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except TypeError as err:
        raise err
    except IOError as err:
        raise err

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err

test_data = {
"pk": 4,
"title": "Test Title",
"author": "Test Author",
"published_date": "2024-06-23",
"publisher": 6,
"price": 9.99,
"discounted_price": 3.56,
"is bestseller": True,
"1s banned": False,
"genres":[1,2,3]
}