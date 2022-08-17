import csv
import json

data_dict = {}


def to_int(s):
    if s == "":
        return 0
    return int(s)


with open("/home/sugan/Documents/SIH/datas in csv/infrastructure.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    sett = {"College Name", "Website", "Area", "Year of Establishment", "Total Teachers", "Number of Study Centers", "Number of pg and off Campus Centers",
            "Speciality", "Number of Departments"}
    for rows in csv_reader:
        print(rows)
        key = rows['id']
        data_dict[key] = rows

    with open("/home/sugan/Documents/GitHub/beautiful-soup-test/infrastructure.json", 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))
