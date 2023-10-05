import json

with open('sample.json', 'r') as json_file:

    json_data = json.load(json_file)
    print(json_data)
    print(json.dumps(json_data, indent=4))
    json_course = json.load(json_file)
    print(json_course)
    print(json.dumps(json_course, indent=4))